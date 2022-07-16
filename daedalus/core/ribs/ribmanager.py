from rib import Rib


class RibManager:
    """A class to manage the ribs of a glider."""

    def __init__(self) -> None:
        # Initialize the glider with 30 ribs at varying angles of attack
        self.ribs = []

        for i in range(0, 30):
            self.ribs.append(Rib("glider_rib.rib"))
