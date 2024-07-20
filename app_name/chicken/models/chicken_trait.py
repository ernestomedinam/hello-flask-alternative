from app_name.base.models.base import BaseModel
from app_name.db import db
from .personality_trait import PersonalityTrait

class ChickenTrait(BaseModel):
    """
        represents a personality trait for
        a specific chicken on a specific order.
    """
    id: int = db.Column(db.Integer, primary_key=True)
    chicken_id: int = db.Column(db.ForeignKey("chicken.id"), nullable=False)
    order: int = db.Column(db.Integer, nullable=False)
    trait: PersonalityTrait = db.Column(db.Enum(PersonalityTrait), nullable=False)
