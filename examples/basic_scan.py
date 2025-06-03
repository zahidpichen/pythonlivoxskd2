import sys
import time
from livoxsdk2.lidar import LivoxLidar

def main():
    # Create an instance of the LivoxLidar class
    lidar = LivoxLidar()

    # Connect to the LiDAR device
    if not lidar.connect():
        print("Failed to connect to LiDAR device.")
        sys.exit(1)

    print("Connected to LiDAR device.")

    # Start scanning
    lidar.start_scanning()
    print("Scanning started...")

    try:
        # Continuously retrieve point cloud data
        while True:
            point_cloud_data = lidar.get_point_cloud()
            if point_cloud_data:
                print(f"Received {len(point_cloud_data)} points.")
            time.sleep(1)  # Adjust the sleep time as needed
    except KeyboardInterrupt:
        print("Stopping scanning...")

    # Stop scanning and disconnect
    lidar.stop_scanning()
    lidar.disconnect()
    print("Disconnected from LiDAR device.")

if __name__ == "__main__":
    main()