from abc import ABC, abstractmethod
from dataclasses import dataclass
from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.sql.schema import SchemaItem
from typing import List

"""Provides helper classes and functionas for data models."""


class AbstractClassicalModel(ABC):
    """
    Abstract base class meant for data models to simplify classical mapping with SQLAlchemy.
    Can be used with data classes to simplify development even further and remove boiler plate code.
    """

    @classmethod
    @abstractmethod
    def make_table(cls, metadata: MetaData) -> Table:
        pass


@dataclass
class ExampleClass(AbstractClassicalModel):
    property1: int
    property2: str

    @classmethod
    def make_table(cls, metadata: MetaData) -> Table:
        constraints: List[SchemaItem] = [
            Column(name='id', type_=Integer, primary_key=True),
            Column(name='property1', type_=Integer, nullable=False),
            Column(name='property2', type_=String, nullable=False)
        ]

        return Table('example_classes', metadata, *constraints)
