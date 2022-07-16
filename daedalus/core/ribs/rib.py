import numpy as np
import scipy as sp


class Rib:
    def __init__(self, rib_file: str = "undefined", aoa: float = 0.0) -> None:
        self.rib_file = rib_file
        self.aoa = aoa

    def import_rib(self) -> None:
        with open(self.rib_file, "r") as f:
            # Read in points of XFLR file (or a daedalus airfoil file)
            # define these points in 3d space via numpy arrays
            # self.airfoil_points = np.array([[x, y, z] for x, y, z in f])
            pass
