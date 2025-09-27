from abc import ABC, abstractmethod


class Character(ABC):
    """Docstring for Character Class"""
    first_name: str
    is_alive: bool

    @abstractmethod
    def die(self) -> None:
        """die docstring from Character Class"""
        pass

    def __init__(self, first_name: str, is_alive: bool = True):
        """__init__ docstring from Character Class"""
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(Character):
    """Docstring for Stark Class"""
    def die(self) -> None:
        """die docstring from Stark Class"""
        self.is_alive = False
