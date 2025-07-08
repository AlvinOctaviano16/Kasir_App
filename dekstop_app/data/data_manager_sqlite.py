import sqlite3
import os

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DB_PATH=os.path.join(BASE_DIR,'..','kasir.db')

def create_Connection():
    """Koneksi program ke database (otomatis input database by program)"""
    connection=None
    try:
        connection=sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        print(e)
    return connection

def get_all_item():
    """Mengambil semua item pada tabel database item"""
    connection=create_Connection()
    if connection is not None:
        try:
            kursor=connection.cursor()
            kursor.execute("SELECT * FROM item")
            item=kursor.fetchall()
            return item
        except sqlite3.Error as e:
            print(f"Error saat mengambil data item : {e}")
            return []
        finally:
            #Menutup koneksi
            connection.close()
    return []

def add_item(kode:str,nama:str,harga:int,stock:int):
    """Fungsi menambahkan item baru ke database"""
    connection=create_Connection();
    if connection is not None:
        try:
            kursor=connection.cursor()
            query="INSERT INTO item(kode_item,nama_item,harga_item,stock_item) VALUES (?,?,?,?)"
            kursor.execute(query, (kode,nama,harga,stock))
            connection.commit()

            print(f"Item {nama} berhasil ditambahkan")
            return True
        except sqlite3.Error as e:
            print(f"Error saat menambahkan item : {e}")
            return False
        finally :
            connection.close()
    return False

def delete_item(kode:str):
    """Fungsi untuk menghapus item berdasarkan kode_item"""
    connection=create_Connection()
    if connection is not None:
        try:
            kursor=connection.cursor()
            query="DELETE FROM item WHERE kode_item=?"
            kursor.execute(query,(kode,))
            connection.commit()
            print(f"Item dengan kode {kode} berhasil dihapus")
            return True
        except sqlite3.Error as e:
            print(f"Error saat menghapus item : {e}")
            return False
        finally:
            connection.close()
    return False 

if __name__=="__main__":
    print("Testing fungsi terbaru")
    add_item("O0003","Obeng A",11000,25)
    delete_item("O0003")
    products=get_all_item()

    if products:
        print("Berhasil mengambil data ...")
        for it in products:
            print(it)
    else:
        print("Gagal mengambil data ...")