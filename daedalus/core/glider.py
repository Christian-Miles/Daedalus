from .ribs.rib import Rib
import numpy as np


class Glider(object):
    """A Glider Object"""

    def __init__(self) -> None:
        self.ribs = np.array([])

    def add_ribs(self, num_cells: int, rib_type: str) -> None:
        """Add Ribs to the Glider"""
        num_ribs = num_cells + 1
        for i in range(num_ribs):
            self.ribs.append(Rib(rib_type))
