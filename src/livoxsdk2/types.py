# This file defines custom types and data structures used throughout the package.

from enum import Enum

class LidarWorkMode(Enum):
    NORMAL = 0
    SLEEP = 1
    STANDBY = 2

class LidarDeviceType(Enum):
    HUB = 0
    MID40 = 1
    TELE = 2
    HORIZON = 3
    MID70 = 4
    AVIA = 5
    MID360 = 6
    INDUSTRIAL_HAP = 7
    HAP = 8
    PA = 9

class LidarStatus(Enum):
    SUCCESS = 0
    FAILURE = 1

class LidarPointCloudData:
    def __init__(self, x, y, z, reflectivity):
        self.x = x
        self.y = y
        self.z = z
        self.reflectivity = reflectivity

class LidarConfig:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

# Additional types and data structures can be defined here as needed.