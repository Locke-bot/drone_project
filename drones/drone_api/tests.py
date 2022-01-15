from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from .models import Drone, Medication
import json
import types
# Create your tests here.

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.drone_endpoint = '/drones/'
        self.medication_endpoint = '/medications/'
        self.test_drone = {
            "serial_number": "12345",
            "model": "Lightweight",
            "weight_limit": 500,
            "battery_capacity": 45,
            "state": "LOADING"
        }
        
        response = self.client.post(self.drone_endpoint, self.test_drone)
        self.drone_id = json.loads(response.content).get("id")
        
    # Testing Drone Registration
    def test_drone_registration(self):
        response = self.client.post(self.drone_endpoint, {**self.test_drone, 'serial_number': '12346'})
        self.assertEquals(response.status_code, 201)
        serial_number = json.loads(response.content).get("serial_number")
        self.assertEquals(serial_number, '12346')
        
    # Testing Drone Listing
    def test_drone_get_list(self):
        response = self.client.get(self.drone_endpoint)
        self.assertEquals(response.status_code, 200)
        drones = json.loads(response.content)
        self.assertEquals(len(drones), 1)
        
    # Testing Single Drone Detail
    def test_drone_get_drone_detail(self):
        response = self.client.get(self.drone_endpoint+str(self.drone_id)+"/")
        self.assertEquals(response.status_code, 200)
        drone = json.loads(response.content)
        self.assertEquals(drone.get("model"), self.test_drone.get("model"))
        self.assertEquals(drone.get("state"), self.test_drone.get("state"))
        
    # Testing Checking Single Drone Battery Level
    def test_drone_check_drone_battery_level(self):
        response = self.client.get(self.drone_endpoint+str(self.drone_id)+"/battery_level/")
        self.assertEquals(response.status_code, 200)
        response_json = json.loads(response.content)
        self.assertEquals(response_json.get("battery_level"), 45)
        
    # Testing Updating Drone Details
    def test_drone_update_detail(self):
        response = self.client.put(self.drone_endpoint+str(self.drone_id)+"/", {**self.test_drone, 'state': 'IDLE'}, content_type="application/json" )
        self.assertEquals(response.status_code, 200)
        response_json = json.loads(response.content)
        self.assertEquals(response_json.get("state"), "IDLE")
        
            
    # Testing Get Available Drones for Loading
    def test_drone_get_drone_detail(self):
        response = self.client.get(self.drone_endpoint+"available_drones/")
        self.assertEquals(response.status_code, 200)
        drone = json.loads(response.content)
        self.assertEquals(len(drone), 1)
        


    # Testing Loading Drone with Medication Items
    def test_drone_load_medication_items(self):
        medications = [
            # Good Medication Input
            {
                "name": "Medication_1",
                "weight": 450,
                "code": "ABC",
                "drone": self.drone_id,
                "image": None
            },
            # Bad Medication Input -> Testing Medication Name is Letters, Numbers, - and _
            {
                "name": "Medication(1)",
                "weight": 450,
                "code": "ABC",
                "drone": self.drone_id,
                "image": None
            },
            # Bad Medication Input -> Testing Medication Code is Uppercase, - and _
            {
                "name": "Medication_-2",
                "weight": 450,
                "code": "abc12",
                "drone": self.drone_id,
                "image": None
            },
            # Drone Left Weight is Less than Medication Weight
            {
                "name": "Medication_-3",
                "weight": 600,
                "code": "abc12",
                "drone": self.drone_id,
                "image": None
            },
            # Drone Left Weight is Less than Medication Weight
            {
                "name": "Medication(1)1",
                "weight": 600,
                "code": "ABC",
                "drone": self.drone_id,
                "image": None
            },
            # Test medication loading without a drone
            {
                "name": "Medication2",
                "weight": 10,
                "code": "ABC",
                "drone": None,
                "image": None
            },
        ]
        
        for medication in medications:
            response = self.client.post(self.medication_endpoint, medication, content_type="application/json" )
            name = medication.get("name")
            response_json = json.loads(response.content)
            
            if name == "Medication_1":
                self.assertEquals(response.status_code, 201)
                self.assertEquals(response_json.get("weight"), 450)
                
            elif name == "Medication(1)":
                self.assertEquals(response.status_code, 400)
                self.assertEquals(type(response_json.get("name")), type([]))
                
            elif name == "Medication_-3":
                self.assertEquals(response.status_code, 400)
                self.assertEquals(type(response_json.get("name")), type([]))
            
            elif name == "Medication(1)1":
                self.assertEquals(response.status_code, 400)
                self.assertEquals(type(response_json.get("weight")), type([]))
            
            elif name == "Medication2":
                self.assertEquals(response.status_code, 400)
                self.assertEquals(type(response_json.get("drone")), type([]))
                
    # Testing Checking Single Drone Battery Level
    def test_drone_check_loaded_medication(self):
        medications = [
            {
                "name": "Medication_1",
                "weight": 50,
                "code": "ABC1",
                "drone": self.drone_id,
                "image": None
            },
            {
                "name": "Medication_2",
                "weight": 50,
                "code": "ABC2",
                "drone": self.drone_id,
                "image": None
            },
            {
                "name": "Medication_3",
                "weight": 50,
                "code": "ABC3",
                "drone": self.drone_id,
                "image": None
            },
        ]
        
        for medication in medications:
            response = self.client.post(self.medication_endpoint, medication, content_type="application/json" )
            self.assertEquals(response.status_code, 201)
         
        response = self.client.get(self.drone_endpoint+str(self.drone_id)+"/loaded_medication_items/")  
        response_json = json.loads(response.content)
        self.assertEquals(len(response_json.get("medication_items")), 3)
        
        
        