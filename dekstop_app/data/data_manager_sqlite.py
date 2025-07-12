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
            if connection:
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

            if kursor.rowcount>0:
                print(f"Item {nama} berhasil ditambahkan")
                return True
            else:
                print(f"Gagal menambahkan item {nama}")
                return False
        except sqlite3.IntegrityError:
            print(f"Error: Kode item {kode} sudah ada di database. Gunakan kode lain")
            return False
        except sqlite3.Error as e:
            print(f"Error saat menambahkan item : {e}")
            return False
        finally :
            if connection:
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
            if kursor.rowcount>0:
                print(f"Item dengan kode {kode} berhasil dihapus")
                return True
            else:
                print(f"Gagal menghapus item {kode}")
                return False
            
        except sqlite3.Error as e:
            print(f"Error saat menghapus item : {e}")
            return False
        finally:
            if connection:
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
            if kursor.rowcount>0:
                print(f"Berhasil menambahkan stock item dengan kode {kode} sebanyak {sum}")
                return True
            else:
                print(f"Gagal menambahkan stock item dengan kode {kode} sebanyak ")
                return False
        except sqlite3.Error as e:
            print(f"Error saat menambahkan stock {kode} : {e}")
            return False
        finally:
            if connection:
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
            if connection:
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
            if connection:
                connection.close()
    return None

def add_user(username:str,hashed_password:bytes,role:str):
    """Fungsi untuk menambahkan user ke database"""
    connection=create_Connection()
    if connection is not None:
        try:
            kursor=connection.cursor()
            query= "INSERT INTO user(user_name,hash_password,role) VALUES (?,?,?)"
            kursor.execute(query,(username,hashed_password,role))
            print(f"Berhasil menambahkan {username} ke database")
            connection.commit()
            if kursor.rowcount>0:
                print(f"Berhasil menambahkan user dengan username {username}")
                return True
            else:
                print(f"Gagal menambahkan user dengan username {username}")
                return False
        except sqlite3.IntegrityError:
            print(f"Error : username {username} sudah digunakan")
        except sqlite3.Error as e:
            print(f"Gagal menambahkan {username} ke database : {e}")
            return False
        finally:
            if connection:
                connection.close()
    return False

def cari_user(username:str):
    connection=create_Connection()
    if connection is not None:
        try:
            kursor=connection.cursor()
            query="SELECT * FROM user WHERE user_name=(?)"
            kursor.execute(query,(username,))
            output=kursor.fetchone()
            if output:
                return output
            else:
                return None
        except sqlite3.Error as e:
            print(f"Tidak dapat menemukan {username} : {e}")
            return None
        finally:
            if connection:
                connection.close()
    return None
            
def create_new_transaction(transaksi:list):
    connection=create_Connection()
    if connection is not None:
        try:
            kursor=connection.cursor()
            id_transaksi,timestamp_transaksi,total_nominal_transaksi,id_user,status_transaksi=transaksi
            query_1=""
            return
        except:
            return 
    return


