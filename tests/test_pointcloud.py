import pytest
from livoxsdk2.lidar import LiDAR

def test_point_cloud_data():
    lidar = LiDAR()
    assert lidar.connect() == True  # Test connection to the LiDAR

    lidar.start()  # Start the LiDAR
    point_cloud_data = lidar.get_point_cloud()  # Retrieve point cloud data

    assert point_cloud_data is not None  # Ensure point cloud data is received
    assert len(point_cloud_data) > 0  # Ensure there is data in the point cloud

    lidar.stop()  # Stop the LiDAR
    lidar.disconnect()  # Disconnect from the LiDAR

def test_point_cloud_reflectivity():
    lidar = LiDAR()
    assert lidar.connect() == True  # Test connection to the LiDAR

    lidar.start()  # Start the LiDAR
    point_cloud_data, reflectivity_data = lidar.get_point_cloud_with_reflectivity()  # Retrieve point cloud and reflectivity data

    assert point_cloud_data is not None  # Ensure point cloud data is received
    assert reflectivity_data is not None  # Ensure reflectivity data is received
    assert len(point_cloud_data) == len(reflectivity_data)  # Ensure point cloud and reflectivity data lengths match

    lidar.stop()  # Stop the LiDAR
    lidar.disconnect()  # Disconnect from the LiDAR