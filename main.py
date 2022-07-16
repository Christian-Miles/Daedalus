from PySide6.QtWidgets import QApplication
from daedalus.gui.main_window import MainWindow

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication()
    # Create a button, connect it and show it
    main_window = MainWindow()
    main_window.show()
    # Run the main Qt loop
    app.exec()