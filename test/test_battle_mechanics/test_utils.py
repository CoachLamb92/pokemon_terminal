from src.battle_mechanics.utils import fight_introduction, choose_move, valid_move_choice, move_string_to_move
# from src.battle_mechanics.battle_state import battle_state
from src.data import squirtle, charmander, pidgey
from src.pokemon import Pokemon
from src.moves import Move
import io
import sys

class TestUtils:
    def test_fight_introduction_prints_correctly(self):
        # Arrange
        oppo_pkmn = squirtle
        expected = "A wild squirtle appeared!\n"
        # Act
        print_statement = io.StringIO()     # Make StringIO.
        sys.stdout = print_statement        # Redirect stdout.
        fight_introduction(oppo_pkmn)       # Call function.
        sys.stdout = sys.__stdout__         # Reset redirect.
        result = print_statement.getvalue()
        # Assert
        assert expected == result

        # Arrange
        oppo_pkmn = charmander
        expected = "A wild charmander appeared!\n"
        # Act
        print_statement = io.StringIO()     # Make StringIO.
        sys.stdout = print_statement        # Redirect stdout.
        fight_introduction(oppo_pkmn)       # Call function.
        sys.stdout = sys.__stdout__         # Reset redirect.
        result = print_statement.getvalue()
        # Assert
        assert expected == result

    def test_choose_move_prints_correctly(self):
        # Arrange
        user_pkmn = squirtle
        expected = "Choose a move!\nwater gun\n"
        # Act
        print_statement = io.StringIO()
        sys.stdout = print_statement
        choose_move(user_pkmn)
        sys.stdout = sys.__stdout__
        result = print_statement.getvalue()
        # Assert
        assert expected == result

        # Arrange
        user_pkmn = pidgey
        expected = "Choose a move!\ntackle, gust\n"
        # Act
        print_statement = io.StringIO()
        sys.stdout = print_statement
        choose_move(user_pkmn)
        sys.stdout = sys.__stdout__
        result = print_statement.getvalue()
        # Assert
        assert expected == result

    def test_move_string_to_move_returns_correctly(self):
        # Arrange
        user_pkmn = Pokemon('squirtle')
        chosen_move = 'water gun'
        water_gun = Move('water gun', 6, 'water', 100, 'special')
        user_pkmn.add_move(water_gun)
        expected = water_gun
        # Act
        result = move_string_to_move(user_pkmn, chosen_move)
        # Assert
        assert expected == result

    def test_valid_move_choice_prints_correctly(self):
        # Arrange
        user_pkmn = Pokemon('squirtle')
        water_gun = Move('water gun', 6, 'water', 100)
        chosen_move = water_gun
        expected = 'water gun is out of PP, it cannot be used!\n'
        # Act
        user_pkmn.add_move(chosen_move)
        user_pkmn.alter_pp(chosen_move)
        print_statement = io.StringIO()
        sys.stdout = print_statement
        valid_move_choice(user_pkmn, chosen_move)
        sys.stdout = sys.__stdout__
        result = print_statement.getvalue()
        # Assert
        assert expected == result

    def test_valid_move_choice_returns_correctly(self):
        # Arrange
        user_pkmn = Pokemon('squirtle')
        water_gun = Move('water gun', 6, 'water', 100)
        chosen_move = water_gun
        expected = True
        # Act
        result = valid_move_choice(user_pkmn, chosen_move)
        # Assert
        assert expected == result



