def load_config(file_path):
    """Load configuration from a JSON file."""
    import json
    with open(file_path, 'r') as f:
        return json.load(f)

def save_config(file_path, config):
    """Save configuration to a JSON file."""
    import json
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

def validate_ip(ip):
    """Validate the format of an IP address."""
    import re
    pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'
    return re.match(pattern, ip) is not None

def format_point_cloud_data(data):
    """Format point cloud data for output."""
    return [{'x': point[0], 'y': point[1], 'z': point[2]} for point in data]