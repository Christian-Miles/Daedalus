import numpy as np
import scipy as sp
import pathlib
import matplotlib.pyplot as plt


class Rib:
    def __init__(self, aoa: float = 0, rot_x_axis: float = 0.0) -> None:
        self.rib_file = str(pathlib.Path(__file__).parents[2]) + "/defaults/ribs.dat"
        self.aoa = 0
        self.arc_ang = 0
        self.import_rib(self.rib_file)
        self.apply_rot(aoa=aoa, arc_ang=rot_x_axis)

    def import_rib(self, rib_file: str) -> None:
        with open(rib_file, "r") as f:
            self.airfoil_name = f.readline().strip()
            lines = f.readlines()
            point_list = []

            for line in lines:
                values = line.split()
                values.insert(1, 0.0)
                values = np.float_(values)
                values[0] = (values[0] - 1) * -1  # Flip and set tail to be 0 point
                values = values[np.newaxis].T
                point_list.append(values)

            # Returns the individual points of a rib in the form of [[x], [y], [z]]
            self.rib_points_original = np.array(point_list)
            self.rib_points = np.array(point_list)

    def apply_rot(self, aoa: float = None, arc_ang: float = None) -> None:

        self.aoa = aoa if aoa is not None else self.aoa
        self.arc_ang = arc_ang if arc_ang is not None else self.arc_ang

        aoa_rad = np.deg2rad(self.aoa)
        arc_rad = np.deg2rad(self.arc_ang)

        rotation_matrix = np.array(
            [
                [np.cos(aoa_rad), 0, -np.sin(aoa_rad)],
                [0, np.cos(arc_rad), np.sin(arc_rad)],
                [np.sin(aoa_rad), -np.sin(arc_rad), np.cos(aoa_rad) * np.cos(arc_rad)],
            ]
        )

        for index, item in enumerate(self.rib_points_original):
            self.rib_points[index] = rotation_matrix @ item

    def visualize(self):
        """Purely for debugging, will be removed in later releases"""
        x = []
        y = []
        z = []

        for each in self.rib_points.squeeze():
            x.append(each[0])
            y.append(each[1])
            z.append(each[2])

        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(x, y, z, c="r")
        ax.axes.set_xlim3d(-1, 1)
        ax.axes.set_ylim3d(-1, 1)
        ax.axes.set_zlim3d(-1, 1)
        plt.show()
