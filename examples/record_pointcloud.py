import time
import livoxsdk2.lidar as lidar

def main():
    # Initialize the LiDAR SDK
    if not lidar.initialize():
        print("Failed to initialize LiDAR SDK.")
        return

    # Discover LiDAR devices
    devices = lidar.discover()
    if not devices:
        print("No LiDAR devices found.")
        return

    # Automatically connect to the first available LiDAR
    device_info = lidar.auto_connect()
    if not device_info['success']:
        print(f"Connection failed: {device_info['error']}")
        return

    print(f"Connected to LiDAR: {device_info['sn']} at {device_info['ip']}")

    # Start recording point cloud data
    if not lidar.start_recording(device_info['ip']):
        print("Failed to start recording.")
        return

    print("Recording point cloud data... Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)  # Keep the script running to record data
    except KeyboardInterrupt:
        print("Stopping recording...")

    # Stop recording point cloud data
    if not lidar.stop_recording():
        print("Failed to stop recording.")

    print("Recording stopped.")

if __name__ == "__main__":
    main()