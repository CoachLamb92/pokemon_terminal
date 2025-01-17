from src.battle_state.pokemon import Pokemon

# attribute tests
def test_pokemon_nickname_attribue_exists():
    # Arrange
    dummy_pokemon = Pokemon('ivysaur')
    expected = 'nickname'
    # Act
    result = dir(dummy_pokemon)
    # Assert
    assert expected in result

def test_pokemon_nickname_attribue_returns_nickname():
    # Arrange
    dummy_pokemon = Pokemon('charmeleon')
    expected = 'charmeleon'
    # Act
    result = dummy_pokemon.nickname
    # Assert
    assert expected == result

def test_pokemon_name_attribue_exists():
    # Arrange
    dummy_pokemon = Pokemon('eevee')
    expected = 'name'
    # Act
    result = dir(dummy_pokemon)
    # Assert
    assert expected in result

def test_pokemon_name_attribue_returns_name():
    # Arrange
    dummy_pokemon = Pokemon('pikachu')
    expected = 'pikachu'
    # Act
    result = dummy_pokemon.name
    # Assert
    assert expected == result

def test_pokemon_level_attribue_exists():
    # Arrange
    dummy_pokemon = Pokemon('squirtle')
    expected = 'level'
    # Act
    result = dir(dummy_pokemon)
    # Assert
    assert expected in result

def test_pokemon_level_attribue_returns_level():
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

def test_pokemon_nature_attribue_exists():
    # Arrange
    dummy_pokemon = Pokemon('wartortle')
    expected = 'nature'
    # Act
    result = dir(dummy_pokemon)
    # Assert
    assert expected in result
"""
Uncomment when natures is implemented
def test_pokemon_nature_attribue_returns_nature():
    # Arrange
    dummy_pokemon = Pokemon('charizard')
    expected = ''
    # Act
    result = dummy_pokemon.nature
    # Assert
    assert expected == result
"""
def test_pokemon_stats_attribue_exists():
    # Arrange
    dummy_pokemon = Pokemon('venusaur')
    expected = 'stats'
    # Act
    result = dir(dummy_pokemon)
    # Assert
    assert expected in result
"""
Uncomment when stats are implemented
def test_pokemon_stats_attribue_returns_stats():
    # Arrange
    dummy_pokemon = Pokemon('blastoise')
    expected = 'charmeleon'
    # Act
    result = dummy_pokemon.stats
    # Assert
    assert expected == result
"""
def test_pokemon_experience_attribue_exists():
    # Arrange
    dummy_pokemon = Pokemon('caterpie')
    expected = 'experience'
    # Act
    result = dir(dummy_pokemon)
    # Assert
    assert expected in result

def test_pokemon_experience_attribue_returns_experience():
    # Arrange
    dummy_pokemon = Pokemon('metapod')
    expected = 0
    # Act
    result = dummy_pokemon.experience
    # Assert
    assert expected == result

def test_pokemon_gender_attribue_exists():
    # Arrange
    dummy_pokemon = Pokemon('butterfree')
    expected = 'gender'
    # Act
    result = dir(dummy_pokemon)
    # Assert
    assert expected in result
"""
def test_pokemon_gender_attribue_returns_gender():
    Uncomment when gender is implemented
    Arrange
    dummy_pokemon = Pokemon('tauros')
    expected = 'male'
    # Act
    result = dummy_pokemon.gender
    # Assert
    assert expected == result

    Uncomment when gender is implemented
    Arrange
    dummy_pokemon = Pokemon('chansey')
    expected = 'female'
    # Act
    result = dummy_pokemon.gender
    # Assert
    assert expected == result

    Uncomment when gender is implemented
    Arrange
    dummy_pokemon = Pokemon('magnemite')
    expected = 'n/a'
    # Act
    result = dummy_pokemon.gender
    # Assert
    assert expected == result

    Uncomment when gender is implemented
    Arrange
    dummy_pokemon = Pokemon('weedle')
    expected = ['male', 'female']
    # Act
    result = dummy_pokemon.gender
    # Assert
    assert result in expected
"""
