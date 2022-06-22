import carla
import random

client = carla.Client('localhost', 2000)
world = client.get_world()
blueprint_library = world.get_blueprint_library()
print("blueprint_library", blueprint_library, "\n\n")
# Find a specific blueprint.
collision_sensor_bp = blueprint_library.find('sensor.other.collision')
print("collision_sensor_bp", collision_sensor_bp, "\n\n")
# Choose a vehicle blueprint at random.
vehicle_bp = random.choice(blueprint_library.filter('vehicle.*.*'))
print("vehicle_bp", vehicle_bp, "\n\n")

# is_bike = [vehicle.get_attribute('number_of_wheels') == 2]
# if(is_bike):
#     vehicle.set_attribute('color', '255,0,0')

