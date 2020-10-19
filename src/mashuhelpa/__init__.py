"""
__init__.py
Imports mashuhelpa into module level

side effect
patches Mashuhelpa bug

"""
from .mashuhelpa import *
from .dchelpa import *

from mashuhelpa import compat

compat.register()  # patch mashumaro failing fwd declare
