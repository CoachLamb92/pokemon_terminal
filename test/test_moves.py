from src.moves import Move

class TestMoveAttributes:
    def test_move_name_attribute_exists(self):
        # Arrange
        dummy_move = Move('tackle')
        expected = '_name'
        # Act
        result = dir(dummy_move)
        # Assert
        assert expected in result

    def test_move_name_attribute_returns_name(self):
        # Arrange
        dummy_move = Move('scratch')
        expected = 'scratch'
        # Act
        result = dummy_move._name
        # Assert
        assert expected == result

    def test_move_damage_attribute_exists(self):
        # Arrange
        dummy_move = Move('bite')
        expected = '_damage'
        # Act
        result = dir(dummy_move)
        # Assert
        assert expected in result

    def test_move_damage_attribute_returns_damage(self):
        # Arrange
        dummy_move = Move('crunch')
        expected = 50
        # Act
        result = dummy_move._damage
        # Assert
        assert expected == result

        # Arrange
        dummy_move = Move('splash', damage=0)
        expected = 0
        # Act
        result = dummy_move._damage
        # Assert
        assert expected == result

    def test_move_type_attribute_exists(self):
        # Arrange
        dummy_move = Move('defense curl')
        expected = '_type'
        # Act
        result = dir(dummy_move)
        # Assert
        assert expected in result

    def test_move_type_attribute_returns_type(self):
        # Arrange
        dummy_move = Move('tail whip')
        expected = 'normal'
        # Act
        result = dummy_move._type
        # Assert
        assert expected == result

        # Arrange
        dummy_move = Move('water gun', type='water')
        expected = 'water'
        # Act
        result = dummy_move._type
        # Assert
        assert expected == result

    def test_move_accuracy_attribute_exists(self):
        # Arrange
        dummy_move = Move('growl')
        expected = '_accuracy'
        # Act
        result = dir(dummy_move)
        # Assert
        assert expected in result

    def test_move_accuracy_attribute_returns_accuracy(self):
        # Arrange
        dummy_move = Move('string shot')
        expected = 100
        # Act
        result = dummy_move._accuracy
        # Assert
        assert expected == result

        # Arrange
        dummy_move = Move('sand attack', accuracy=70)
        expected = 70
        # Act
        result = dummy_move._accuracy
        # Assert
        assert expected == result

    def test_move_category_attribute_exists(self):
        # Arrange
        dummy_move = Move('twin needle')
        expected = '_category'
        # Act
        result = dir(dummy_move)
        # Assert
        assert expected in result

    def test_move_category_attribute_returns_category(self):
        # Arrange
        dummy_move = Move('harden', category='status')
        expected = 'status'
        # Act
        result = dummy_move._category
        # Assert
        assert expected == result

        # Arrange
        dummy_move = Move('slash', category='physical')
        expected = 'physical'
        # Act
        result = dummy_move._category
        # Assert
        assert expected == result

        # Arrange
        dummy_move = Move('bubble', category='special')
        expected = 'special'
        # Act
        result = dummy_move._category
        # Assert
        assert expected == result

        
class TestMoveMethods:
    def test_move_has_hit_method_exists(self):
        # Arrange
        dummy_move = Move('poison sting')
        expected = '_has_hit'
        # Act
        result = dir(dummy_move)
        # Assert
        assert expected in result

    def test_move_has_hit_method_returns_correctly(self):
        # Arrange
        dummy_move = Move('gust')
        expected = True
        # Act
        for _ in range(100):
            result = dummy_move._has_hit()
            # Assert
            assert expected == result

        # Arrange
        dummy_move = Move('karate chop', accuracy=100)
        expected = True
        # Act
        for _ in range(100):
            result = dummy_move._has_hit()
            # Assert
            assert expected == result

        # Arrange
        dummy_move = Move('peck', accuracy=0)
        expected = False
        # Act
        for _ in range(100):
            result = dummy_move._has_hit()
            # Assert
            assert expected == result