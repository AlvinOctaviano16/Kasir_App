from core import kasir_logic
from data import data_manager_sqlite
from PySide6.QtWidgets import QPushButton,QLineEdit,QTableWidget,QSpinBox,QMessageBox

class KasirTabHander:
    def __init__(self,tab_widget):
        self.parent_tab= tab_widget
        self.keranjang=[]
        self
