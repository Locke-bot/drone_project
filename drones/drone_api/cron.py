from .models import BatteryLevelLog, Drone

def log_battery(drone):
    log_data = {
        "drone_id"            :   drone.pk,
        "serial_number"       :   drone.serial_number,
        "battery_level"       :   drone.battery_capacity,
        "state"               :   drone.state
    }
    log = BatteryLevelLog(**log_data)
    log.save()
    
def check_drones_battery():
    [ log_battery(drone) for drone in Drone.objects.all() ]
    
      
      