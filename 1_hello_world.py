#!/usr/bin/env python3
from nornir import InitNornir

def greet_host(task):
    print(f"Hello from {task.host.name}!")
    print(f"- Platform: {task.host.platform}")
    print(f"- IP Address: {task.host.hostname}")
    
    # Show loopback config if available
    loopbacks = task.host.get("loopbacks", [])
    if loopbacks:
        print("- Loopbacks:")
        for lb in loopbacks:
            print(f"  - Loopback{lb['number']} → {lb['ip']} {lb['mask']}")
    else:
        print("- No loopbacks defined.")

nr = InitNornir(config_file="config.yaml")
nr.run(task=greet_host)
