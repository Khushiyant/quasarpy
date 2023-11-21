from xml.etree.ElementTree import Element, SubElement, tostring
from typing import List, Callable, Optional, Any
from abc import ABC, abstractmethod
import json


class Formatter(ABC):
    @abstractmethod
    def format(self, data):
        ...


class JsonFormatter(Formatter):
    # TODO: Process the data
    def format(self, data) -> str:
        return json.dumps(data, indent=4)


class XmlFormatter(Formatter):

    def format(self, data) -> Any:
        def serialize(data):
            root = Element(data.__class__.__name__)
            for name, value in data.__dict__.items():
                if isinstance(value, list):
                    for item in value:
                        SubElement(root, name).text = item.__class__.__name__
                else:
                    SubElement(root, name).text = value.__class__.__name__
            return tostring(root, encoding='utf8').decode('utf8')

        if isinstance(data, (list, tuple)):
            return '\n'.join(serialize(item) for item in data)
        else:
            return serialize(data)

# TODO: Class object handling


def formatted_data(data, formatter):
    return formatter.format(data)
