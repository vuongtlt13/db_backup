from typing import List, TYPE_CHECKING

from utils import find_supported_drivers

if TYPE_CHECKING:
    from driver import Driver

SUPPORTED_DRIVERS: List["Driver"] = []

find_supported_drivers(SUPPORTED_DRIVERS)
