#!/usr/bin/env python3
"""
Nornir Basics Demo - Cisco Live 2025
This script demonstrates the fundamental concepts of Nornir:
1. Inventory Management
2. Task Definition
3. Task Execution
4. Result Handling

Think of this as a "Hello World" for network automation, similar to a basic Ansible playbook
but using pure Python instead of YAML.
"""

from nornir import InitNornir
from nornir.core.task import Task, Result
from nornir_utils.plugins.functions import print_result
from typing import Any

def hello_network(task: Task) -> Result:
    """
    A simple task that returns a greeting for each device.
    In Nornir, tasks are just Python functions that take a Task object and return a Result.
    This is similar to an Ansible task, but written in Python instead of YAML.
    """
    return Result(
        host=task.host,
        result=f"Hello from {task.host.name}! I am a {task.host.platform} device at {task.host.hostname}"
    )

def main():
    # Initialize Nornir with our inventory
    # This is similar to Ansible's inventory, but can be in YAML, JSON, or even a database
    nr = InitNornir(
        config_file="config.yaml",
        logging={"enabled": True, "level": "INFO"}
    )

    # Run our task against all devices in the inventory
    # This is similar to running an Ansible playbook
    result = nr.run(
        task=hello_network,
        name="Greeting all network devices"
    )

    # Print the results in a nice format
    # Nornir provides built-in result formatting, similar to Ansible's output
    print_result(result)

if __name__ == "__main__":
    main()
