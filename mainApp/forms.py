from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from users.models import User
from django.contrib.auth.models import User
from .models import *



class SignInForm(forms.Form):
    username = forms.CharField(label='username', max_length=300, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, label='Password', required=True)

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter UserName'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'
        
        


# class check_up_hydrantForm(forms.ModelForm):
#     class Meta:
#         model = check_up_hydrant
#         fields = ('name','')

#     def __init__(self, *args, **kwargs):
#         super(CityForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs['class'] = 'form-control'
#         self.fields['name'].widget.attrs['placeholder'] = 'Type City Name here'