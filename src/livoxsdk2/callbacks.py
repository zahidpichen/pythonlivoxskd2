from livox_lidar_api import *

def on_device_info_change(handle, info, client_data):
    # Handle device discovery events
    if info:
        print(f"Device discovered: {info.sn}, IP: {info.lidar_ip}")

def on_connection_status_change(handle, info, client_data):
    # Handle connection status changes
    if info:
        print(f"Connected to device: {info.sn}, IP: {info.lidar_ip}")

def on_point_cloud_received(handle, data, client_data):
    # Handle point cloud data reception
    if data:
        print(f"Received {data.dot_num} points from device {handle}")

def on_work_mode_change(status, handle, response, client_data):
    # Handle work mode change responses
    if status == kLivoxLidarStatusSuccess:
        print(f"Work mode changed successfully for device {handle}")
    else:
        print(f"Failed to change work mode for device {handle}: {response.ret_code}")