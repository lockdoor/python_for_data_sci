import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate an id"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class use dataclass init with field description"""
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
        This method call after dataclass instanciate
        """
        self.login = self.name[0] + self.surname[:7]
        self.id = generate_id()
