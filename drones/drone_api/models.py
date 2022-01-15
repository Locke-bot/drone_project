from django.db import models


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



class Medication(models.Model):
    name                =       models.CharField(max_length=255)
    weight              =       models.FloatField(default=0)
    code                =       models.FloatField(default=0)
    image               =       models.ImageField(null=True, upload_to='medications', max_length=1024)
    
class Drone(models.Model):
    serial_number       =       models.CharField(max_length=100)
    model               =       models.CharField(max_length=50, choices=MODEL_CHOICES)
    weight_limit        =       models.FloatField(default=0)
    battery_capacity    =       models.FloatField(default=0)
    state               =       models.CharField(max_length=50, choices=DRONE_STATES)
    medications         =       models.ManyToManyField(Medication)
    