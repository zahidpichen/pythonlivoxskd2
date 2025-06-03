from livoxsdk2.types import LivoxLidarInfo, LivoxLidarPointCloud
from livoxsdk2.callbacks import DeviceInfoChangeCallback, PointCloudCallback
from livoxsdk2.utils import create_config_file
import threading

class LiDAR:
    def __init__(self, host_ip="192.168.1.10"):
        self.host_ip = host_ip
        self.connected = False
        self.device_info = None
        self.point_cloud_data = []
        self.lock = threading.Lock()

    def discover_devices(self):
        create_config_file(self.host_ip)
        # Call the SDK function to discover devices
        # This should set self.device_info with discovered devices
        # Example: self.device_info = discover(self.host_ip)

    def connect(self):
        if not self.device_info:
            raise RuntimeError("No devices discovered. Please run discover_devices() first.")
        
        # Connect to the first discovered device
        # Example: self.connected = connect_to_device(self.device_info[0])

    def start(self):
        if not self.connected:
            raise RuntimeError("Device not connected. Please connect first.")
        
        # Start the LiDAR
        # Example: start_lidar(self.device_info[0].ip)

    def stop(self):
        if not self.connected:
            raise RuntimeError("Device not connected. Please connect first.")
        
        # Stop the LiDAR
        # Example: stop_lidar(self.device_info[0].ip)

    def record_point_cloud(self):
        if not self.connected:
            raise RuntimeError("Device not connected. Please connect first.")
        
        # Start recording point cloud data
        # Example: start_recording(self.device_info[0].ip)

    def get_point_cloud(self):
        with self.lock:
            return self.point_cloud_data

    def point_cloud_callback(self, data: LivoxLidarPointCloud):
        with self.lock:
            self.point_cloud_data.append(data)

    def device_info_change_callback(self, info: LivoxLidarInfo):
        self.device_info = info
        # Handle device info change, e.g., update UI or log info

# Example usage:
# lidar = LiDAR()
# lidar.discover_devices()
# lidar.connect()
# lidar.start()