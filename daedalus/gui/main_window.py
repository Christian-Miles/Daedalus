from PySide6.QtGui import *
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Daedalus - Home')
        
        # Menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        # File menu
        new_project = file_menu.addAction('New Project')
        open_project = file_menu.addAction('Open Project')
        save_project = file_menu.addAction('Save project')
        save_as_project = file_menu.addAction('Save project as')
        new_project.triggered.connect(self.new_project)
        open_project.triggered.connect(self.open_project)
        save_project.triggered.connect(self.save_project)
        save_as_project.triggered.connect(self.save_as_project)

    def new_project(self):
        #self.folder_path = QFileDialog.getSaveFile(self, 'Select Folder')
        pass
    
    def open_project(self):
        #self.folder_path = QFileDialog.getOpenFileName(self, 'Select Folder')
        pass

    def save_project(self):
        if not self.folder_path:
            self.save_as_project()
        else:
            pass
    
    def save_as_project(self):
        #self.folder_path = QFileDialog.getSaveFileUrl(self, 'Select Folder')
        pass