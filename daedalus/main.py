from PySide6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Daedalus")

if __name__ == "__main__":
    # Create the Qt Application
    app = QApplication()
    # Create a button, connect it and show it
    main_window = MainWindow()
    main_window.show()
    # Run the main Qt loop
    app.exec()