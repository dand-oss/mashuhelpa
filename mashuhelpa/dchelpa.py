"""Resolve dataclasses types forward declared with string annotations."""
import dataclasses as dc
import typing

# https://github.com/python-attrs/attrs/issues/288#issuecomment-345556521

# https://stackoverflow.com/questions/51946571/how-can-i-get-python-3-7-new-dataclass-field-types
# https://github.com/python/typing/blob/master/src/typing.py
# https://www.python.org/dev/peps/pep-0484/#the-problem-of-forward-declarations


def resolve_types(
    a_dc: typing.Any,
    globalns: typing.Optional[typing.Dict[str, typing.Any]] = None,
    localns: typing.Optional[typing.Dict[str, typing.Any]] = None,
) -> bool:
    """Resolve dataclass field types from string version."""
    retc = True
    try:
        # resolving is expensive, so check if already done
        retc = getattr(a_dc, f"__attrs_types_{a_dc.__name__}_resolved__")

    except AttributeError:
        # resolve  all the string annotations and forward annotations
        # BY EVAL - slow, and requires full context
        hint_dict = typing.get_type_hints(
            a_dc, globalns=globalns, localns=localns
        )

        # roll the fields
        for cfield in dc.fields(a_dc):
            # is this a type?
            if cfield.name in hint_dict:
                # prefer resolved type!
                cfield.type = hint_dict[cfield.name]

        # mark done
        setattr(a_dc, f"__attrs_types_{a_dc.__name__}_resolved__", True)
    return retc
