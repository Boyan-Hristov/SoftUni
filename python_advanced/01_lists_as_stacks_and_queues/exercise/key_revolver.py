from collections import deque

bullet_price = int(input())
gun_capacity = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(y) for y in input().split()])
intelligence_value = int(input())

total_bullets = len(bullets)
bullets_used = 0
is_opened = False

while bullets:
    bullets_used += 1
    bullet = bullets.pop()
    lock = locks.popleft()
    if lock >= bullet:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)
    if bullets_used % gun_capacity == 0 and bullets:
        print("Reloading!")
    if not locks:
        is_opened = True
        break


if is_opened:
    bullets_left = total_bullets - bullets_used
    money_earned = intelligence_value - bullet_price * bullets_used
    print(f"{bullets_left} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
