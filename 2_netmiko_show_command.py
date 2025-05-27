#!/usr/bin/env python3
"""
Nornir Netmiko Demo - Cisco Live 2025
This script demonstrates how to use Nornir with Netmiko to connect to a Cisco IOS device and run a command.
It highlights how Python code can replace YAML playbooks (like in Ansible) for more flexible automation.
"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command

def main():
    # Initialize Nornir with our inventory and config
    nr = InitNornir(config_file="config.yaml")

    # Run 'show version' on all devices using Netmiko
    # This is similar to an Ansible task, but in Python
    result = nr.run(
        task=netmiko_send_command,
        command_string="show version"
    )

    # Print the results in a readable format
    print_result(result)

if __name__ == "__main__":
    main() 