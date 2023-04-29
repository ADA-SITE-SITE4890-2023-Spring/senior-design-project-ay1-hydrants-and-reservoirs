from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("login/", obtain_auth_token, name="login"),
    
    
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', signIn, name="signIn"),
    path('map', mapPage, name="mapPage"),
    path('list/', listPage, name="listPage"),
    path('checkup/', checkup, name="checkup"),
    path('create_hydrant_checkup/<int:pk>', create_hydrant_checkup, name="create_hydrant_checkup"),
    path('create_reservoir_checkup/<int:pk>', create_reservoir_checkup, name="create_reservoir_checkup"),
    
    
    path('hydrants/', hydrants, name="hydrants"),
    path('reservoirs/', reservoirs, name="reservoirs"),
    
    #APIs 
    path('api/Reservoirs/', ReservoirList.as_view(), name='ReservoirList'),
    path('api/Hydrants/', HydrantList.as_view(), name='HydrantList'),
    path('api/HydrantCheckup/', check_up_hydrantList.as_view(), name='HydrantCheckup'),
    path('api/ReservoirCheckup/', check_up_reservoirList.as_view(), name='ReservoirCheckup'),
    
    
    
    
    
    
    
]
