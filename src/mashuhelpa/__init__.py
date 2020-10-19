"""
__init__.py
Imports mashuhelpa into module level

side effect
patches Mashuhelpa bug
"""
from mashuhelpa import compat

from .dchelpa import *
from .mashuhelpa import *

compat.register()  # patch mashumaro failing fwd declare
