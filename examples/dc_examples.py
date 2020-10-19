"""
examples/dc_examples.py

If you do not or cannot forward declare your classes.

You cannot serialize them as the types are strings.

This tools shows how to turn the strings back to types.

"""
# allows type definitions WITHOUT forward declarations
# by making types into strings
from __future__ import annotations

import typing
from dataclasses import dataclass, is_dataclass
import mashuhelpa as mh


# normal dataclass declarations...
# no MixIns
@dataclass
class MainClass:
    a: int
    # Member is not declared yet
    member_list: typing.List[Member]


# member type follows usage...  NOT forward declared
@dataclass
class Member:
    c: int


# you must build after the type are all known
# AFTER all dataclasses
# at module load time

# run the dataclasses for this module
for obj in [co for co in globals().values() if is_dataclass(co)]:
    # this runs the builder
    mh.build_mashumaro(obj)
    # resolves the field types USING THE MODULE CONTEXT
    mh.resolve_types(obj, localns=globals())
