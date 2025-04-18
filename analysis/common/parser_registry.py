from dataclasses import dataclass
from enum import Enum
import pkgutil
import importlib

@dataclass
class ParserVersion:
    schema_name : str
    version : int

def parser_class(version : ParserVersion):
    """
    A decorator for marking a class as a parser.
    It must inherit from BaseParser
    """
    def decorator(cls):
        ParserRegistry.add_parser(version, cls)
        return cls
    
    return decorator

class Parser:
    pass

class ParserRegistry:
    parsers : dict[ParserVersion, Parser]

    @staticmethod
    def add_parser(version : ParserVersion, cls):
        ParserRegistry.parsers[version] = cls

    @staticmethod
    def get_parser_versions() -> list[ParserVersion]:
        return ParserRegistry.parsers.keys()
    
    @staticmethod
    def load_parsers():
        package = analysis.common.parsers
        for finder, module_name, is_pkg in pkgutil.iter_modules(package.__path__):
            full_module_name = f"{package.__name__}.{module_name}"
            importlib.import_module(full_module_name)
