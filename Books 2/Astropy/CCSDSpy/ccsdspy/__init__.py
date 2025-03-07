# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
IO Interface for Reading CCSDS Data in Python.
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

if not _ASTROPY_SETUP_:
    # For egg_info test builds to pass, put package imports here.

    from .interface import (FixedLength, PacketField)




