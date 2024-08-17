def distribute_wealth(population_list: list) -> list:
    for index in range(len(population_list) - 1):
        wealthiest_part = max(population_list)
        wealthiest_part_index = population_list.index(wealthiest_part)
        if population_list[index] < minimum_wealth:
            wealth_needed = minimum_wealth - population_list[index]
            wealthiest_part -= wealth_needed
            population_list[index] += wealth_needed
            population_list[wealthiest_part_index] = wealthiest_part
    return population_list


population = [int(number) for number in input().split(", ")]
minimum_wealth = int(input())
population = distribute_wealth(population)
population_after_distribution = [group for group in population if group >= minimum_wealth]
if len(population_after_distribution) != len(population):
    print("No equal distribution possible")
else:
    print(population_after_distribution)
