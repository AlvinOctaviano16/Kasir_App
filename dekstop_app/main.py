from PySide6.QtWidgets import QApplication
from ui import LoginWindow
from data import *
from ui import *
from core import verifikasi_login
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

    