from nornir import InitNornir
from nornir.core.task import Task, Result
import requests

def fetch_card_info(task: Task) -> Result:
    card_name = task.host.get("mtg_card", "Black Lotus")  # fallback if not defined

    try:
        response = requests.get(
            "https://api.scryfall.com/cards/named",
            params={"exact": card_name},
            headers={"User-Agent": "NornirDemo/1.0", "Accept": "application/json"}
        )
        response.raise_for_status()
        card_data = response.json()
        return Result(host=task.host, result=f"Found card: {card_data['flavor_text']}")
    except requests.exceptions.RequestException as e:
        return Result(host=task.host, 
                      result=f"API request failed for card: {card_name}",
                      failed=True, 
                      exception=e
                    )

nr = InitNornir(config_file="config.yaml")
result = nr.run(task=fetch_card_info)

print("\n--- MTG API Result Demo ---")
for host, multi_result in result.items():
    r = multi_result[0]
    print(f"\nHost: {host}")
    print(f"  .result  (Card Flavor Text) → {r.result}")
    print(f"  .failed   → {r.failed}")
    print(f"  .exception→ {r.exception}")