"""
tests/test-fwd-decl.py

No inhertance
forward declare classes
"""
from dataclasses import dataclass

import mashuhelpa  # patches CodeBuilder on import
from mashumaro.serializer.base.metaprogramming import CodeBuilder


@dataclass
class Member:
    """Provides a member for MainClass."""

    count: int


@dataclass
class MainClass:
    """Contains a previously declared member class."""

    member: Member


builder = CodeBuilder(MainClass)
builder.add_from_dict()
