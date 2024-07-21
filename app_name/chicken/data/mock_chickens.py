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
    chickens: List[Chicken] = []
    for time in range(1, number_of_chickens + 1):
        colors = CSSColor.list_names()
        new_chicken = Chicken.create(
            name=f"test chicken number {time}",
            color=colors[randint(0, len(colors))]
        )
        chickens.append(new_chicken)
    return chickens
