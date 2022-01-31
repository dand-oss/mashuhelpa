"""
examples/dc_examples.py

If you do not or cannot forward declare your classes.

You cannot serialize them as the types are strings.

This tools shows how to turn the strings back to types.
"""
# allows type definitions WITHOUT forward declarations
# by making types into strings
from __future__ import annotations

from dataclasses import dataclass
from dataclasses import is_dataclass

import mashuhelpa as mh


# normal dataclass declarations...
# no MixIns
@dataclass
class MainClass:
    """Uses a list of member classes, declared later."""

    a_int: int
    # Member is not declared yet
    member_list: list[Member]


# member type follows usage...  NOT forward declared
@dataclass
class Member:
    """Member to be put in a list."""

    c_int: int


# you must build after all types can be known
# AFTER all dataclasses formed
# at module load time

# run the dataclasses for this module
for obj in [co for co in globals().values() if is_dataclass(co)]:
    # this runs the builder
    mh.build_mashumaro(obj)
    # resolves the field types USING THE MODULE CONTEXT
    mh.resolve_types(obj, localns=globals())
