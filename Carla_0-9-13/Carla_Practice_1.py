import carla
import random

# Connect to the client and retrieve the world object
client = carla.Client('localhost', 2000)
world = client.get_world()
# Retrieve the spectator object
spectator = world.get_spectator()
# world.load_world('Town05')
# Get the location and rotation of the spectator through its transform
transform = spectator.get_transform()

location = transform.location
rotation = transform.rotation
print("location", location, "rotation", rotation)

# Set the spectator with an empty transform
# spectator.set_transform(carla.Transform())
# This will set the spectator at the origin of the map, with 0 degrees
# pitch, yaw and roll - a good way to orient yourself in the map

# Get the blueprint library and filter for the vehicle blueprints
vehicle_blueprints = world.get_blueprint_library().filter('*vehicle*')
print("vehicle_blueprints \n", vehicle_blueprints)
print("vehicle_blueprints Type \n", type(vehicle_blueprints))
# Get the map's spawn points
spawn_points = world.get_map().get_spawn_points()
print("spawn_points", spawn_points)

# Spawn 50 vehicles randomly distributed throughout the map
# for each spawn point, we choose a random vehicle from the blueprint library
#for i in range(0, 50):
#    world.try_spawn_actor(random.choice(vehicle_blueprints, random.choice(spawn_points)))

ego_vehicle = world.spawn_actor(random.choice(vehicle_blueprints), random.choice(spawn_points))
