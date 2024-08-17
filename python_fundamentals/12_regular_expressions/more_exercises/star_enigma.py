import re

messages_count = int(input())
pattern = r"\@([A-Za-z]+)([^\@\-\!\,\:\>])?\:(\d+)\2?\!([AD])\!\2?\-\>(\d+)"
attacked_planets = []
destroyed_planets = []
for message in range(messages_count):
    encrypted_message = input()
    key_letters = ["s", "t", "a", "r"]
    key_value = 0
    for letter in encrypted_message:
        if letter.lower() in key_letters:
            key_value += 1
    decrypted_message = ""
    for character in encrypted_message:
        decrypted_message += chr(ord(character) - key_value)
    match = re.search(pattern, decrypted_message)
    if match:
        planet = match.group(1)
        attacked_or_destroyed = match.group(4)
        if attacked_or_destroyed == "A":
            attacked_planets.append(planet)
        elif attacked_or_destroyed == "D":
            destroyed_planets.append(planet)

attacked_planets = list(sorted(attacked_planets, key=lambda x: x))
destroyed_planets = list(sorted(destroyed_planets, key=lambda x: x))
print(f"Attacked planets: {len(attacked_planets)}")
for attacked_planet in attacked_planets:
    print(f"-> {attacked_planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for destroyed_planet in destroyed_planets:
    print(f"-> {destroyed_planet}")


