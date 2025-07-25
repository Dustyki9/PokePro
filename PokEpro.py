import time

from colorama import init, Fore, Style

init(autoreset=True)

pokemon_by_number = {
    1: {"name": "Bulbasaur", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
        "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    2: {"name": "Ivysaur", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
        "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    3: {"name": "Venusaur", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
        "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    4: {"name": "Charmander", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
        "Weakness": ["Water", "Ground", "Rock"]},
    5: {"name": "Charmeleon", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
        "Weakness": ["Water", "Ground", "Rock"]},
    6: {"name": "Charizard", "Type": ["Fire", "Flying"], "Strength": ["Grass", "Bug", "Steel", "Fighting"],
        "Weakness": ["Water", "Electric", "Rock"]},
    7: {"name": "Squirtle", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
        "Weakness": ["Electric", "Grass"]},
    8: {"name": "Wartortle", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
        "Weakness": ["Electric", "Grass"]},
    9: {"name": "Blastoise", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
        "Weakness": ["Electric", "Grass"]},
    10: {"name": "Caterpie", "Type": ["Bug"], "Strength": ["Grass", "Psychic"], "Weakness": ["Fire", "Flying", "Rock"]},
    11: {"name": "Metapod", "Type": ["Bug"], "Strength": ["Grass", "Psychic"], "Weakness": ["Fire", "Flying", "Rock"]},
    12: {"name": "Butterfree", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Psychic"],
         "Weakness": ["Fire", "Electric", "Ice", "Flying", "Rock"]},
    13: {"name": "Weedle", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],
         "Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    14: {"name": "Kakuna", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],
         "Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    15: {"name": "Beedrill", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],
         "Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    16: {"name": "Pidgey", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Rock"]},
    17: {"name": "Pidgeotto", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Rock"]},
    18: {"name": "Pidgeot", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Rock"]},
    19: {"name": "Rattata", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    20: {"name": "Raticate", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    21: {"name": "Spearow", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Rock"]},
    22: {"name": "Fearow", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Rock"]},
    23: {"name": "Ekans", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    24: {"name": "Arbok", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    25: {"name": "Pikachu", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    26: {"name": "Raichu", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    27: {"name": "Sandshrew", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],
         "Weakness": ["Water", "Grass", "Ice"]},
    28: {"name": "Sandslash", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],
         "Weakness": ["Water", "Grass", "Ice"]},
    29: {"name": "Nidoran Female", "Type": ["Poison"], "Strength": ["Grass", "Fairy"],
         "Weakness": ["Ground", "Psychic"]},
    30: {"name": "Nidorina", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    31: {"name": "Nidoqueen", "Type": ["Poison", "Ground"],
         "Strength": ["Grass", "Electric", "Poison", "Rock", "Steel"],
         "Weakness": ["Water", "Ice", "Ground", "Psychic"]},
    32: {"name": "Nidoran Male", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    33: {"name": "Nidorino", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    34: {"name": "Nidoking", "Type": ["Poison", "Ground"], "Strength": ["Grass", "Electric", "Poison", "Rock", "Steel"],
         "Weakness": ["Water", "Ice", "Ground", "Psychic"]},
    35: {"name": "Clefairy", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    36: {"name": "Clefable", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    37: {"name": "Vulpix", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
         "Weakness": ["Water", "Ground", "Rock"]},
    38: {"name": "Ninetales", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
         "Weakness": ["Water", "Ground", "Rock"]},
    39: {"name": "Jigglypuff", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    40: {"name": "Wigglytuff", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    41: {"name": "Zubat", "Type": ["Poison", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Psychic", "Rock"]},
    42: {"name": "Golbat", "Type": ["Poison", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Psychic", "Rock"]},
    43: {"name": "Oddish", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
         "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    44: {"name": "Gloom", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
         "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    45: {"name": "Vileplume", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
         "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    46: {"name": "Paras", "Type": ["Bug", "Grass"], "Strength": ["Grass", "Psychic", "Water", "Ground", "Rock"],
         "Weakness": ["Fire", "Flying", "Poison", "Bug", "Ice"]},
    47: {"name": "Parasect", "Type": ["Bug", "Grass"], "Strength": ["Grass", "Psychic", "Water", "Ground", "Rock"],
         "Weakness": ["Fire", "Flying", "Poison", "Bug", "Ice"]},
    48: {"name": "Venonat", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],
         "Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    49: {"name": "Venomoth", "Type": ["Bug", "Poison"], "Strength": ["Grass", "Psychic"],
         "Weakness": ["Fire", "Flying", "Rock", "Psychic"]},
    50: {"name": "Diglett", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],
         "Weakness": ["Water", "Grass", "Ice"]},
    51: {"name": "Dugtrio", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],
         "Weakness": ["Water", "Grass", "Ice"]},
    52: {"name": "Meowth", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    53: {"name": "Persian", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    54: {"name": "Psyduck", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
         "Weakness": ["Electric", "Grass"]},
    55: {"name": "Golduck", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
         "Weakness": ["Electric", "Grass"]},
    56: {"name": "Mankey", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],
         "Weakness": ["Flying", "Psychic"]},
    57: {"name": "Primeape", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],
         "Weakness": ["Flying", "Psychic"]},
    58: {"name": "Growlithe", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
         "Weakness": ["Water", "Ground", "Rock"]},
    59: {"name": "Arcanine", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
         "Weakness": ["Water", "Ground", "Rock"]},
    60: {"name": "Poliwag", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
         "Weakness": ["Electric", "Grass"]},
    61: {"name": "Poliwhirl", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
         "Weakness": ["Electric", "Grass"]},
    62: {"name": "Poliwrath", "Type": ["Water", "Fighting"],
         "Strength": ["Fire", "Ground", "Rock", "Normal", "Ice", "Rock", "Dark", "Steel"],
         "Weakness": ["Electric", "Grass", "Flying", "Psychic"]},
    63: {"name": "Abra", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"], "Weakness": ["Bug", "Ghost", "Dark"]},
    64: {"name": "Kadabra", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],
         "Weakness": ["Bug", "Ghost", "Dark"]},
    65: {"name": "Alakazam", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],
         "Weakness": ["Bug", "Ghost", "Dark"]},
    66: {"name": "Machop", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],
         "Weakness": ["Flying", "Psychic"]},
    67: {"name": "Machoke", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],
         "Weakness": ["Flying", "Psychic"]},
    68: {"name": "Machamp", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],
         "Weakness": ["Flying", "Psychic"]},
    69: {"name": "Bellsprout", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
         "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    70: {"name": "Weepinbell", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
         "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    71: {"name": "Victreebel", "Type": ["Grass", "Poison"], "Strength": ["Water", "Ground", "Rock"],
         "Weakness": ["Fire", "Ice", "Flying", "Psychic"]},
    72: {"name": "Tentacool", "Type": ["Water", "Poison"], "Strength": ["Fire", "Ground", "Rock", "Grass", "Fairy"],
         "Weakness": ["Electric", "Psychic", "Ground"]},
    73: {"name": "Tentacruel", "Type": ["Water", "Poison"], "Strength": ["Fire", "Ground", "Rock", "Grass", "Fairy"],
         "Weakness": ["Electric", "Psychic", "Ground"]},
    74: {"name": "Geodude", "Type": ["Rock", "Ground"],
         "Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],
         "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    75: {"name": "Graveler", "Type": ["Rock", "Ground"],
         "Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],
         "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    76: {"name": "Golem", "Type": ["Rock", "Ground"],
         "Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],
         "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    77: {"name": "Ponyta", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
         "Weakness": ["Water", "Ground", "Rock"]},
    78: {"name": "Rapidash", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
         "Weakness": ["Water", "Ground", "Rock"]},
    79: {"name": "Slowpoke", "Type": ["Water", "Psychic"], "Strength": ["Fire", "Ground", "Rock", "Fighting", "Poison"],
         "Weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]},
    80: {"name": "Slowbro", "Type": ["Water", "Psychic"], "Strength": ["Fire", "Ground", "Rock", "Fighting", "Poison"],
         "Weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]},
    81: {"name": "Magnemite", "Type": ["Electric", "Steel"], "Strength": ["Water", "Flying", "Ice", "Rock"],
         "Weakness": ["Fire", "Fighting", "Ground"]},
    82: {"name": "Magneton", "Type": ["Electric", "Steel"], "Strength": ["Water", "Flying", "Ice", "Rock"],
         "Weakness": ["Fire", "Fighting", "Ground"]},
    83: {"name": "Farfetch'd", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Rock"]},
    84: {"name": "Doduo", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Rock"]},
    85: {"name": "Dodrio", "Type": ["Normal", "Flying"], "Strength": ["Grass", "Fighting", "Bug"],
         "Weakness": ["Electric", "Ice", "Rock"]},
    86: {"name": "Seel", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"], "Weakness": ["Electric", "Grass"]},
    87: {"name": "Dewgong", "Type": ["Water", "Ice"],
         "Strength": ["Fire", "Ground", "Rock", "Grass", "Flying", "Dragon"],
         "Weakness": ["Electric", "Grass", "Fighting", "Rock"]},
    88: {"name": "Grimer", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    89: {"name": "Muk", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    90: {"name": "Shellder", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
         "Weakness": ["Electric", "Grass"]},
    91: {"name": "Cloyster", "Type": ["Water", "Ice"],
         "Strength": ["Fire", "Ground", "Rock", "Grass", "Flying", "Dragon"],
         "Weakness": ["Electric", "Grass", "Fighting", "Rock"]},
    92: {"name": "Gastly", "Type": ["Ghost", "Poison"], "Strength": ["Psychic", "Ghost", "Grass", "Fairy"],
         "Weakness": ["Ghost", "Psychic", "Ground"]},
    93: {"name": "Haunter", "Type": ["Ghost", "Poison"], "Strength": ["Psychic", "Ghost", "Grass", "Fairy"],
         "Weakness": ["Ghost", "Psychic", "Ground"]},
    94: {"name": "Gengar", "Type": ["Ghost", "Poison"], "Strength": ["Psychic", "Ghost", "Grass", "Fairy"],
         "Weakness": ["Ghost", "Psychic", "Ground"]},
    95: {"name": "Onix", "Type": ["Rock", "Ground"],
         "Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],
         "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    96: {"name": "Drowzee", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],
         "Weakness": ["Bug", "Ghost", "Dark"]},
    97: {"name": "Hypno", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],
         "Weakness": ["Bug", "Ghost", "Dark"]},
    98: {"name": "Krabby", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
         "Weakness": ["Electric", "Grass"]},
    99: {"name": "Kingler", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
         "Weakness": ["Electric", "Grass"]},
    100: {"name": "Voltorb", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    101: {"name": "Electrode", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    102: {"name": "Exeggcute", "Type": ["Grass", "Psychic"],
          "Strength": ["Water", "Ground", "Rock", "Fighting", "Poison"],
          "Weakness": ["Fire", "Ice", "Flying", "Bug", "Ghost", "Dark"]},
    103: {"name": "Exeggutor", "Type": ["Grass", "Psychic"],
          "Strength": ["Water", "Ground", "Rock", "Fighting", "Poison"],
          "Weakness": ["Fire", "Ice", "Flying", "Bug", "Ghost", "Dark"]},
    104: {"name": "Cubone", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],
          "Weakness": ["Water", "Grass", "Ice"]},
    105: {"name": "Marowak", "Type": ["Ground"], "Strength": ["Fire", "Electric", "Poison", "Rock", "Steel"],
          "Weakness": ["Water", "Grass", "Ice"]},
    106: {"name": "Hitmonlee", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],
          "Weakness": ["Flying", "Psychic"]},
    107: {"name": "Hitmonchan", "Type": ["Fighting"], "Strength": ["Normal", "Ice", "Rock", "Dark", "Steel"],
          "Weakness": ["Flying", "Psychic"]},
    108: {"name": "Lickitung", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    109: {"name": "Koffing", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    110: {"name": "Weezing", "Type": ["Poison"], "Strength": ["Grass", "Fairy"], "Weakness": ["Ground", "Psychic"]},
    111: {"name": "Rhyhorn", "Type": ["Ground", "Rock"],
          "Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],
          "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    112: {"name": "Rhydon", "Type": ["Ground", "Rock"],
          "Strength": ["Fire", "Electric", "Poison", "Flying", "Fire", "Ice", "Rock", "Steel"],
          "Weakness": ["Water", "Grass", "Fighting", "Ground", "Steel"]},
    113: {"name": "Chansey", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    114: {"name": "Tangela", "Type": ["Grass"], "Strength": ["Water", "Ground", "Rock"],
          "Weakness": ["Fire", "Ice", "Poison", "Flying", "Bug"]},
    115: {"name": "Kangaskhan", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    116: {"name": "Horsea", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass"]},
    117: {"name": "Seadra", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass"]},
    118: {"name": "Goldeen", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass"]},
    119: {"name": "Seaking", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass"]},
    120: {"name": "Staryu", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass"]},
    121: {"name": "Starmie", "Type": ["Water", "Psychic"], "Strength": ["Fire", "Ground", "Rock", "Fighting", "Poison"],
          "Weakness": ["Electric", "Grass", "Bug", "Ghost", "Dark"]},
    122: {"name": "Mr. Mime", "Type": ["Psychic", "Fairy"],
          "Strength": ["Fighting", "Poison", "Dragon", "Dark", "Fighting"], "Weakness": ["Poison", "Ghost", "Steel"]},
    123: {"name": "Scyther", "Type": ["Bug", "Flying"], "Strength": ["Grass", "Psychic", "Fighting", "Bug"],
          "Weakness": ["Fire", "Electric", "Ice", "Flying", "Rock"]},
    124: {"name": "Jynx", "Type": ["Ice", "Psychic"],
          "Strength": ["Grass", "Ground", "Flying", "Dragon", "Fighting", "Poison"],
          "Weakness": ["Fire", "Rock", "Bug", "Ghost", "Dark", "Steel"]},
    125: {"name": "Electabuzz", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    126: {"name": "Magmar", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
          "Weakness": ["Water", "Ground", "Rock"]},
    127: {"name": "Pinsir", "Type": ["Bug"], "Strength": ["Grass", "Psychic"], "Weakness": ["Fire", "Flying", "Rock"]},
    128: {"name": "Tauros", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    129: {"name": "Magikarp", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass"]},
    130: {"name": "Gyarados", "Type": ["Water", "Flying"],
          "Strength": ["Fire", "Ground", "Rock", "Grass", "Fighting", "Bug"], "Weakness": ["Electric", "Rock"]},
    131: {"name": "Lapras", "Type": ["Water", "Ice"],
          "Strength": ["Fire", "Ground", "Rock", "Grass", "Flying", "Dragon"],
          "Weakness": ["Electric", "Grass", "Fighting", "Rock"]},
    132: {"name": "Ditto", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    133: {"name": "Eevee", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    134: {"name": "Vaporeon", "Type": ["Water"], "Strength": ["Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass"]},
    135: {"name": "Jolteon", "Type": ["Electric"], "Strength": ["Water", "Flying"], "Weakness": ["Ground"]},
    136: {"name": "Flareon", "Type": ["Fire"], "Strength": ["Grass", "Ice", "Bug", "Steel"],
          "Weakness": ["Water", "Ground", "Rock"]},
    137: {"name": "Porygon", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    138: {"name": "Omanyte", "Type": ["Rock", "Water"],
          "Strength": ["Fire", "Ice", "Flying", "Bug", "Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    139: {"name": "Omastar", "Type": ["Rock", "Water"],
          "Strength": ["Fire", "Ice", "Flying", "Bug", "Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    140: {"name": "Kabuto", "Type": ["Rock", "Water"],
          "Strength": ["Fire", "Ice", "Flying", "Bug", "Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    141: {"name": "Kabutops", "Type": ["Rock", "Water"],
          "Strength": ["Fire", "Ice", "Flying", "Bug", "Fire", "Ground", "Rock"],
          "Weakness": ["Electric", "Grass", "Fighting", "Ground"]},
    142: {"name": "Aerodactyl", "Type": ["Rock", "Flying"],
          "Strength": ["Fire", "Ice", "Flying", "Bug", "Grass", "Fighting"],
          "Weakness": ["Water", "Electric", "Ice", "Rock", "Steel"]},
    143: {"name": "Snorlax", "Type": ["Normal"], "Strength": [], "Weakness": ["Fighting"]},
    144: {"name": "Articuno", "Type": ["Ice", "Flying"], "Strength": ["Grass", "Ground", "Flying", "Dragon"],
          "Weakness": ["Fire", "Electric", "Rock", "Steel"]},
    145: {"name": "Zapdos", "Type": ["Electric", "Flying"], "Strength": ["Water", "Flying", "Grass", "Fighting", "Bug"],
          "Weakness": ["Ice", "Rock"]},
    146: {"name": "Moltres", "Type": ["Fire", "Flying"], "Strength": ["Grass", "Bug", "Steel", "Fighting"],
          "Weakness": ["Water", "Electric", "Rock"]},
    147: {"name": "Dratini", "Type": ["Dragon"], "Strength": ["Dragon"], "Weakness": ["Ice", "Dragon"]},
    148: {"name": "Dragonair", "Type": ["Dragon"], "Strength": ["Dragon"], "Weakness": ["Ice", "Dragon"]},
    149: {"name": "Dragonite", "Type": ["Dragon", "Flying"], "Strength": ["Dragon", "Grass", "Fighting", "Bug"],
          "Weakness": ["Ice", "Rock", "Dragon", "Fairy"]},
    150: {"name": "Mewtwo", "Type": ["Psychic"], "Strength": ["Fighting", "Poison"],
          "Weakness": ["Bug", "Ghost", "Dark"]},
}

pokemon_by_name = {info["name"].lower(): number for number, info in pokemon_by_number.items()}

def type_out(text, color=Fore.WHITE, delay=0.02):
    for char in text:
        print(f"{color}{char}", end="", flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)


def print_pokemon_info(number):
    pokemon = pokemon_by_number[number]
    print(Fore.CYAN + f"\n#{number} - {pokemon['name']}")
    print(Fore.GREEN + f"  Type: {', '.join(pokemon['Type'])}")
    print(Fore.BLUE + f"  Strengths: {', '.join(pokemon['Strength']) or 'None'}")
    print(Fore.RED + f"  Weaknesses: {', '.join(pokemon['Weakness']) or 'None'}\n")

def list_all_pokemon(pokedex):
    print(Fore.CYAN + "\n--- Pokédex Entries ---")
    for number in sorted(pokedex.keys()):
        name = pokedex[number]["name"]
        print(Fore.YELLOW + f"#{number:03d} - {name}")
    print()

def blinking_dots(message="Loading", cycles=3, delay=0.4):
    for _ in range(cycles):
        for dots in ['.', '..', '...']:
            print(f"\r{Fore.GREEN}{message}{dots}   ", end='', flush=True)
            time.sleep(delay)
    print("\r" + " " * (len(message) + 5), end='\r')

def main():
    history = []

    blinking_dots("Booting PokEpro V2")
    time.sleep(2)

    blinking_dots("Loading Pokédex system")
    time.sleep(1.5)

    blinking_dots("Initializing data modules")
    time.sleep(2)

    type_out("Welcome to PokEpro!\n", Fore.BLUE)
    type_out("Type a Pokémon name or Pokédex number to look it up.", Fore.MAGENTA)
    type_out("Commands: 'list' to show all Pokémon, 'undo' to go back, 'quit' to exit.\n", Fore.MAGENTA)

    while True:
        user_input = input(Fore.WHITE + "Enter Pokémon name or number (or command): ").strip().lower()

        if user_input in ["quit", "exit"]:
            print(Fore.CYAN + "Thanks for using PokEpro! Goodbye!")
            break

        if user_input == "undo":
            if len(history) >= 2:
                history.pop()  #remove lookup
                previous = history[-1]
                print(Fore.YELLOW + "🔄 Undoing. Showing previous Pokémon:")
                print_pokemon_info(previous)
            else:
                print(Fore.RED + "❌ Nothing to undo.")
            continue

        if user_input == "list":
            list_all_pokemon(pokemon_by_number)
            continue

        # what if number
        if user_input.isdigit():
            number = int(user_input)
            if number in pokemon_by_number:
                print_pokemon_info(number)
                history.append(number)
            else:
                print(Fore.RED + "❌ ERROR: Unknown Pokédex number.")
        else:
            # Try exact name
            if user_input in pokemon_by_name:
                number = pokemon_by_name[user_input]
                print_pokemon_info(number)
                history.append(number)
            else:
                # Try partial/fuzzy
                matches = search_pokemon_by_partial_name(user_input)
                if len(matches) == 0:
                    print(Fore.RED + "❌ ERROR: Unknown Pokémon name.")
                elif len(matches) == 1:
                    number = pokemon_by_name[matches[0]]
                    print_pokemon_info(number)
                    history.append(number)
                else:
                    print(Fore.YELLOW + "Multiple Pokémon found matching your input:")
                    for i, name in enumerate(matches, 1):
                        print(f"{i}. {pokemon_by_number[pokemon_by_name[name]]['name']}")
                    try:
                        choice = int(input("Enter number of the Pokémon to select (or 0 to cancel): "))
                        if choice == 0:
                            print("Cancelled selection.")
                            continue
                        selected_name = matches[choice - 1]
                        number = pokemon_by_name[selected_name]
                        print_pokemon_info(number)
                        history.append(number)
                    except (ValueError, IndexError):
                        print(Fore.RED + "Invalid selection. Please try again.")

        cont = input("Lookup another? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            print(Fore.CYAN + "Thanks for using PokEpro! Goodbye!")
            break

if __name__ == "__main__":
    main()
