def fight_introduction(pokemon):
    first_string = f"A wild {pokemon.name} appeared!"
    print(first_string)

def choose_move(pokemon):
    string = "Choose a move!"
    print(string)
    move_list = [move._name for move in pokemon.move_pool if move]
    print(', '.join(move_list))

def valid_move_choice(pokemon, move):
    if move._powerpoints > 0:
        return True
    else:
        print(f"{move._name} is out of PP, it cannot be used!")
    return False

def move_string_to_move(pokemon, move_string):
    if move_string in pokemon.move_list:
        return pokemon.move_pool[pokemon.move_list.index(move_string)]