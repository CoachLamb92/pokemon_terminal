from src.battle_mechanics.utils import fight_introduction, choose_move, valid_move_choice
# from src.battle_mechanics.battle_state import battle_state
from src.data import squirtle, charmander, pidgey, example_moves
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

    def test_valid_move_choice_prints_correctly(self):
        # Arrange
        user_pkmn = squirtle
        chosen_move = 'water gun'
        expected = 'water gun is out of PP, it cannot be used!'
        # Act
        for move in example_moves:
            if move._name == chosen_move:
                move._powerpoints = 0
        # print(user_pkmn.move_pool[0]._powerpoints)
        # user_pkmn.move_pool[0]._powerpoints = 0
        # print(user_pkmn.move_pool[0]._powerpoints)
        # print_statement = io.StringIO()
        # sys.stdout = print_statement
        print(move._powerpoints)
        valid_move_choice(user_pkmn, chosen_move)
        # sys.stdout = sys.__stdout__
        # result = print_statement.getvalue()
        # Assert
        assert expected == result

    # def test_valid_move_choice_returns_correctly(self):
    #     assert False