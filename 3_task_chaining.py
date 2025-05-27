#!/usr/bin/env python3

from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config


def show_hostname(task):
    result = task.run(
        name="Get Hostname",
        task=netmiko_send_command,
        command_string="show run | include hostname"
    )
    # Extract last word from command output, e.g., 'hostname R1' → 'R1'
    hostname = result[0].result.strip().split()[-1]
    task.host["hostname_from_device"] = hostname
    return result


def set_loopback_description(task):
    hostname = task.host.get("hostname_from_device", "unknown")
    return task.run(
        name="Set Loopback Description",
        task=netmiko_send_config,
        config_commands=[
            "interface Loopback100",
            f"description Host: {hostname}"
        ]
    )


def config_chain(task):
    task.run(task=show_hostname)
    task.run(task=set_loopback_description)
    return None  # Optionally return a summary result if needed


def main():
    nr = InitNornir(config_file="config.yaml")
    result = nr.run(task=config_chain)
    print_result(result)


if __name__ == "__main__":
    main()