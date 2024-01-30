from enum import Enum


class ModelType(Enum):
    """
    Enum representing different types of models.
    """
    CLASS = 'CLASS'
    METHOD = 'METHOD'


class SmellType(Enum):
    """
    Enumeration representing different types of smells.
    """
    CLASS = 'CLASS'
    METHOD = 'METHOD'


class FormatterType(Enum):
    """
    Represents the available formatter types for data serialization.
    """

    JSON = 'JSON'
    XML = 'XML'
