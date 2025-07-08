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

def menampilkan_item(database:list):
    """Fungsi menampilkan semua item"""
    if database:
        print("Menampilkan semua informasi item")
        for it in database:
            _id_item,kode_item,nama_item,harga_item,stock_item=it
            print(f"|{kode_item:{10}} | {nama_item:{10}}  | {harga_item:{10}} | {stock_item:{10}}|")
        return True
    else:
        print("Tidak ada sama sekali item yang tercatat di database")
    return False

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

def menambah_stock(kode:str,sum:int):
    """Fungsi untuk menambah stock"""
    connection=create_Connection()
    if connection is not None:
        try:
            kursor=connection.cursor()
            query="UPDATE item SET stock_item=stock_item+(?) WHERE kode_item=(?)"
            kursor.execute(query,(sum,kode))
            connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error saat menambahkan stock {kode} : {e}")
            return False
        finally:
            connection.close()
    return False

def mengurangi_stock(kode:str,sum:int):
    """Fungsi untuk menambah stock"""
    connection=create_Connection()
    if connection is not None:
        try:
            kursor=connection.cursor()
            query="UPDATE item SET stock_item=stock_item-(?) WHERE kode_item=(?) AND stock_item>=(?)"
            kursor.execute(query,(sum,kode,sum))
            connection.commit()
            if kursor.rowcount>0:
                print(f"Berhasil mengurangi stock item {kode}")
                return True
            else:
                print(f"Gagal mengurangi stock item {kode}. Stock mungkin tidak mencukupi")
                return False
        except sqlite3.Error as e:
            print(f"Error saat mengurangi stock {kode} : {e}")
            return False
        finally:
            connection.close()
    return False

def mencari_item(kode:str):
    """Fungsi mencari item secara spesifik berdasarkan kode_item"""
    connection=create_Connection()
    if connection is not None:
        try:
            # connection.row_factory=sqlite3.Row 
            kursor=connection.cursor()
            query="SELECT * FROM item WHERE kode_item=(?)"
            kursor.execute(query,(kode,))
            output=kursor.fetchone()
            if output:
                return output
            else:
                return None
        except sqlite3.Error as e:
            print(f"Gagal melakukan pencarian : {e}")
            return None
        finally:
            connection.close()
    return None

if __name__=="__main__":
    # products=get_all_item()
    # menampilkan_item(products)
    x=mencari_item("S0001")
    