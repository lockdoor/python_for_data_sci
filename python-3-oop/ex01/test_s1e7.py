import unittest
from .S1E7 import Baratheon, Lannister
from io import StringIO
from contextlib import redirect_stdout


class TestS1E7(unittest.TestCase):

    def test_Baratheon(self):
        Robert = Baratheon("Robert")
        d: dict = {
            'first_name': 'Robert',
            'is_alive': True,
            'family_name': 'Baratheon',
            'eyes': 'brown',
            'hairs': 'dark'
        }
        self.assertEqual(Robert.__dict__, d)
        s: str = "<bound method Baratheon.__str__ of Vector: \
('Baratheon', 'brown', 'dark')>"
        self.assertEqual(str(Robert.__str__), s)
        r: str = s.replace('str', 'repr')
        self.assertEqual(str(Robert.__repr__), r)
        result: str = "Vector: ('Baratheon', 'brown', 'dark')"
        # when print(Robert) will take result
        # print(Robert)
        self.assertEqual(str(Robert), result)
        self.assertEqual(str(Robert), Robert.__str__())
        self.assertEqual(str(Robert), Robert.__repr__())
        self.assertTrue(Robert.is_alive)
        self.assertEqual(Robert.__doc__, "Docstring for Baratheon Class")

    def test_Lannister(self):
        Cersei = Lannister('Cersei')
        d = {
            'first_name': 'Cersei',
            'is_alive': True,
            'family_name': 'Lannister',
            'eyes': 'blue',
            'hairs': 'light'
        }
        self.assertEqual(Cersei.__dict__, d)
        self.assertEqual(Cersei.__doc__, "Docstring for Lannister Class")
        self.assertTrue(Cersei.is_alive)
        s = "<bound method Lannister.__str__ of Vector: \
('Lannister', 'blue', 'light')>"
        self.assertEqual(str(Cersei.__str__), s)

    def test_create_lannister(self):
        Jaine: Lannister = Lannister.create_lannister("Jaine", True)

        result = f"Name : {Jaine.first_name, type(Jaine).__name__}, \
Alive : {Jaine.is_alive}"
        expect = "Name : ('Jaine', 'Lannister'), Alive : True"

        self.assertEqual(result, expect)

    def test_repr_str(self):
        '''Test use print instance will print the __str__'''
        except_str = 'hello world'
        Lannister.__str__ = lambda self: 'hello world'
        Jaine = Lannister.create_lannister("Jaine", True)

        with StringIO() as buf, redirect_stdout(buf):
            print(Jaine)
            output = buf.getvalue().strip()
        self.assertEqual(Jaine.__str__(), output, except_str)
