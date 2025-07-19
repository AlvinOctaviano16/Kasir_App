from core import mencari_item_kode_logic,proses_transaksi
from data import data_manager_sqlite
from PySide6.QtWidgets import (QPushButton, QLineEdit, QTableWidget, QSpinBox, 
                               QMessageBox, QLabel, QAbstractItemView, QHeaderView, QTableWidgetItem)
from PySide6.QtCore import Qt

class KasirTabHandler:
    """Fungsi untuk backend dan koneksi tab_kasir"""
    def __init__(self,tab_widget,user_id):
        self.parent_tab= tab_widget
        self.keranjang=[]
        self.current_user_id= user_id
        self.total_harga=0
        self.mencari_widgets()
        self.inisialisasi_tampilan()
        self.setup_connection()


    def mencari_widgets(self):
        """Fungsi untuk menyiapkan dan melakukan input terhadap semua object pada bagian pencarian item"""
        #Bagian Input
        self.item_kode_input=self.parent_tab.findChild(QLineEdit,"kode_item_input")
        self.nama_item_output=self.parent_tab.findChild(QLineEdit,"nama_item_output")
        self.harga_item_output=self.parent_tab.findChild(QLineEdit,"harga_item_output")
        self.jumlah_item=self.parent_tab.findChild(QSpinBox,"spinbox_jumlah_item")
        self.tambah_keranjang_button=self.parent_tab.findChild(QPushButton,"button_tambah_keranjang")
        
        #Bagian Tabel Transaksi
        self.tabel_keranjang=self.parent_tab.findChild(QTableWidget,"keranjang_transaksi_tabel")
        self.total_harga_label=self.parent_tab.findChild(QLabel,"nominal_label")
        self.bayar_button=self.parent_tab.findChild(QPushButton,"bayar_button")

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

    def setup_connection(self):
        """Fungsi untuk menghubungkan semua signal button"""
        self.item_kode_input.returnPressed.connect(self.on_search_item)
        self.tambah_keranjang_button.clicked.connect(self.tambah_ke_keranjang)
        self.bayar_button.clicked.connect(self.process_pembayaran)

    def on_search_item(self):
        """Fungsi untuk melakukan pencarian item saat mencari item by kode"""
        input_section=self.item_kode_input.text()
        if not input_section:
            return
        
        informasi_item=mencari_item_kode_logic(input_section)
        self.searched_item=informasi_item

        if informasi_item:
            self.nama_item_output.setText(informasi_item['nama_item'])
            self.harga_item_output.setText(str(informasi_item['harga_item']))
            self.jumlah_item.setValue(1)
            self.jumlah_item.setFocus()
        else:
            self.nama_item_output.clear()
            self.harga_item_output.clear()
            QMessageBox.warning(self.parent_tab, "Error", f"Item dengan kode '{input_section}' tidak ditemukan.")

    def tambah_ke_keranjang(self):
        """Fungsi saat tombol Tambah diklik"""
        if not self.searched_item:
            QMessageBox.warning(self.parent_tab,"Item belum dipilih", "Silahkan cari item terlebih dahulu")
        
        jumlah=self.jumlah_item.value()
        if jumlah <=0 :
             QMessageBox.warning(self.parent_tab,"Jumlah tidak valid", "Jumlah item harus lebih dari Nol")
             return
        
        
        listed_item=next((item for item in self.keranjang if item['id_item']==self.searched_item['id_item']), None) if self.searched_item else ""

        if listed_item:
            listed_item['jumlah_item']+=jumlah
        else:
            if self.searched_item is not None:
                self.keranjang.append ({
                    'id_item':self.searched_item['id_item'],
                    'nama_item':self.searched_item['nama_item'],
                    'kode_item':self.searched_item['kode_item'],
                    'harga_item':self.searched_item['harga_item'],
                    'jumlah_item':jumlah
                })
        self.update_keranjang_display()
        self.reset_input()

    def update_keranjang_display(self): 
        """Memperbarui keranjang transaksi"""
        self.tabel_keranjang.setRowCount(0)
        self.total_harga=0
        for row_index, item in enumerate(self.keranjang):
            self.tabel_keranjang.insertRow(row_index)
            subtotal=item['harga_item'] * item['jumlah_item']
            self.total_harga+=subtotal
            item['nominal_saat_transaksi']=subtotal
            self.tabel_keranjang.setItem(row_index,0,QTableWidgetItem(item['kode_item']))
            self.tabel_keranjang.setItem(row_index,1,QTableWidgetItem(item['nama_item']))
            self.tabel_keranjang.setItem(row_index,2,QTableWidgetItem(f"{item['harga_item']:,}"))
            self.tabel_keranjang.setItem(row_index,3, QTableWidgetItem(str(item['jumlah_item'])))
            self.tabel_keranjang.setItem(row_index,4,QTableWidgetItem(f"{item['nominal_saat_transaksi']:,}"))

        self.total_harga_label.setText(f"Rp {self.total_harga:,}")

    def reset_input(self):
        """Fungsi untuk membersihkan input dan output qlinedit setelah item ditambahkan"""
        self.item_kode_input.clear()
        self.nama_item_output.clear()
        self.harga_item_output.clear()
        self.jumlah_item.setValue(1)
        self.searched_item=None
        self.item_kode_input.setFocus()

    def process_pembayaran(self):
        """Fungsi interaksi saat tombol klik diketik """
        if not self.keranjang:
            QMessageBox.warning(self.parent_tab,"Keranjang Kosong","Tidak ada item untuk dibayar")
            return
        
        reply=QMessageBox.question(self.parent_tab,"Konfirmasi Pembayaran",
                                   f"Total belanja adalah {self.total_harga_label.text()}. \n Lanjut pembayaran?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        
        if reply==QMessageBox.StandardButton.Yes:
            success,pesan=proses_transaksi(self.current_user_id,self.keranjang,self.total_harga) 
            if success :
                QMessageBox.information(self.parent_tab,"Berhasil", f"Transaksi {pesan} berhasil disimpan")
                self.keranjang.clear()
                self.update_keranjang_display()
                self.reset_input()
            else :
                QMessageBox.critical(self.parent_tab,"Gagal",pesan or "Terjadi kesalahan...")