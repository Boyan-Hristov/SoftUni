def sum_of_coins(sequence: list, amount: int) -> str:
    result = ""
    coins_taken = {}
    for coin in sorted(sequence, reverse=True):
        number_of_coins = amount // coin
        if number_of_coins:
            coins_taken[coin] = number_of_coins
        amount %= coin
        if amount == 0:
            break

    if amount == 0:
        result += f"Number of coins to take: {sum(coins_taken.values())}\n"
        for key, value in coins_taken.items():
            result += f"{value} coin(s) with value {key}\n"

        return result

    else:
        return "Error"


coins = [int(x) for x in input().split(", ")]
target = int(input())
print(sum_of_coins(coins, target))
