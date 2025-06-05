#!/usr/bin/env python3
from nornir import InitNornir

def greet_host(task):
    print(f"Hello from {task.host.name}!")
    print(f"- Platform: {task.host.platform}")
    print(f"- IP Address: {task.host.hostname}")

nr = InitNornir(config_file="config.yaml")
nr.run(task=greet_host)
