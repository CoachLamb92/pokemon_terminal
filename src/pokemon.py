class Pokemon:
    
    def __init__(self, name, level=1, move_pool=[None, None, None, None]):
        self.nickname = name    # Eventually create method to reassign
        self.name = name
        self.level = level
        self.move_pool = move_pool.copy()   # Generate these soon
        self.move_list = []
        for move in move_pool:
            if move == None:
                self.move_list.append("")
            else:
                self.move_list.append(move._name)

        self.nature = "" # Create a random nature generator
        self.stats = {'hitpoints': 0,
                      'attack': 0,
                      'defense': 0,
                      'special_attack': 0,
                      'special_defense': 0,
                      'speed': 0}   # Eventually populate using PokeAPI values and random
        self.experience = 0     # Very low-priority implementation
        self.gender = None # Eventually randomly generate using PokeAPI values and random
        self.non_volatile_status = None # Eventually code in Sleep, Burned, Paralysed, Poisoned and Badly Poisoned
        self.volatile_status = None # Eventually code in Confused, Infatuated, etc

    def use_move(self, move_string):
        pass
        # implement a function which takes 'move_string' argument and executes its effects

    def take_damage(self, damage_int):
        self.stats['hitpoints'] = max(self.stats['hitpoints']-damage_int, 0)

    def has_fainted(self):
        return True if self.stats['hitpoints'] == 0 else False
    
    def add_move(self, move):
        free_spaces = self.move_pool.count(None)
        if move._name in self.move_list:
            print("This move is already known!")
            return
        if free_spaces > 0:
            self.move_pool[4-free_spaces] = move
            self.move_list[4-free_spaces] = move._name
        else:
            pass
            # implement a function to replace a move

    def delete_move(self, move):
        if move._name in self.move_list:
            move_list_index = self.move_list.index(move._name)
            for i in range(move_list_index + 1, 4):
                self.move_pool[i-1] = self.move_pool[i]
                self.move_list[i-1] = self.move_list[i]
            self.move_pool[3] = None
            self.move_list[3] = ""
        else:
            pass
            # implement a print to say no move to delete

    def alter_pp(self, move):
        # simply reduces by one for now. eventually add in healing options, spite and pressure
        if move in self.move_pool and move._powerpoints > 0:
            move._powerpoints -= 1