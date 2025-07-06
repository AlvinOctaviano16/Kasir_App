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


if __name__=="__main__":
    print("Testing fungsi get_all_item()...")
    products=get_all_item()

    if products:
        print("Berhasil mengambil data ...")
        for it in products:
            print(it)
    else:
        print("Gagal mengambil data ...")