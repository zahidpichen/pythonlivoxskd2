#ifndef LIVOX_INTERFACE_H_
#define LIVOX_INTERFACE_H_

#include "livox_lidar_api.h"

// Function declarations for interacting with the Livox SDK
void initialize_sdk(const char* config_path);
void start_device_scanning();
void stop_device_scanning();
void set_point_cloud_callback(LivoxLidarPointCloudCallBack callback, void* client_data);
void set_info_change_callback(LivoxLidarInfoChangeCallback callback, void* client_data);
void connect_to_device(uint32_t handle);
void disconnect_from_device(uint32_t handle);
void set_work_mode(uint32_t handle, LivoxLidarWorkMode mode);
void get_device_info(uint32_t handle, LivoxLidarInfo* info);

#endif  // LIVOX_INTERFACE_H_