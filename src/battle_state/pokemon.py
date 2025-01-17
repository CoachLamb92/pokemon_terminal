class Pokemon:
    
    def __init__(self, name, level=1):
        self.nickname = name    # Eventually create method to reassign
        self.name = name
        self.level = level
        self.nature = "" # Create a random nature generator
        self.stats = {'hitpoints': 0,
                      'attack': 0,
                      'defense': 0,
                      'special_attack': 0,
                      'special_defense': 0,
                      'speed': 0}   # Eventually populate using PokeAPI values and random
        self.experience = 0
        self.gender = None # Eventually randomly generate using PokeAPI values and random
        self.non_volatile_status = None # Eventually code in Sleep, Burned, Paralysed, Poisoned and Badly Poisoned
        self.volatile_status = None # Eventually code in Confused, Infatuated, etc