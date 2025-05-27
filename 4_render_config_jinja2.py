#!/usr/bin/env python3
"""
Nornir Jinja2 + Netmiko Demo – Cisco Live 2025
Render and apply a loopback config using Jinja2 and Netmiko.
"""

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_netmiko.tasks import netmiko_send_config
import json

def render_and_apply_config(task):
    # Render template with loopback data
    result = task.run(
        task=template_file,
        template="loopbacks.j2",
        path="templates",
        loopbacks=task.host["loopbacks"]  # From host inventory or injected data
    )
    
    # Use the rendered config as input to Netmiko
    config_lines = result.result.splitlines()
    task.run(
        task=netmiko_send_config,
        config_commands=config_lines
    )

def main():
    nr = InitNornir(config_file="config.yaml")

    # Inject loopback data manually or from JSON
    with open("data/loopbacks.json") as f:
        loopback_data = json.load(f)

    # Attach data to each host (for simplicity, one shared payload)
    for host in nr.inventory.hosts.values():
        host["loopbacks"] = loopback_data["loopbacks"]

    # Run render + apply logic
    result = nr.run(task=render_and_apply_config)
    print_result(result)

if __name__ == "__main__":
    main()