import os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader

UI_FILE=os.path.join(os.path.dirname(__file__), 'main_window.ui')

class MainWindow:
    def __init__(self):
        loader=QUiLoader()
        self.ui=loader.load(UI_FILE,None)
        self.ui.setWindowTitle("Main Window")
        self.current_user_info=None

    def on_login_success(self,user_data):
        """Informasi dari LoginWindow dan menjalankan main"""
        self.current_user_info=user_data
        self.show()

    def show(self):
        """Fungsi untuk menampilkan window"""
        self.ui.show()

    def close(self):
        """Fungsi untuk menutup window"""
        self.ui.close()

    def setup_tabs(self):
        """Fungsi untuk mengatur tiap tab yang ada """