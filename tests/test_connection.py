import pytest
from livoxsdk2.lidar import LivoxLidar

def test_device_discovery():
    lidar = LivoxLidar()
    devices = lidar.discover(timeout_seconds=5)
    assert isinstance(devices, list)
    assert len(devices) > 0

def test_auto_connect():
    lidar = LivoxLidar()
    result = lidar.auto_connect(timeout_seconds=5)
    assert result["success"] is True
    assert "sn" in result
    assert "ip" in result

def test_connection_error_handling():
    lidar = LivoxLidar()
    result = lidar.auto_connect(host_ip="192.168.1.100", timeout_seconds=5)
    assert result["success"] is False
    assert "error" in result

def test_start_lidar():
    lidar = LivoxLidar()
    lidar.auto_connect(timeout_seconds=5)
    assert lidar.start_lidar() is True

def test_stop_lidar():
    lidar = LivoxLidar()
    lidar.auto_connect(timeout_seconds=5)
    lidar.start_lidar()
    assert lidar.stop_lidar() is True