from django.db import models
from django.db.models.aggregates import Sum

MODEL_CHOICES = (
    ("Lightweight", "Lightweight"),
    ("Middleweight", "Middleweight"),
    ("Cruiserweight", "Cruiserweight"),
    ("Heavyweight", "Heavyweight")
)

DRONE_STATES = (
    ("IDLE", "IDLE"),
    ("LOADING", "LOADING"),
    ("DELIVERING", "DELIVERING"),
    ("DELIVERED", "DELIVERED"),
    ("RETURNING", "RETURNING")
)


class Drone(models.Model):
    serial_number       =       models.CharField(max_length=100, unique=True)
    model               =       models.CharField(max_length=50, choices=MODEL_CHOICES)
    weight_limit        =       models.FloatField(default=0)
    battery_capacity    =       models.IntegerField(default=0)
    state               =       models.CharField(max_length=50, choices=DRONE_STATES)
    
    def loaded_weight(self):
        loaded_weight = Medication.objects.filter(drone=self).aggregate(Sum("weight")).get("weight__sum", 0)
        return loaded_weight if(loaded_weight != None) else 0
        
    
class Medication(models.Model):
    name                =       models.CharField(max_length=255)
    weight              =       models.FloatField(default=0)
    code                =       models.CharField(max_length=255)
    image               =       models.ImageField(null=True, upload_to='medications', max_length=1024)
    drone               =       models.ForeignKey(Drone, null=True, on_delete=models.SET_NULL)
    