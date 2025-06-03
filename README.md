# Python Livox SDK2

This project provides a Python wrapper around the Livox SDK, allowing users to interact with Livox LiDAR devices for various applications such as point cloud data acquisition, visualization, and processing.

## Features

- Discover and connect to Livox LiDAR devices.
- Start and stop LiDAR operations.
- Record and retrieve point cloud data.
- Support for callback functions to handle data reception and connection status changes.
- Example scripts demonstrating basic functionality and usage.

## Installation

To install the Python Livox SDK2, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd python-livoxsdk2
pip install -r requirements.txt
```

## Usage

### Basic Scanning

To perform basic scanning with the LiDAR, you can use the `basic_scan.py` example:

```bash
python examples/basic_scan.py
```

### Point Cloud Visualization

To visualize point cloud data, run the `point_cloud_viewer.py` example:

```bash
python examples/point_cloud_viewer.py
```

### Recording Point Cloud Data

To record point cloud data, use the `record_pointcloud.py` example:

```bash
python examples/record_pointcloud.py
```

## Testing

To run the tests for the project, use the following command:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.