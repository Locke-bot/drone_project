from django.urls import include, path
from rest_framework import routers
from .views import DroneViewSet, MedicationViewSet

router = routers.DefaultRouter()
router.register(r'drones', DroneViewSet)
router.register(r'medications', MedicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]