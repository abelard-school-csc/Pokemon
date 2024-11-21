import requests
import random


class Pokemon:
    def __init__(self, name):
        self.name = name
        self.stats = self.get_stats()
        self.hp = self.stats["hp"]
        self.moves = self.get_moves()

    def get_stats(self):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        data = response.json()
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
        return stats

    def get_moves(self):
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}")
        data = response.json()
        moves = [move["move"]["name"] for move in data["moves"]]
        return moves[:4] if len(moves) >= 4 else moves

    def attack(self, move, opponent):
        power = random.randint(30, 70)
        damage = power * (self.stats["attack"] / opponent.stats["defense"])
        opponent.hp -= damage
        return damage


class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def fight(self):
        first, second = (self.pokemon1, self.pokemon2) if random.choice([True, False]) else (self.pokemon2, self.pokemon1)
        print("=" * 40)
        print(f"Battle: {first.name} vs {second.name}")
        print("=" * 40)
        while self.pokemon1.hp > 0 and self.pokemon2.hp > 0:
            for attacker, defender in [(first, second), (second, first)]:
                if defender.hp <= 0:
                    break
                move = random.choice(attacker.moves)
                damage = attacker.attack(move, defender)
                print(f"{attacker.name} used {move}! {damage:.2f} damage to {defender.name}")
        winner = self.pokemon1 if self.pokemon1.hp > 0 else self.pokemon2
        print(f"{winner.name} wins the battle!")
        return winner


class Tournament:
    def __init__(self):
        self.pokemon_names = self.get_random_pokemon()
        self.pokemon = [Pokemon(name) for name in self.pokemon_names]
        self.bracket = []

    def get_random_pokemon(self):
        response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000")
        data = response.json()
        return random.sample([pokemon["name"] for pokemon in data["results"]], 16)

    def generate_bracket(self, round_number):
        print("\n" + "-" * 10 + f" ROUND {round_number} " + "-" * 10)
        pairs = [
            f"{self.pokemon[i].name} vs {self.pokemon[i + 1].name}"
            for i in range(0, len(self.pokemon), 2)
        ]
        for match in pairs:
            print(f"  {match}")

    def visualize_tree(self, winners):
        layers = []
        while len(winners) > 1:
            layers.append(winners)
            winners = [winners[i] for i in range(0, len(winners), 2)]
        layers.append(winners)

        max_width = len(layers[0]) * 8
        for i, layer in enumerate(layers[::-1]):
            spacing = " " * ((max_width // (len(layer) + 1)) - 4)
            print(spacing.join(layer).center(max_width))
            if i < len(layers) - 1:
                lines = " " * ((max_width // (len(layer) + 1)) - 4)
                lines = (lines + "|") * len(layer)
                print(lines.center(max_width))

    def start(self):
        round_number = 1
        while len(self.pokemon) > 1:
            self.generate_bracket(round_number)
            next_round = []
            for i in range(0, len(self.pokemon), 2):
                battle = Battle(self.pokemon[i], self.pokemon[i + 1])
                winner = battle.fight()
                next_round.append(winner.name)
            self.bracket.append(next_round)
            self.pokemon = [Pokemon(name) for name in next_round]
            round_number += 1

        print(f"\nTournament Champion: {self.pokemon[0].name}")
        print("\n--- TOURNAMENT BRACKET ---")
        self.visualize_tree(self.bracket[0])


if __name__ == "__main__":
    tournament = Tournament()
    tournament.start()
