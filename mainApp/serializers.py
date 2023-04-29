from dataclasses import fields
from rest_framework import serializers
from .models import *


class ReservoirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservoir
        fields = '__all__'
        
        
class HydrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hydrant
        fields = '__all__'
        
class check_up_hydrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = check_up_hydrant
        fields = '__all__'
        
class check_up_reservoirSerializer(serializers.ModelSerializer):
    class Meta:
        model = check_up_reservoir
        fields = '__all__'