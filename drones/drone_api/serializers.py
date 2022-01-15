from rest_framework import serializers
from .models import Drone, Medication
from django.core.validators import RegexValidator

class DroneSerializer(serializers.HyperlinkedModelSerializer):
    serial_number       =       serializers.CharField(max_length=100, required=True)
    model               =       serializers.CharField(max_length=50, required=True)
    weight_limit        =       serializers.FloatField(min_value=0, max_value=500, required=True)
    battery_capacity    =       serializers.IntegerField(min_value=0, max_value=100, required=True)
    
    class Meta:
        model = Drone
        fields = "__all__"


class MedicationSerializer(serializers.HyperlinkedModelSerializer):
    
    name                =       serializers.CharField(max_length=255, required=True,
                                                      validators=[RegexValidator('^[A-Za-z0-9_]*$',
                                                        'Only letters, numbers, - and _ are allowed.')])
    weight              =       serializers.FloatField(default=0, min_value=0, max_value=500)
    code                =       serializers.CharField(max_length=255, required=True,
                                                      validators=[RegexValidator('^[A-Z0-9_]*$',
                                                        'Only uppercase letters, numbers and _ are allowed.')])
    
    # image               =       serializers.ImageField(null=True, upload_to='medications', max_length=1024)
    
    class Meta:
        model = Medication
        fields = "__all__"

