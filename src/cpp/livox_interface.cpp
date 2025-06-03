#include "livox_interface.h"
#include "livox_lidar_api.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <vector>
#include <string>
#include <mutex>
#include <atomic>

// Namespace for pybind11
namespace py = pybind11;

// Global state
std::mutex device_mutex;
std::vector<LivoxLidarInfo> discovered_devices;
std::atomic<bool> is_recording(false);

// Callback function for device discovery
void DeviceInfoChangeCallback(uint32_t handle, const LivoxLidarInfo* info, void*) {
    if (!info) return;
    std::lock_guard<std::mutex> lk(device_mutex);
    discovered_devices.push_back(*info);
    std::cout << "Discovered LiDAR - Handle: " << handle
              << " Type: " << static_cast<int>(info->dev_type)
              << " SN: " << info->sn
              << " IP: " << info->lidar_ip << std::endl;
}

// Function to discover Livox LiDAR devices
py::list discover_devices() {
    std::lock_guard<std::mutex> lock(device_mutex);
    discovered_devices.clear();

    if (!LivoxLidarSdkInit("./livox_config.json")) {
        throw std::runtime_error("Failed to initialize Livox SDK");
    }

    SetLivoxLidarInfoChangeCallback(DeviceInfoChangeCallback, nullptr);
    if (!LivoxLidarSdkStart()) {
        LivoxLidarSdkUninit();
        throw std::runtime_error("Failed to start Livox SDK");
    }

    std::this_thread::sleep_for(std::chrono::seconds(5));

    py::list devices;
    for (const auto& device : discovered_devices) {
        py::dict device_info;
        device_info["dev_type"] = static_cast<int>(device.dev_type);
        device_info["sn"] = device.sn;
        device_info["ip"] = device.lidar_ip;
        devices.append(device_info);
    }

    LivoxLidarSdkUninit();
    return devices;
}

// Function to start recording point cloud data
void start_recording() {
    is_recording.store(true);
}

// Function to stop recording point cloud data
void stop_recording() {
    is_recording.store(false);
}

// Function to check if recording is active
bool is_recording_active() {
    return is_recording.load();
}

// Define Python module
PYBIND11_MODULE(livox_interface, m) {
    m.doc() = "Livox SDK Interface";
    m.def("discover_devices", &discover_devices, "Discover Livox LiDAR devices");
    m.def("start_recording", &start_recording, "Start recording point cloud data");
    m.def("stop_recording", &stop_recording, "Stop recording point cloud data");
    m.def("is_recording_active", &is_recording_active, "Check if recording is active");
}