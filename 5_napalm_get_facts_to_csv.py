#!/usr/bin/env python3
"""
Nornir NAPALM Demo - Cisco Live 2025
This script demonstrates how to use Nornir with NAPALM to collect device facts and export them to CSV.
It shows how Python makes it easy to process and use network data, compared to static YAML outputs.
"""

import csv
from nornir import InitNornir
from nornir_napalm.plugins.tasks import napalm_get
from nornir_utils.plugins.functions import print_result

def main():
    # Initialize Nornir with our inventory and config
    nr = InitNornir(config_file="config.yaml")

    # Run NAPALM 'get_facts' on all devices
    result = nr.run(
        task=napalm_get,
        getters=["facts"]
    )

    # Print the results in a readable format
    print_result(result)

    # Export facts to CSV
    with open("device_facts.csv", "w", newline="") as csvfile:
        fieldnames = [
            "host", "hostname", "model", "os_version", "serial_number", "uptime"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for host, multi_result in result.items():
            facts = multi_result[0].result.get("facts", {})
            writer.writerow({
                "host": host,
                "hostname": facts.get("hostname", ""),
                "model": facts.get("model", ""),
                "os_version": facts.get("os_version", ""),
                "serial_number": facts.get("serial_number", ""),
                "uptime": facts.get("uptime", "")
            })
    print("\nDevice facts exported to device_facts.csv\n")

if __name__ == "__main__":
    main() 