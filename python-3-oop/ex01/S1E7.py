from .S1E9 import Character


class Baratheon(Character):
    """Docstring for Baratheon Class"""
    eyes: str
    hairs: str
    family_name: str

    def __init__(self, first_name: str, is_alive: bool = True) -> object:
        """__init__ docstring from Baratheon Class"""
        super().__init__(first_name, is_alive)
        self.eyes = 'brown'
        self.hairs = 'dark'
        self.family_name = 'Baratheon'

    def die(self) -> None:
        """die docstring from Baratheon Class"""
        self.is_alive = False

    def __str__(self) -> str:
        """__str__ docstring from Baratheon Class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    # representation
    def __repr__(self) -> str:
        """__repr__ docstring from Baratheon Class"""
        return self.__str__()


class Lannister(Character):
    """Docstring for Lannister Class"""
    eyes: str
    hairs: str
    family_name: str

    def __init__(self, first_name: str, is_alive: bool = True) -> object:
        """__init__ docstring from Lannister Class"""
        super().__init__(first_name, is_alive)
        self.eyes = 'blue'
        self.hairs = 'light'
        self.family_name = 'Lannister'

    def die(self) -> None:
        """die docstring from Lannister Class"""
        self.is_alive = False

    def __str__(self) -> str:
        """__str__ docstring from Lannister Class"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """__repr__ docstring from Lannister Class"""
        return self.__str__()

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True) -> object:
        """create_lannister docstring from Lannister Class"""
        return Lannister(first_name, is_alive)
