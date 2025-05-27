from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

# Run a command that will cause an error on the device
result = nr.run(
    task=netmiko_send_command,
    command_string="show notarealcommand"
)

# Inspect results
for host, multi_result in result.items():
    task_result = multi_result[0]  # Nornir tasks always return a list per host
    print(f"\n{host}:")

    if task_result.failed:
        print("[!] Task FAILED")
        print("Exception:", task_result.exception)
        print("Output:", task_result.result)
    else:
        print("[✓] Task SUCCEEDED")
        print("Output:", task_result.result)