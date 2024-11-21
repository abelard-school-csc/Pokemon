### README

# Pokémon Battle Simulator

## Overview

This project is a Python-based Pokémon battle simulator using the PokeAPI. It simulates a bracket-style tournament with 16 randomly chosen Pokémon. A coin flip determines the first move in each battle. The simulator retrieves Pokémon stats and moves from the API to conduct battles. Each battle's outcome depends on the stats and randomly chosen moves. 

## Features

- Random selection of 16 Pokémon.
- Bracket-style tournament (single elimination).
- Stats-based damage calculation.
- Randomized moves for attack.
- Detailed battle logs, including moves and damage for every turn.
- Declares the final champion after four rounds.

## Requirements

- Python 3.7 or higher
- `requests` library

Install the required package using:

```bash
pip install requests
```

## Usage

Run the simulator with:

```bash
python tournament.py
```

The output will display:
1. Pokémon battles in each round.
2. Moves used during each battle and their damage.
3. The tournament champion.

## API Reference

The simulator uses the [PokeAPI](https://pokeapi.co/) to fetch Pokémon stats and moves. Ensure you have a stable internet connection while running the program.

## License

This project is open-source and free to use under the MIT License.
