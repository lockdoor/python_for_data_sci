import unittest
from .S1E9 import Character, Stark


class TestS1E9(unittest.TestCase):

    def test_can_instantiate_Stark(self):
        Ned = Stark("Ned")

        self.assertEqual(Ned.__dict__, {'first_name': 'Ned', 'is_alive': True})
        self.assertTrue(Ned.is_alive)

        Ned.die()
        self.assertFalse(Ned.is_alive)

        self.assertEqual(Ned.__doc__, 'Docstring for Stark Class')
        self.assertEqual(Ned.__init__.__doc__,
                         '__init__ docstring from Character Class')
        self.assertEqual(Ned.die.__doc__, 'die docstring from Stark Class')

    def test_can_init_is_alive(self):
        Lyanna = Stark('Lyanna', False)
        self.assertEqual(
            Lyanna.__dict__, {'first_name': 'Lyanna', 'is_alive': False})

    def test_can_not_instantiate_Character(self):
        with self.assertRaises(TypeError):
            Character('name')
