import pytest
from app_name.chicken.models.chicken import Chicken
from app_name.chicken.models.css_color import CSSColor

def test_create_a_chicken_from_name_and_color(db_session):
    """
        tests a chicken can be created with 
        a name and a color.
    """
    some_chicken = Chicken.create(
        name="some",
        color=CSSColor.BEIGE
    )
    assert some_chicken.name == "some"
    assert some_chicken.color == CSSColor.BEIGE
    assert hasattr(some_chicken, "id")

def test_chicken_has_three_random_traits(db_session):
    """
        tests any created chicken gets three
        random personality traits that have a
        specific order.
    """
    some_chicken = Chicken.create(
        name="some",
        color=CSSColor.BEIGE
    )
    assert len(some_chicken.traits) == 3
