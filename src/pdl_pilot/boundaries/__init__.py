"""Empirical boundary models for magnetopause and bow shock."""
from pdl_pilot.boundaries.shue1998 import shue1998_standoff, shue1998_r
from pdl_pilot.boundaries.merka2005 import merka2005_standoff

__all__ = ["shue1998_standoff", "shue1998_r", "merka2005_standoff"]
