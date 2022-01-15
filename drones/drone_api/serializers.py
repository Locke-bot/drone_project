from enum import unique

from django.db.models.query_utils import Q
from rest_framework import serializers
from .models import Drone, Medication
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator
from django.db.models import Sum

class DroneSerializer(serializers.ModelSerializer):
    serial_number       =       serializers.CharField(max_length=100, required=True, 
                                                           validators=[UniqueValidator(queryset=Drone.objects.all())])
    model               =       serializers.CharField(max_length=50, required=True)
    weight_limit        =       serializers.FloatField(min_value=0, max_value=500, required=True)
    battery_capacity    =       serializers.IntegerField(min_value=0, max_value=100, required=True)
    
    class Meta:
        model = Drone
        fields = "__all__"


class MedicationSerializer(serializers.ModelSerializer):
    
    name                =       serializers.CharField(max_length=255, required=True,
                                                        validators=[RegexValidator('^[A-Za-z0-9_]*$',
                                                        'Only letters, numbers, - and _ are allowed.')])
    weight              =       serializers.FloatField(default=0, min_value=0, max_value=500)
    code                =       serializers.CharField(max_length=255, required=True,
                                                        validators=[RegexValidator('^[A-Z0-9_]*$',
                                                        'Only uppercase letters, numbers and _ are allowed.')])
    drone               =       serializers.PrimaryKeyRelatedField(many=False, required=True, 
                                                        queryset=Drone.objects.filter(Q(state="LOADING")&Q(battery_capacity__gte = 25)).all())
    
    def validate_weight(self, value):
        drone_id = self.initial_data.get("drone", None)
        drone = Drone.objects.filter(pk=drone_id).first()
        if drone :
            weight = drone.weight_limit - drone.loaded_weight()
            if self.instance and self.instance.drone.pk == drone.pk:
                weight = weight + self.instance.weight
            if (weight >= value):
                return value
            raise serializers.ValidationError("Selected drone can not take more "+str(weight)+"g medication currently.")
        raise serializers.ValidationError("Select one drone please.")    
    class Meta:
        model = Medication
        fields = "__all__"

