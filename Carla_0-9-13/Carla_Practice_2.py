import carla
import time
import logging

client = carla.Client('localhost', 2000)
#
# client.load_world('Town05')
#
# # client.start_recorder('recording.log')
#
# world = client.get_world()
# print("world", world)
#
# level = world.get_map()
# print("level", level)
#
# weather = world.get_weather()
# print("weather", weather, "\n\n")
#
# blueprint_library = world.get_blueprint_library()
# print("blueprint_library", blueprint_library)

# Setting synchronous mode
# settings = world.get_settings()
# settings.synchronous_mode = False  # Enables synchronous mode
# settings.fixed_delta_seconds = 0.05
# world.apply_settings(settings)

# Using synchronous mode
# settings = world.get_settings()
# settings.synchronous_mode = True
# world.apply_settings(settings)
#
# camera = world.spawn_actor(blueprint, transform)
# image_queue = queue.Queue()
# camera.listen(image_queue.put)
#
# while True:
#     world.tick()
#     image = image_queue.get()

client.start_recorder("/home/zhihao/PycharmProjects/CarlaPractices/CarlaSaved/recording01.log")
time.sleep(3)
client.stop_recorder()
client.replay_file("/home/zhihao/PycharmProjects/CarlaPractices/CarlaSaved/recording01.log", start=0, duration=2, camera=0)
