import pybullet as p
import time

p.connect(p.GUI)
custom_model_path = "C:/Users/girij/Distributed systems/models"
p.setAdditionalSearchPath(custom_model_path)

try:
    robot = p.loadURDF("simple_robot.urdf", basePosition=[0, 0, 0.1])
    print("Robot loaded successfully.")
except Exception as e:
    print(f"Failed to load robot URDF: {e}")

time.sleep(5)
p.disconnect()
