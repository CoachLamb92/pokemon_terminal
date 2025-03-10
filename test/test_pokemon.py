from src.pokemon import Pokemon
from src.moves import Move
from src.data import tackle
import io
import sys

class TestPokemonAttributes:
    def test_pokemon_nickname_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('ivysaur')
        expected = 'nickname'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_pokemon_nickname_attribute_returns_nickname(self):
        # Arrange
        dummy_pokemon = Pokemon('charmeleon')
        expected = 'charmeleon'
        # Act
        result = dummy_pokemon.nickname
        # Assert
        assert expected == result

    def test_pokemon_name_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('eevee')
        expected = 'name'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_pokemon_name_attribute_returns_name(self):
        # Arrange
        dummy_pokemon = Pokemon('pikachu')
        expected = 'pikachu'
        # Act
        result = dummy_pokemon.name
        # Assert
        assert expected == result

    def test_pokemon_level_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('squirtle')
        expected = 'level'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_pokemon_level_attribute_returns_level(self):
        # Arrange
        dummy_pokemon = Pokemon('charmander')
        expected = 1
        # Act
        result = dummy_pokemon.level
        # Assert
        assert expected == result

        # Arrange
        dummy_pokemon = Pokemon('bulbasaur', 5)
        expected = 5
        # Act
        result = dummy_pokemon.level
        # Assert
        assert expected == result

    def test_pokemon_move_pool_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('raticate')
        expected = 'move_pool'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result
    
    def test_pokemon_move_pool_attribute_returns_move_pool(self):
        # Arrange
        dummy_pokemon = Pokemon('spearow', move_pool=[tackle, None, None, None])
        expected = [tackle, None, None, None]
        # Act
        result = dummy_pokemon.move_pool
        # Assert
        assert expected == result

        # Arrange
        dummy_pokemon = Pokemon('vulpix')
        expected = [tackle, None, None, None]
        # Act
        dummy_pokemon.add_move(tackle)
        result = dummy_pokemon.move_pool
        # Assert
        assert expected == result
    
    def test_pokemon_nature_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('wartortle')
        expected = 'nature'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result
    """
    Uncomment when natures is implemented
    def test_pokemon_nature_attribute_returns_nature(self):
        # Arrange
        dummy_pokemon = Pokemon('charizard')
        expected = ''
        # Act
        result = dummy_pokemon.nature
        # Assert
        assert expected == result
    """
    def test_pokemon_stats_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('venusaur')
        expected = 'stats'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result
    """
    Uncomment when stats are implemented
    def test_pokemon_stats_attribute_returns_stats(self):
        # Arrange
        dummy_pokemon = Pokemon('blastoise')
        expected = 'charmeleon'
        # Act
        result = dummy_pokemon.stats
        # Assert
        assert expected == result
    """
    def test_pokemon_experience_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('caterpie')
        expected = 'experience'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_pokemon_experience_attribute_returns_experience(self):
        # Arrange
        dummy_pokemon = Pokemon('metapod')
        expected = 0
        # Act
        result = dummy_pokemon.experience
        # Assert
        assert expected == result

    def test_pokemon_gender_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('butterfree')
        expected = 'gender'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result
    """
    def test_pokemon_gender_attribute_returns_gender(self):
        Uncomment when gender is implemented
        # Arrange
        dummy_pokemon = Pokemon('tauros')
        expected = 'male'
        # Act
        result = dummy_pokemon.gender
        # Assert
        assert expected == result

        Uncomment when gender is implemented
        # Arrange
        dummy_pokemon = Pokemon('chansey')
        expected = 'female'
        # Act
        result = dummy_pokemon.gender
        # Assert
        assert expected == result

        Uncomment when gender is implemented
        # Arrange
        dummy_pokemon = Pokemon('magnemite')
        expected = 'n/a'
        # Act
        result = dummy_pokemon.gender
        # Assert
        assert expected == result

        Uncomment when gender is implemented
        # Arrange
        dummy_pokemon = Pokemon('weedle')
        expected = ['male', 'female']
        # Act
        result = dummy_pokemon.gender
        # Assert
        assert result in expected
    """
    def test_pokemon_non_volatile_status_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('kakuna')
        expected = 'non_volatile_status'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result
    """
    def test_pokemon_non_volatile_status_attribute_returns_non_volatile_status(self):
        Uncomment when non_volatile_status is implemented
        # Arrange
        dummy_pokemon = Pokemon('beedrill')
        expected = ''
        # Act
        result = dummy_pokemon.non_volatile_status
        # Assert
        assert expected == result
    """
    def test_pokemon_volatile_status_attribute_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('pidgey')
        expected = 'volatile_status'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result
    """
    def test_pokemon_volatile_status_attribute_returns_volatile_status(self):
        Uncomment when volatile_status is implemented
        # Arrange
        dummy_pokemon = Pokemon('pidgeotto')
        expected = ''
        # Act
        result = dummy_pokemon.volatile_status
        # Assert
        assert expected == result
    """
    def test_move_list_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('nidoking')
        expected = 'move_list'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_move_list_returns_correctly(self):
        # Arrange
        dummy_pokemon = Pokemon('clefairy', move_pool=[tackle, None, None, None])
        expected = 'tackle'
        # Act
        result = dummy_pokemon.move_list[0]
        # Assert
        assert expected == result

        # Arrange
        dummy_pokemon = Pokemon('clefable')
        expected = 'tackle'
        # Act
        dummy_pokemon.add_move(tackle)
        result = dummy_pokemon.move_list[0]
        # Assert
        assert expected == result

class TestPokemonMethods:
    def test_use_move_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('pidgeot')
        expected = 'use_move'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result
    """
    # Uncomment when use_move can be tested properly
    def test_use_move_executes_correctly(self):
        # Arrange
        dummy_pokemon = Pokemon('rattata')
        input_move = ''
        expected = ''
        # Act
        result = dummy_pokemon.use_move(input_move)
        # Assert
        assert expected == result
    """
    def test_take_damage_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('fearow')
        expected = 'take_damage'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_take_damage_reduces_health_correctly(self):
        # Arrange
        dummy_pokemon = Pokemon('ekans')
        input_damage = 5
        expected = 4
        # Act
        dummy_pokemon.stats['hitpoints'] = 9
        dummy_pokemon.take_damage(input_damage)
        result = dummy_pokemon.stats['hitpoints']
        # Assert
        assert expected == result

        # Arrange
        dummy_pokemon = Pokemon('arbok')
        input_damage = 10
        expected = 0
        # Act
        dummy_pokemon.stats['hitpoints'] = 9
        dummy_pokemon.take_damage(input_damage)
        result = dummy_pokemon.stats['hitpoints']
        # Assert
        assert expected == result

    def test_has_fainted_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('raichu')
        expected = 'has_fainted'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_has_fainted_returns_correctly(self):
        # Arrange
        dummy_pokemon = Pokemon('sandshrew')
        expected = False
        # Act
        dummy_pokemon.stats['hitpoints'] = 9
        result = dummy_pokemon.has_fainted()
        # Assert
        assert expected == result

        # Arrange
        dummy_pokemon = Pokemon('sandslash')
        input_damage = 8
        expected = False
        # Act
        dummy_pokemon.stats['hitpoints'] = 9
        dummy_pokemon.take_damage(input_damage)
        result = dummy_pokemon.has_fainted()
        # Assert
        assert expected == result

        # Arrange
        dummy_pokemon = Pokemon('nidoran(f)')
        expected = True
        # Act
        result = dummy_pokemon.has_fainted()
        # Assert
        assert expected == result

        # Arrange
        dummy_pokemon = Pokemon('nidorina')
        input_damage = 9
        expected = True
        # Act
        dummy_pokemon.stats['hitpoints'] = 9
        dummy_pokemon.take_damage(input_damage)
        result = dummy_pokemon.has_fainted()
        # Assert
        assert expected == result

        # Arrange
        dummy_pokemon = Pokemon('nidoqueen')
        input_damage = 20
        expected = True
        # Act
        dummy_pokemon.stats['hitpoints'] = 9
        dummy_pokemon.take_damage(input_damage)
        result = dummy_pokemon.has_fainted()
        # Assert
        assert expected == result

    def test_add_move_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('nidoran(m)')
        expected = 'add_move'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_add_move_returns_correctly_once(self):
        # Arrange
        dummy_pokemon = Pokemon('nidorino')
        expected = 'tackle'
        # Act
        dummy_pokemon.add_move(tackle)
        result_1 = dummy_pokemon.move_pool[0]._name
        result_2 = dummy_pokemon.move_list[0]
        # Assert
        assert expected == result_1
        assert expected == result_2

    def test_add_move_returns_correctly_twice(self):
        # Arrange
        dummy_pokemon = Pokemon('ninetales')
        expected_1 = ['tackle', "", "", ""]
        expected_2 = [tackle, None, None, None]
        # Act
        dummy_pokemon.add_move(tackle)
        dummy_pokemon.add_move(tackle)
        result_1 = dummy_pokemon.move_list
        result_2 = dummy_pokemon.move_pool
        # Assert
        assert expected_1 == result_1
        assert expected_2 == result_2

    def test_add_move_prints_correctly(self):
        # Arrange
        dummy_pokemon = Pokemon('jigglypuff')
        expected = "This move is already known!\n"
        # Act
        dummy_pokemon.add_move(tackle)
        print_statement = io.StringIO()
        sys.stdout = print_statement
        dummy_pokemon.add_move(tackle)
        sys.stdout = sys.__stdout__
        result = print_statement.getvalue()
        # Assert
        assert expected == result

    def test_alter_pp_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('wigglytuff')
        expected = 'alter_pp'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_alter_pp_changes_move_pp(self):
        # Arrange
        dummy_pokemon = Pokemon('oddish')
        expected = 0
        # Act
        dummy_pokemon.add_move(tackle)
        dummy_pokemon.alter_pp(tackle)
        result = dummy_pokemon.move_pool[0]._powerpoints
        # Assert
        assert expected == result

    def test_delete_move_exists(self):
        # Arrange
        dummy_pokemon = Pokemon('gloom')
        expected = 'delete_move'
        # Act
        result = dir(dummy_pokemon)
        # Assert
        assert expected in result

    def test_delete_move_changes_move_pool_and_move_list(self):
        # Arrange
        dummy_pokemon = Pokemon('vileplume')
        input_move = Move('tackle', 6, 'normal', 100, 'physical')
        expected_pool = [None, None, None, None]
        expected_list = ["", "", "", ""]
        # Act
        dummy_pokemon.add_move(input_move)
        dummy_pokemon.delete_move(input_move)
        result_pool = dummy_pokemon.move_pool
        result_list = dummy_pokemon.move_list
        # Assert
        assert expected_list == result_list
        assert expected_pool == result_pool

    # Arrange
        dummy_pokemon = Pokemon('zubat')
        input_move_1 = Move('tackle', 6, 'normal', 100, 'physical')
        input_move_2 = Move('gust', 5, 'flying', 85, 'special')
        expected_pool = [input_move_2, None, None, None]
        expected_list = ['gust', "", "", ""]
        # Act
        dummy_pokemon.add_move(input_move_1)
        dummy_pokemon.add_move(input_move_2)
        dummy_pokemon.delete_move(input_move_1)
        result_pool = dummy_pokemon.move_pool
        result_list = dummy_pokemon.move_list
        # Assert
        assert expected_list == result_list
        assert expected_pool == result_pool
