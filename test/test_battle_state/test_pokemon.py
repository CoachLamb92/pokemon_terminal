from src.battle_state.pokemon import Pokemon

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
    """
    # Uncomment when move_pool is implemented
    def test_pokemon_move_pool_attribute_returns_move_pool(self):
        # Arrange
        dummy_pokemon = Pokemon('spearow')
        expected = ''
        # Act
        result = dummy_pokemon.move_pool
        # Assert
        assert expected == result
    """
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
        expected = ''
        # Act
        result = dummy_pokemon.nickname
        # Assert
        assert expected == result
    """
