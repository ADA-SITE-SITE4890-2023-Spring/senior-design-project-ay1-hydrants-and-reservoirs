from django.db import models

from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token





@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Reservoir(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)
    depth = models.FloatField(default=0)
    water_level = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Reservoir_id = {}, Adress = {} , Status = {}".format(str(self.id),str(self.address),str(self.status))


class Hydrant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    coordinates = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    cap_diameter = models.IntegerField(default=0)
    # pressure =models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Hydrant_id = {}, Adress = {} , Status = {}".format(str(self.id),str(self.address),str(self.status))


class check_up_hydrant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture=models.FileField(upload_to="pictures/", null=True, blank=True)
    confirmed= models.BooleanField(default=False)
    date=models.DateField()
    information = models.TextField()
    pressure =models.FloatField(default=0)
    Hydrant=models.ForeignKey(Hydrant,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Check_up_id={}  confirmed ={}".format(self.id,str(self.confirmed))


class check_up_reservoir(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture=models.FileField(upload_to="pictures/", null=True, blank=True)
    confirmed = models.BooleanField(default=False)
    date=models.DateField()
    information = models.TextField()
    distance =models.FloatField(default=0)
    
    Reservoir=models.ForeignKey(Reservoir,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "Check_up_id={}  confirmed ={}".format(self.id,str(self.confirmed))
    
    
