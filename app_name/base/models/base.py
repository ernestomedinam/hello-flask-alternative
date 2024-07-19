import enum
import json
from datetime import timezone
from typing import Self

from app_name.db import db


class BaseEnum(enum.Enum):
    """ base class for Enum classes """

    @classmethod
    def list_values(cls):
        return list(map(lambda item: item.value, cls))

    @classmethod
    def list_names(cls):
        return list(map(lambda item: item.name, cls))

    @classmethod
    def serialize(cls):
        return json.dumps(dict(list(map(lambda item: (item.name, item.value), cls))))


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {
        "mysql_engine": "InnoDB"
    }
    created_at = db.Column(db.DateTime(timezone=True), default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=db.func.now(), onupdate=db.func.now(), nullable=False)

    def __init__(self, **kwargs):
        """ class constructor """
        self._provision(**kwargs)

    def _provision(self, **kwargs) -> bool:
        """ sets attributes for keys in validated_data """
        count = 0
        tuples = list(kwargs.items())
        for (key, value) in tuples:
            if hasattr(self, key):
                count += 1
                setattr(self, key, kwargs.pop(key))
        return count > 0

    @classmethod
    def create(cls, **kwargs) -> Self | None:
        """ runs class constructor, commits to db and returns instance """
        instance = cls(**kwargs)
        if isinstance(instance, cls):
            db.session.add(instance)
            try:
                db.session.commit()
                return instance
            except Exception as error:
                db.session.rollback()
                print(error.args)
        return None

    def update(self, **kwargs) -> bool:
        """ updates attributes for self from keys on validated_data, commits to db and returns boolean """
        updated = self._provision(**kwargs)
        if updated:
            try:
                db.session.commit()
                return True
            except Exception as error:
                db.session.rollback()
                print(error.args)
        return False

    def delete(self) -> bool:
        """ deletes and commits to db, returns boolean """
        db.session.delete(self)
        try:
            db.session.commit()
            return True
        except Exception as error:
            db.session.rollback()
            print(error.args)
        return False

    @classmethod
    def get(cls, **kwargs) -> Self | None:
        """ queries class for a specific criteria with unique value; expects/returns one or none """
        # kwergs = map(lambda key, value: f"{key}={value}", kwargs.items())
        return cls.query.filter_by(
            **kwargs
        ).one_or_none()

    @classmethod
    def find(cls, **filters) -> list[Self]:
        """ queries class for named arguments as filters """
        return cls.query.filter_by(**filters).all()

    @classmethod
    def all(cls) -> list[Self]:
        return cls.query.all()
