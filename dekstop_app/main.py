from PySide6.QtWidgets import QApplication
from ui.login_window import LoginWindow
from data.data_manager_sqlite import *
from ui.console_view import *
from core.kasir_logic import *
from core import load_theme
import bcrypt
import sys

def main():
    verifikasi_login("Alvin Octaviano","Octaviano1907")

    """Fungsi main untuk melakukan testing"""

if __name__=="__main__":
    app = QApplication(sys.argv)
    
    # --- TERAPKAN STYLE & STYLESHEET ---
    app.setStyle("Fusion")
    app.setStyleSheet(load_theme("dark_theme.qss"))  
    # --- SELESAI ---

    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())

    