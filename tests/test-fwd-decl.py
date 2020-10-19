"""
tests/test-fwd-decl.py

No inhertance
forward declare classes
"""

from dataclasses import dataclass
from mashumaro.serializer.base.metaprogramming import CodeBuilder
import mashuhelpa  # patches CodeBuilder on import


@dataclass
class Member:
    count: int


@dataclass
class MainClass:
    member: Member


builder = CodeBuilder(MainClass)
builder.add_from_dict()
