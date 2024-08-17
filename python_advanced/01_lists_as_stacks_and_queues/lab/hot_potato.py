from collections import deque

players = deque(input().split())
wild_number = int(input()) - 1

while len(players) > 1:
    players.rotate(-wild_number)
    print(f"Removed {players.popleft()}")

print(f"Last is {players[0]}")


# from collections import deque
#
# players = deque(input().split())
# wild_number = int(input())
# counter = 1
#
# while len(players) > 1:
#     if counter == wild_number:
#         print(f"Removed {players.popleft()}")
#         counter = 1
#     else:
#         players.append(players.popleft())
#         counter += 1
#
# print(f"Last is {players[0]}")
