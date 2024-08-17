for _ in range(5):              # име на променлива "_" се използва когато няма да ползваме променливата
    print("Trying to fetch data...")

num = 100_000_000 # големи числа могат да се изписват с долна черта
print(num)

# break # може да се ползва само в loop и приключва цикъла

total_sum = 0
for i in range(5):
    total_sum += 100
    print(total_sum)
    if total_sum > 222:
        print("will break the for loop")
        break

