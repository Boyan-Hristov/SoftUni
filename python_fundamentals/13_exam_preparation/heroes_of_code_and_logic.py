heroes = {}
max_hit_points = 100
max_mana_points = 200
number_of_heroes = int(input())
for current_hero in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {"hit points": int(hit_points), "mana points": int(mana_points)}

command = input()
while not command == "End":
    tokens = command.split(" - ")
    action = tokens[0]
    if action == "CastSpell":
        hero = tokens[1]
        mana_needed = int(tokens[2])
        spell_name = tokens[3]
        if heroes[hero]["mana points"] >= mana_needed:
            heroes[hero]["mana points"] -= mana_needed
            print(f"{hero} has successfully cast {spell_name} and now has {heroes[hero]['mana points']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero = tokens[1]
        damage = int(tokens[2])
        attacker = tokens[3]
        heroes[hero]["hit points"] -= damage
        if heroes[hero]["hit points"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hit points']} HP left!")
        else:
            heroes.pop(hero)
            print(f"{hero} has been killed by {attacker}!")
    elif action == "Recharge":
        hero = tokens[1]
        amount = int(tokens[2])
        new_mana_points = min(max_mana_points, heroes[hero]["mana points"] + amount)
        mana_points_recharged = new_mana_points - heroes[hero]["mana points"]
        heroes[hero]["mana points"] = new_mana_points
        print(f"{hero} recharged for {mana_points_recharged} MP!")
    elif action == "Heal":
        hero = tokens[1]
        amount = int(tokens[2])
        new_hit_points = min(max_hit_points, heroes[hero]["hit points"] + amount)
        hit_points_healed = new_hit_points - heroes[hero]["hit points"]
        heroes[hero]["hit points"] = new_hit_points
        print(f"{hero} healed for {hit_points_healed} HP!")
    command = input()

for hero_alive, attributes in heroes.items():
    print(hero_alive)
    print(f"  HP: {attributes['hit points']}")
    print(f"  MP: {attributes['mana points']}")
