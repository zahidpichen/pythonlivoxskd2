#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "livox_interface.h"

namespace py = pybind11;

PYBIND11_MODULE(livoxsdk2, m) {
    m.doc() = "Python wrapper for the Livox SDK";

    // Expose functions from livox_interface
    m.def("discover", &discover, "Discover LiDAR devices");
    m.def("auto_connect", &auto_connect, "Automatically connect to the first available LiDAR");
    m.def("start_lidar", &start_lidar, "Start the LiDAR");
    m.def("stop_lidar", &stop_lidar, "Stop the LiDAR");
    m.def("start_recording", &start_recording, "Start recording point cloud data");
    m.def("stop_recording", &stop_recording, "Stop recording point cloud data");
    m.def("get_point_cloud", &get_point_cloud, "Retrieve recorded point cloud data");
    m.def("is_recording_active", &is_recording_active, "Check if recording is active");
    m.def("get_recording_error", &get_recording_error, "Get the last recording error message");
    m.def("get_work_mode_error", &get_work_mode_error, "Get the last work mode error message");
}