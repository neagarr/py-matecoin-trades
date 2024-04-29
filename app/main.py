import json
from decimal import Decimal


def calculate_profit(file: str) -> None:
    result = {
        "earned_money": "0",
        "matecoin_account": "0"
    }

    with open(file, "r") as file:
        trades = json.load(file)

    for contract in trades:
        if contract["bought"]:
            result["matecoin_account"] = str(
                Decimal(result["matecoin_account"]) +
                Decimal(contract["bought"])
            )
            result["earned_money"] = str(
                Decimal(result["earned_money"]) -
                Decimal(contract["bought"]) *
                Decimal(contract["matecoin_price"])
            )

        if contract["sold"]:
            result["matecoin_account"] = str(
                Decimal(result["matecoin_account"]) -
                Decimal(contract["sold"])
            )
            result["earned_money"] = str(
                Decimal(result["earned_money"]) +
                Decimal(contract["sold"]) *
                Decimal(contract["matecoin_price"])
            )

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


