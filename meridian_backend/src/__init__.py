"""Meridian-X backend package marker + import bootstrap.

Ensures the backend root (the directory containing database.py) is importable
whenever anything under ``src`` is imported, so bare ``from database import``
statements keep working regardless of the process working directory. No other
imports here on purpose: importing this package must stay side-effect free.
"""

import os as _os
import sys as _sys

_backend_root = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
if _backend_root not in _sys.path:
    _sys.path.insert(0, _backend_root)

del _os, _sys, _backend_root
