def recursive_drawing(num: int) -> None:
    if num == 0:
        return

    print(num * "*")

    recursive_drawing(num - 1)

    print(num * "#")


number = int(input())
recursive_drawing(number)
