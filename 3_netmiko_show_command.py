#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command


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
