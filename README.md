# Nornir Demo Scripts

This repository contains a series of demo scripts showcasing Nornir's capabilities for network automation. Network device is from [Cisco DevNet Sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/IOS%20XE%20on%20Cat8kv_ios-xe-cat-8kv).

## Demo Scripts

### 1. Hello World (`1_hello_world.py`)
- Basic Nornir setup and initialization
- Simple task execution to greet hosts
- Basic host information display

### 2. Results Object (`2_results_object.py`)
- Working with Nornir's Result objects
- Task result handling and inspection
- Error handling and exception management
- Custom task result formatting

### 3. Netmiko Show Command (`3_netmiko_show_command.py`)
- Device connection using Netmiko
- Command execution on network devices
- Output processing
- Basic error handling

### 4. Task Chaining (`4_task_chaining.py`)
- Running multiple tasks in sequence
- Data passing between tasks
- Task result aggregation
- Programmatic task control

### 5. Render Config with Jinja2 (`5_render_config_jinja2.py`)
- Template-based configuration
- Jinja2 template rendering
- Configuration application
- Dynamic config generation

### 6. NAPALM Get Facts to CSV (`6_napalm_get_facts_to_csv.py`)
- Multi-vendor support with NAPALM
- Data collection and processing
- CSV output generation
- Structured data handling

### 7. Troubleshooting (`7_troubleshoot_failed_task.py`)
- Error handling and debugging
- Failed task inspection
- API integration example
- Exception handling patterns

## Key Nornir Features Demonstrated

- **Inventory Management**: YAML-based inventory with groups and variables
- **Task Execution**: Parallel and sequential task execution
- **Plugin System**: Integration with Netmiko and NAPALM
- **Template Support**: Jinja2 templating for configurations
- **Error Handling**: Comprehensive error handling and debugging
- **Data Processing**: Collection, transformation, and output
- **Multi-vendor Support**: Working with different network platforms

## Requirements

- Python 3.8+
- Nornir and its plugins (see `requirements.txt`)
- Network device access (DevNet sandbox or similar)

## Usage

Each script can be run independently:
```bash
python <script_name>.py
```

## Additional Resources

- [Nornir Documentation](https://nornir.readthedocs.io/)
- [Netmiko Documentation](https://github.com/ktbyers/netmiko)
- [NAPALM Documentation](https://napalm.readthedocs.io/) 