from src.moves import Move
from src.pokemon import Pokemon

types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

example_moves = []
tackle = Move('tackle', 6, 'normal', 100)
water_gun = Move('water gun', 6, 'water', 100)
ember = Move('ember', 8, 'fire', 80)
gust = Move('gust', 5, 'flying', 85)

example_moves = [tackle, water_gun, ember, gust]

charmander = Pokemon('charmander', 5)
charmander.stats['hitpoints'] = 30
charmander.add_move(ember)

squirtle = Pokemon('squirtle', 5)
squirtle.stats['hitpoints'] = 34
squirtle.add_move(water_gun)

pidgey = Pokemon('pidgey', 5)
pidgey.stats['hitpoints'] = 27
pidgey.add_move(tackle)
pidgey.add_move(gust)

example_pokemon = [charmander, squirtle, pidgey]