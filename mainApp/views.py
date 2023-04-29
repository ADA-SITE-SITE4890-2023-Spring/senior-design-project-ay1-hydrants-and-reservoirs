from django.shortcuts import render,redirect
from django.template import loader
from .models import Hydrant, Reservoir, check_up_hydrant, check_up_reservoir
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=raw_password)
            # and not user.is_superuser
            if user is not None and not user.is_superuser :
                login(request,user)
                
                
                # messages.success(request, 'successfully login')
                return redirect('mapPage')
            else:
                # messages.error(
                    # request, 'Please enter correct username and password combination')
                return redirect('/')
    else:
        form = SignInForm()
    
    if request.user.is_authenticated:
        return redirect('mapPage')

    return render(request, 'main/login.html', {'form': form})


@login_required
def mapPage(request):
    return render(request, 'main/map.html')


@login_required
def listPage(request):
    user_token = Token.objects.get_or_create(user=request.user)
    print(user_token[0])
    if request.method == 'POST':
        search_text = request.POST['search_text']
        hydrant = Hydrant.objects.filter(
            Q(name = search_text) |
            Q(address = search_text) |
            Q(coordinates = search_text) |
            Q(status = search_text) 
        )
        
        reservoir = Reservoir.objects.filter(
            Q(name = search_text) |
            Q(address = search_text) |
            Q(coordinates = search_text) |
            Q(status = search_text) 
        )
        context ={
            'hydrant' : hydrant,
            'reservoir': reservoir,
            'token': user_token[0] 
             
        }
        return render(request, 'main/list.html', context)
    hydrant = Hydrant.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(hydrant, 5)
    try:
        hydrant = paginator.page(page)
    except PageNotAnInteger:
        hydrant = paginator.page(1)
    except EmptyPage:
        hydrant = paginator.page(paginator.num_pages)
        
    reservoir = Reservoir.objects.all()
    reservoirpage = request.GET.get('reservoirpage', 1)
    reservoir_paginator = Paginator(reservoir, 5)
    try:
        reservoir = reservoir_paginator.page(reservoirpage)
    except PageNotAnInteger:
        reservoir = reservoir_paginator.page(1)
    except EmptyPage:
        reservoir = reservoir_paginator.page(reservoir_paginator.num_pages)
    
    
    context ={
        'hydrant' : hydrant,
        'reservoir': reservoir,
        'token': user_token[0] 
        
    }
    return render(request, 'main/list.html', context)

from datetime import date

today = date.today()

@login_required
def create_hydrant_checkup(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        hydrant = Hydrant.objects.get(id=pk)
        
        information = request.POST['information']
        pressure = request.POST['pressure']
        
        hydrant_image = request.FILES.get('hydrant_image', None)
        print(hydrant_image)
        if hydrant_image:
            
            check_up =check_up_hydrant.objects.create(
                user = user,
                picture = hydrant_image,
                date = today,
                pressure = pressure,
                information = information,
                Hydrant = hydrant
            )
        else:
            
            check_up =check_up_hydrant.objects.create(
                user = user,
                date = today,
                pressure = pressure,
                information = information,
                Hydrant = hydrant
            )
            
        return redirect('hydrants')
        
    return render(request, 'main/hydrant_check.html')


@login_required
def create_reservoir_checkup(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        reservoir = Reservoir.objects.get(id=pk)
        
        information = request.POST['information']
        distance = request.POST['distance']
        
        reservoir_image = request.FILES.get('reservoir_image', None)
        if reservoir_image:
            check_up = check_up_reservoir.objects.create(
                user = user,
                picture = reservoir_image,
                date = today,
                distance= distance,
                information = information,
                Reservoir = reservoir
            )
        else:
            check_up = check_up_reservoir.objects.create(
                user = user,
                date = today,
                distance=distance,
                information = information,
                Reservoir = reservoir
            )
        return redirect('reservoirs')
        
    return render(request, 'main/reservoir-check.html')


@login_required
def checkup(request):
    return render(request, 'main/checkups.html')


@login_required
def hydrants(request):
    user = User.objects.get(id=request.user.id)
    print(user)
    checkups = check_up_hydrant.objects.filter(user= user)
    print(checkups)
    
    context ={
        'checkups': checkups 
    }
    return render(request, 'main/hydrant_check_table.html',context)


@login_required
def reservoirs(request):
    user = User.objects.get(id=request.user.id)
    checkups = check_up_reservoir.objects.filter(user= user)
    print(checkups)
    
    context ={
        'checkups': checkups 
    }
    return render(request, 'main/reservoir_check_table.html',context)



class ReservoirList(APIView):
    
    permission_classes =[IsAuthenticated]
    
    def get(self, request):
        reservoir = Reservoir.objects.all()

        serializer = ReservoirSerializer(reservoir, many=True)
        
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        
        serializer = ReservoirSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
        
class HydrantList(APIView):
    permission_classes =[IsAuthenticated]
    
    def get(self, request):
        
        hydrant = Hydrant.objects.all()
        serializer = HydrantSerializer(hydrant, many=True)
        
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        
        serializer = HydrantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
        
class check_up_hydrantList(APIView):
    print('LOLLOLOLOLOL')
    permission_classes =[IsAuthenticated]
    
    def get(self, request):
        
        check_up_hydrant_data = check_up_hydrant.objects.all()
        serializer = check_up_hydrantSerializer(check_up_hydrant_data, many=True)
        
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def post(self, request):
        
        serializer = check_up_hydrantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
    
    
class check_up_reservoirList(APIView):
    permission_classes =[IsAuthenticated]
    
    def get(self, request):
        
        check_up_reservoir_data = check_up_reservoir.objects.all()
        serializer = check_up_reservoirSerializer(check_up_reservoir_data, many=True)
        
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
        
    def post(self, request):
        
        serializer = check_up_reservoirSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
        
        
        
     
for user in User.objects.all():
    Token.objects.get_or_create(user=user)