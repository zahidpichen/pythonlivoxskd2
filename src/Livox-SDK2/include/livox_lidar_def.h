// This file defines constants, enums, and data structures used by the Livox SDK. 

#ifndef LIVOX_LIDAR_DEF_H_
#define LIVOX_LIDAR_DEF_H_

#include <stdint.h>

// Livox LiDAR device types
typedef enum {
    kLivoxLidarTypeHub,
    kLivoxLidarTypeMid40,
    kLivoxLidarTypeTele,
    kLivoxLidarTypeHorizon,
    kLivoxLidarTypeMid70,
    kLivoxLidarTypeAvia,
    kLivoxLidarTypeMid360,
    kLivoxLidarTypeIndustrialHAP,
    kLivoxLidarTypeHAP,
    kLivoxLidarTypePA,
    kLivoxLidarTypeUnknown
} LivoxLidarType;

// Livox LiDAR work modes
typedef enum {
    kLivoxLidarNormal,
    kLivoxLidarSleep,
    kLivoxLidarStandby,
    kLivoxLidarWorkModeMax
} LivoxLidarWorkMode;

// Livox LiDAR point data types
typedef enum {
    kLivoxLidarCartesianCoordinateHighData,
    kLivoxLidarCartesianCoordinateLowData,
    kLivoxLidarSphericalCoordinateData,
    kLivoxLidarPointDataTypeMax
} LivoxLidarPointDataType;

// Livox LiDAR status codes
typedef enum {
    kLivoxLidarStatusSuccess,
    kLivoxLidarStatusFailure,
    kLivoxLidarStatusBusy,
    kLivoxLidarStatusInvalid,
    kLivoxLidarStatusMax
} livox_status;

// Structure to hold LiDAR information
typedef struct {
    char sn[32];               // Serial number
    char lidar_ip[16];         // IP address
    LivoxLidarType dev_type;   // Device type
} LivoxLidarInfo;

// Structure for SDK version information
typedef struct {
    uint32_t major;            // Major version
    uint32_t minor;            // Minor version
    uint32_t patch;            // Patch version
} LivoxLidarSdkVer;

// Other necessary structures and definitions can be added here

#endif  // LIVOX_LIDAR_DEF_H_