import os
import sys
from core.kasir_logic import verifikasi_login
from PySide6.QtWidgets import QMainWindow,QMessageBox,QLineEdit,QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Signal,QObject
from PySide6.QtGui import QIcon

UI_FILE=os.path.join(os.path.dirname(__file__), 'login_window.ui')

class LoginWindow(QObject):
    login_succes=Signal(dict)
    def __init__(self):
        super().__init__()
        loader=QUiLoader()
        self.ui=loader.load(UI_FILE,None)
        self.ui.setWindowTitle("Login Aplikasi Kasir")

        #Mengunci ukuran window
        self.ui.setFixedSize(600,400)

        #Mencari tiap element di ui
        self.username_input=self.ui.findChild(QLineEdit,"username_input")
        self.password_input=self.ui.findChild(QLineEdit,"password_input")
        self.login_button=self.ui.findChild(QPushButton,"login_button")

        #Menyembunyikan tampilan password
        if self.password_input is not None: 
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        #Menghubungkan button dengna backend
        if self.login_button is not None:
            self.login_button.clicked.connect(self.handle_login)

        if self.password_input is not None:
            self.password_input.returnPressed.connect(self.handle_login)
    
    def show(self):
        """Fungsi untuk menampilkan window"""
        self.ui.show()

    def close(self):
        """Fungsi untuk menutup window"""
        self.ui.close()

    
    def handle_login(self):
        """Fungsi Backend Button"""
        username = self.username_input.text() if self.username_input else ""
        password = self.password_input.text() if self.password_input else ""

        if not username or not password:
            QMessageBox.warning(self.ui,"Error","Username dan Password tidak boleh kosong")
            return

        user_data=verifikasi_login(username,password) 

        if user_data:
            print(f"Login berhasil sebagai {user_data['user_name']} dengan role {user_data['role']}.")  
            self.login_succes.emit(user_data)
            self.close()
        else:
            QMessageBox.critical(self.ui,"Login Gagal","Username atau Password salah!")
        