from nornir import InitNornir
from nornir.core.task import Result
from nornir_utils.plugins.functions import print_result

def format_site_label(task):
    try:
        site = task.host["site"]
        role = task.host["role"]
        label = f"{site.upper()}-{role.title()}"
        return Result(host=task.host, result=label)
    except Exception as e:
        return Result(host=task.host, result="Could not format label", exception=e, failed=True)

nr = InitNornir(config_file="config.yaml")
result = nr.run(task=format_site_label)

# Show nicely formatted output
print_result(result)

# Manually unpack the result for one host
print("\n--- Manual result inspection ---")
for host, multi_result in result.items():
    print(f"\nHost: {host}")
    task_result = multi_result[0]  # Nornir returns a list of task results per host
    print("  .result   →", task_result.result)
    print("  .failed   →", task_result.failed)
    print("  .exception→", task_result.exception)
    if task_result.failed:
        print("This task failed — check .exception for details")