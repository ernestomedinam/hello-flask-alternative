from random import randint
from typing import List, Self
from sqlalchemy.orm import Mapped
from app_name.base.models.base import BaseModel
from app_name.db import db
from app_name.base.models.api_exception import APIException
from .css_color import CSSColor
from .chicken_trait import ChickenTrait
from .personality_trait import PersonalityTrait

class Chicken(BaseModel):
    """
        a chicken as an object that requires
        a name and a color to exist.
        it gets 3 random personality traits 
        at birth that have a specific order.
    """
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(40), nullable=False)
    color: CSSColor = db.Column(db.Enum(CSSColor), nullable=False)
    traits: Mapped[List[ChickenTrait]] = db.relationship("ChickenTrait", backref="chicken")

    @classmethod
    def _validate_data(cls, **kwargs):
        data = dict()
        if "name" not in kwargs or kwargs["name"] == "": 
            raise APIException(
                "name needed to create chicken 😐",
                400
            )
        data.update(name=kwargs.pop("name"))
        if "color" not in kwargs: raise APIException(
            "color needed to create chicken 😐",
            400
        )
        data.update(color=kwargs.pop("color"))
        return data

    @classmethod
    def create(cls, **kwargs) -> Self:
        chicken_instance = super().create(
            **cls._validate_data(**kwargs)
        )
        for time in range(1,4):
            chicken_instance.add_trait()
        return chicken_instance

    def add_trait(self) -> None:
        if len(self.traits) == 3:
            raise APIException(
                "a chicken can't have more than 3 personality traits 😐",
                400
            )
        all_traits = PersonalityTrait.list_names()
        random_trait = all_traits[randint(0, len(all_traits) -1)]
        ChickenTrait.create(
            order=len(self.traits) + 1,
            chicken_id=self.id,
            trait=PersonalityTrait[random_trait]
        )
        return
