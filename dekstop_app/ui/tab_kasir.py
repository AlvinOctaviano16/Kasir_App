from core import kasir_logic
from data import data_manager_sqlite
from PySide6.QtWidgets import QPushButton,QLineEdit,QTableWidget,QSpinBox,QMessageBox,QLabel,QAbstractItemView,QHeaderView
from PySide6.QtCore import Qt

class KasirTabHander:
    """Fungsi untuk backend dan koneksi tab_kasir"""
    def __init__(self,tab_widget,user_id):
        self.parent_tab= tab_widget
        self.keranjang=[]
        self.current_user_id= user_id
    
        

    def mencari_widgets(self):
        """Fungsi untuk menyiapkan dan melakukan input terhadap semua object pada bagian pencarian item"""
        #Bagian Input
        self.item_id_input=self.parent_tab.findChild(QLineEdit,"kode_item_input")
        self.nama_item_output=self.parent_tab.findChild(QLineEdit,"nama_item_output")
        self.harga_item_output=self.parent_tab.findChild(QLineEdit,"harga_item_output")
        self.jumlah_item=self.parent_tab.findChiild(QSpinBox,"spinbox_jumlah_item")
        self.tambah_keranjang=self.parent_tab.findChild(QPushButton,"button_tambah_keranjang")
        
        #Bagian Tabel Transaksi
        self.tabel_keranjang=self.parent_tab.findChild(QTableWidget,"keranjang_transaksi_tabel")
        self.total_harga=self.parent_tab.findChild(QLabel,"total_label")
        self.bayar=self.parent_tab.findChild(QPushButton,"bayar_button")

    def inisialisasi_tampilan(self):
        """Fungsi untuk menentukan fondasi tampilan tab kasir"""
        self.nama_item_output.setReadOnly(True)
        self.harga_item_output.setReadOnly(True)

        if self.tabel_keranjang:
            headers=["Kode","Nama Item", "Harga", "Jumlah", "Subtotal"]
            self.tabel_keranjang.setColumnCount(len(headers))
            self.tabel_keranjang.setHorizontalHeaderLabels(headers)
            self.tabel_keranjang.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            self.tabel_keranjang.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            self.tabel_keranjang.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


    