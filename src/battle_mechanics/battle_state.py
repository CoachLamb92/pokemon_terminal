from src.battle_mechanics.utils import choose_move, fight_introduction, valid_move_choice
from src.data import squirtle, charmander

def battle_state(player_pokemon, opponent_pokemon):
    # only one instance upon starting a fight
    fight_introduction(opponent_pokemon)

    while True:
        choose_move(player_pokemon)
        chosen_move = input()
        # valid_move_choice_check() PP vs wrong spelling
        if valid_move_choice(player_pokemon, choose_move):
            break
        # if chosen_move in player_pokemon.move_pool:
        #     if chosen_move._pp > 0:
        #         break
        #     else:
        #         f"{chosen_move} is out of PP, it cannot be used!"
            
    print(f'{player_pokemon.name} used {chosen_move}')

battle_state(charmander, squirtle)