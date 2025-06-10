#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_jinja2.plugins.tasks import template_file
from nornir_netmiko.tasks import netmiko_send_config

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


nr = InitNornir(config_file="config.yaml")
nr = nr.filter(platform="ios")
# Run render + apply logic
result = nr.run(task=render_and_apply_config)
print_result(result)

