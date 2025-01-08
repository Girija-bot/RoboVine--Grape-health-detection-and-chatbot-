import pybullet as p
import pybullet_data

def setup_field():
    print("Initializing PyBullet...")
    p.connect(p.GUI)

    # Add PyBullet's default and custom search paths
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Default PyBullet data path
    custom_model_path = "C:/Users/girij/Distributed systems/models"  # Adjust if necessary
    p.setAdditionalSearchPath(custom_model_path)

    # Set gravity
    p.setGravity(0, 0, -9.8)
    print("Gravity set.")

    # Create a ground plane dynamically
    try:
        plane_id = p.createCollisionShape(p.GEOM_PLANE)
        p.createMultiBody(0, plane_id)
        print("Ground plane created dynamically.")
    except Exception as e:
        print(f"Error creating ground plane: {e}")
        raise

    # Add plants with spacing
    plant_positions = []
    plane_size = 10  # 10x10 plane
    spacing = 2.0    # Space between plants

    plants = []
    for x in range(-plane_size // 2, plane_size // 2):
        for y in range(-plane_size // 2, plane_size // 2):
            pos = [x * spacing, y * spacing, 0]
            try:
                plant_id = p.loadURDF("plant.urdf", basePosition=pos)
                p.changeDynamics(plant_id, -1, mass=0)  # Make plants static
                plants.append({"id": plant_id, "position": pos})
                print(f"Plant added at {pos}.")
            except Exception as e:
                print(f"Failed to load plant at {pos}: {e}")

    # Add the robot
    try:
        robot = p.loadURDF("simple_robot.urdf", basePosition=[0, 0, 0.2])
        print("Robot loaded successfully.")
    except Exception as e:
        print(f"Failed to load robot: {e}")
        return None, None

    return robot, plants
