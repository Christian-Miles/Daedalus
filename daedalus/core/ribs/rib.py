import numpy as np
import scipy as sp
import pathlib
import matplotlib.pyplot as plt


class Rib:
    def __init__(self, aoa: float = -4.0, rot_x_axis: float = 0.0) -> None:
        self.rib_file = str(pathlib.Path(__file__).parents[2]) + "/defaults/ribs.dat"
        self.aoa = 0
        self.arc_rot = 0
        self.import_rib(self.rib_file)
        self.apply_aoa(aoa)
        self.test()

    def import_rib(self, rib_file: str) -> None:
        with open(rib_file, "r") as f:
            self.airfoil_name = f.readline().strip()
            lines = f.readlines()
            point_list = []

            for line in lines:
                values = np.float_(line.split())
                values[0] = (values[0] - 1) * -1  # Flip and set tail to be 0 point
                values = np.append(values, 0.0)
                point_list.append(values)

            # Returns the individual points of a rib in the form of [x, y, z]
            self.rib_points = np.array(point_list)

    def apply_aoa(self, aoa: float) -> None:
        """Applies the angle of attack to the rib in 2D."""
        change_list = [-self.aoa, aoa]
        self.aoa = aoa

        for apply in change_list:
            for index, item in enumerate(self.rib_points):
                aoa_rad = np.deg2rad(apply)
                x_new = item[0] * np.cos(aoa_rad) - item[1] * np.sin(aoa_rad)
                z_new = item[0] * np.sin(aoa_rad) + item[1] * np.cos(aoa_rad)
                self.rib_points[index] = [x_new, z_new, item[2]]

    def apply_arc(self, angle: float) -> None:
        pass

    def apply_arc_rot(self, angle: float) -> None:
        """Applies the arc rotation to the rib in 2D."""
        change_list = [-self.arc_rot, angle]
        self.arc_rot = angle

        for apply in change_list:
            for index, item in enumerate(self.rib_points):
                arc_rad = np.deg2rad(apply)
                z_new = item[1] * np.cos(arc_rad) - item[2] * np.sin(arc_rad)
                y_new = item[1] * np.sin(arc_rad) + item[2] * np.cos(arc_rad)
                self.rib_points[index] = [item[0], y_new, z_new]

    def visualize(self):
        """Purely for debugging, will be removed in later releases"""
        x = []
        y = []
        z = []

        for each in self.rib_points:
            x.append(each[0])
            y.append(each[2])
            z.append(each[1])

        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(x, y, z, c="r")
        ax.axes.set_xlim3d(-1, 1)
        ax.axes.set_ylim3d(-1, 1)
        ax.axes.set_zlim3d(-1, 1)
        plt.show()
