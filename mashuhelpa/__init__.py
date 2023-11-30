"""
Imports mashuhelpa into module level.

side effect
patches Mashuhelpa bug
"""
from .dchelpa import *
from .mashuhelpa import *
from mashuhelpa import compat

compat.register()  # patch mashumaro failing fwd declare
