"""
Why

tests/test-fwd-decl.py will fail with mashumaro

Mashumaro demands you INHERIT from its base classe.

https://github.com/Fatal1ty/mashumaro/pull/24

Fatal1ty commented on Nov 21, 2020
It seems like you're using this library in a wrong way. You shouldn't use CodeBuilder class on your own.
"""
from mashumaro.serializer.base import metaprogramming as mp


def _ensure_module_imported(self, module: str) -> None:
    # blow off buggy cache fishing
    # import checks all that for you!
    if module not in self.modules:
        self.modules.add(module)
        self.add_line(f"import {module}")


def register():
    # monkeypatch failing class member
    mp.CodeBuilder.ensure_module_imported = _ensure_module_imported
