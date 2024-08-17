from to_do_list.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, caught_pokemon: Pokemon):
        if caught_pokemon not in self.pokemons:
            self.pokemons.append(caught_pokemon)
            return f"Caught {caught_pokemon.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):

        for current_pokemon in self.pokemons:
            if current_pokemon.name == pokemon_name:
                self.pokemons.remove(current_pokemon)
                return f"You have released {pokemon_name}"

        else:
            return "Pokemon is not caught"

    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"

        for current_pokemon in self.pokemons:
            result += f"- {current_pokemon.pokemon_details()}"

        return result


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())

