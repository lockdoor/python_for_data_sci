import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool
    login: str
    id: str

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.active = True
        self.login = 'Eagle'
        self.id = generate_id()
