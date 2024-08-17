def set_cover(sequence: set, sequences: list) -> str:
    result = ""
    used_sets = []

    while sequence:
        best_subset = max(sequences, key=lambda x: len(sequence.intersection(x)))
        used_sets.append(list(best_subset))
        sequence -= best_subset

    result += f"Sets to take ({len(used_sets)}):\n"
    for subset in used_sets:
        result += "{ " + f"{', '.join([str(x) for x in sorted(subset)])}" + " }\n"

    return result


universe = {int(x) for x in input().split(", ")}
number = int(input())
sets = []
for i in range(number):
    sets.append({int(x) for x in input().split(", ")})

print(set_cover(universe, sets))
