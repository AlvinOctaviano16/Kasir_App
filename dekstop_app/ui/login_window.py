import os
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

UI_FILE=os.path.join(os.path.dirname(__file__), 'login_window.ui')

class LoginWindow:
    def __init__(self):
        loader=QUiLoader()
        self.ui=loader.load(UI_FILE,None)
        self.ui.setWindowTitle("Login Aplikasi Kasir")

        #Mengunci ukuran window
        self.ui.setFixedSize(800,600)
    
    def show(self):
        """Fungsi untuk menampilkan window"""
        self.ui.show()

    def close(self):
        """Fungsi untuk menutup window"""
        self.ui.close()


