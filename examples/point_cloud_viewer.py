import sys
import numpy as np
import openpylivoxv2  # Assuming this is the name of the compiled module
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_point_cloud(points, reflectivity):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Normalize reflectivity for color mapping
    reflectivity_normalized = (reflectivity - np.min(reflectivity)) / (np.max(reflectivity) - np.min(reflectivity))
    colors = plt.cm.viridis(reflectivity_normalized)

    ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=colors, s=1)
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Z (m)')
    plt.title('Point Cloud Visualization')
    plt.show()

def main():
    host_ip = "192.168.1.10"  # Change to your LiDAR's IP address
    lidar = openpylivoxv2.auto_connect(host_ip)

    if not lidar["success"]:
        print(f"Connection failed: {lidar['error']}")
        sys.exit(1)

    print(f"Connected to LiDAR: {lidar['sn']}")

    # Start recording point cloud data
    if not openpylivoxv2.start_recording(host_ip):
        print("Failed to start recording.")
        sys.exit(1)

    print("Recording point cloud data... Press Ctrl+C to stop.")

    try:
        while True:
            points_array, reflectivity_array = openpylivoxv2.get_point_cloud()
            points = np.array(points_array)
            reflectivity = np.array(reflectivity_array)
            visualize_point_cloud(points, reflectivity)
    except KeyboardInterrupt:
        print("Stopping recording...")
        openpylivoxv2.stop_recording()

if __name__ == "__main__":
    main()