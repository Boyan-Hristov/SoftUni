from collections import deque

peaks = deque([
    ("Vihren", 80),
    ("Kutelo", 90),
    ("Banski Suhodol", 100),
    ("Polezhan", 60),
    ("Kamenitza", 10)
])

food_supplies = [int(x) for x in input().split(", ")]
daily_stamina = deque([int(y) for y in input().split(", ")])

peaks_climbed = []
day = 0

while peaks:
    day += 1
    energy = food_supplies.pop() + daily_stamina.popleft()
    data = peaks[0]
    peak, energy_required = data[0], int(data[1])

    if energy >= energy_required:
        peaks_climbed.append(peak)
        peaks.popleft()

    if day == 7:
        break

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if peaks_climbed:
    print(f"Conquered peaks:")
    print("\n".join(peaks_climbed))
