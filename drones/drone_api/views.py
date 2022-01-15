from rest_framework import viewsets
from .serializers import DroneSerializer, MedicationSerializer
from .models import Drone, Medication

class DroneViewSet(viewsets.ModelViewSet):
    queryset                =   Drone.objects.all()
    serializer_class        =   DroneSerializer
    permission_classes      =   []


class MedicationViewSet(viewsets.ModelViewSet):
    queryset                =   Medication.objects.all()
    serializer_class        =   MedicationSerializer
    permission_classes      =   []

