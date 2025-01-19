from src.moves import Move
from src.pokemon import Pokemon

types = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']

example_moves = []
tackle = Move('tackle', 6, 'normal', 100, 'physical')
water_gun = Move('water gun', 6, 'water', 100, 'special')
ember = Move('ember', 8, 'fire', 80, 'special')
gust = Move('gust', 5, 'flying', 85, 'special')

example_moves = [tackle, water_gun, ember, gust]

charmander = Pokemon('charmander', 5)
charmander.stats['hitpoints'] = 30
charmander.move_pool = [ember, None, None, None]

squirtle = Pokemon('squirtle', 5)
squirtle.stats['hitpoints'] = 34
squirtle.move_pool = [water_gun, None, None, None]

pidgey = Pokemon('pidgey', 5)
pidgey.stats['hitpoints'] = 27
pidgey.move_pool = [tackle, gust, None, None]

example_pokemon = [charmander, squirtle, pidgey]