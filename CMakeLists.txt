cmake_minimum_required(VERSION 3.10)

project(livoxsdk2)

set(CMAKE_CXX_STANDARD 14)

# Find pybind11
find_package(pybind11 REQUIRED)

# Include directories
include_directories(src/Livox-SDK2/include)

# Source files
set(SOURCES
    src/cpp/pybind_wrapper.cpp
    src/cpp/livox_interface.cpp
)

# Create the Python module
pybind11_add_module(openpylivoxv2 ${SOURCES})

# Link libraries if needed
# target_link_libraries(openpylivoxv2 PRIVATE <your_library>)