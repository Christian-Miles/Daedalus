from core.ribs.ribmanager import RibManager


class Glider(object):
    """A Glider Object"""

    def __init__(self, num_cells: int = 40) -> None:
        self.num_cells = num_cells
        self.num_ribs = self.num_cells + 1
        self.rib_manager = RibManager()
