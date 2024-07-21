import os
import json
from random import randint
from typing import List
from app_name.chicken.models.chicken import Chicken
from app_name.chicken.models.css_color import CSSColor


def mock_chickens(
    number_of_chickens: int=1
):
    """
        mocks chicken objects for test
        purposes.
    """
    _pwd = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(_pwd, "../data/chicken_names.json")
    names = []
    with open(file_path, "r") as json_file:
        names = json.load(json_file)
    chickens: List[Chicken] = []
    for time in range(1, number_of_chickens + 1):
        colors = CSSColor.list_names()
        new_chicken = Chicken.create(
            name=names[randint(0, len(names) - 1)],
            color=colors[randint(0, len(colors) - 1)]
        )
        chickens.append(new_chicken)
    return chickens
