from PySide6.QtWidgets import QApplication
from data import *
from ui import *
from core import verifikasi_login
from core import load_theme
import bcrypt
import sys

def main():
    app = QApplication(sys.argv)
    
    # --- TERAPKAN STYLE & STYLESHEET ---
    app.setStyle("Fusion")
    app.setStyleSheet(load_theme("dark_theme.qss"))  
    # --- SELESAI ---

    login_window = LoginWindow()
    main_window=MainWindow()
    
    login_window.login_succes.connect(main_window.show)

    login_window.show()
    sys.exit(app.exec())

    """Fungsi main untuk melakukan testing"""

if __name__=="__main__":
    main()

    