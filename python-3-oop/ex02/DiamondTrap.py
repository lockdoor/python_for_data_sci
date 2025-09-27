from .S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Docstring for King Class"""
    def __init__(self, first_name: str, is_alive: bool = True) -> object:
        """__init__ docstring from King Class"""
        super().__init__(first_name, is_alive)

    def get_eyes(self) -> str:
        """get_eyes docstring from King Class"""
        return self.eyes

    def set_eyes(self, eyes: str) -> None:
        """set_eyes docstring from King Class"""
        self.eyes = eyes

    def get_hairs(self) -> str:
        """get_hairs docstring from King Class"""
        return self.hairs

    def set_hairs(self, hairs: str) -> None:
        """set_hairs docstring from King Class"""
        self.hairs = hairs
