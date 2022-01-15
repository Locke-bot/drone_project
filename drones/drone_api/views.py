from django.db.models.query_utils import Q
from rest_framework import viewsets, status
from .serializers import DroneSerializer, MedicationSerializer
from .models import Drone, Medication
from rest_framework.response import Response
from rest_framework.decorators import action

class DroneViewSet(viewsets.ModelViewSet):
    queryset                =   Drone.objects.all()
    serializer_class        =   DroneSerializer
    permission_classes      =   []
    
    @action(detail=True, methods=["get"], name="Loaded Medication Items",  permission_classes=[])
    def loaded_medication_items(self, request, pk=None):
        drone = Drone.objects.filter(pk=pk).first()
        if drone:
            medication_items = Medication.objects.filter(drone_id=pk)
            result = {
                "drone": DroneSerializer(drone).data,
                "medication_items": MedicationSerializer(medication_items, many=True).data
            }
            return Response(result)
        return Response({"detail" : "Drone does not exist"}, status=status.HTTP_400_BAD_REQUEST)  
    
    
    @action(detail=True, methods=["get"], name="Loaded Medication Items",  permission_classes=[])
    def battery_level(self, request, pk=None):
        drone = Drone.objects.filter(pk=pk).first()
        if drone:
            return Response({ "battery_level": drone.battery_capacity })
        return Response({"detail" : "Drone does not exist"}, status=status.HTTP_400_BAD_REQUEST)  
    

    @action(detail=False, methods=["get"], name="Available Drones for Loading",  permission_classes=[])
    def available_drones(self, request, pk=None):
        drones = Drone.objects.filter(Q(state="LOADING")&Q(battery_capacity__gte = 25)).all()
        return Response(DroneSerializer(drones, many=True).data)


class MedicationViewSet(viewsets.ModelViewSet):
    queryset                =   Medication.objects.all()
    serializer_class        =   MedicationSerializer
    permission_classes      =   []

