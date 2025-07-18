import os
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtUiTools import QUiLoader
from .tab_kasir import KasirTabHandler

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
        print(f"Login berhasil. Menyiapkan Main Window untuk user: {self.current_user_info['nama_user']}")
        self.setup_tabs()
        self.show()
        

    def show(self):
        """Fungsi untuk menampilkan window"""
        self.ui.show()

    def close(self):
        """Fungsi untuk menutup window"""
        self.ui.close()

    def setup_tabs(self):
        """Fungsi untuk mempersiapkan tiap tab yang ada"""
        self.kasir_tab=self.ui.findChild(QWidget,"tab_kasir")
        self.stock_tab=self.ui.findChild(QWidget,"tab_stok")
        user_id=self.current_user_info['id_user'] if self.current_user_info else ""

        if self.kasir_tab and self.current_user_info:
            self.kasir_handler=KasirTabHandler(self.kasir_tab,user_id)
            print("KasirTabHandler berhasil di inisialisasi")
      
        
    