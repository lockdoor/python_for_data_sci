from .DiamondTrap import King
import unittest


class TestDimondTrap(unittest.TestCase):

    def test_King(self):
        Joffrey = King('Joffrey')

        d = {
            'first_name': 'Joffrey',
            'is_alive': True,
            'family_name': 'Baratheon',
            'eyes': 'brown',
            'hairs': 'dark'
        }

        self.assertEqual(Joffrey.__dict__, d)

        # print(Joffrey.__doc__)
        # print(Joffrey.die.__doc__)
        # print(King.mro())

        Joffrey.set_eyes('blue')
        Joffrey.set_hairs('light')

        self.assertEqual(Joffrey.get_eyes(), 'blue')
        self.assertEqual(Joffrey.get_hairs(), 'light')

        d['eyes'] = 'blue'
        d['hairs'] = 'light'
        self.assertEqual(Joffrey.__dict__, d)
