import sqlite3
import uuid
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

def mencari_item_kode(kode:str):
    """Fungsi mencari item secara spesifik berdasarkan kode_item"""
    connection=create_Connection()
    if connection is not None:
        try:
            connection.row_factory=sqlite3.Row 
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

def mencari_item_name(item_name:str):
    """Fungsi mencari item secara spesifik berdasarkan nama_item"""
    connection=create_Connection()
    if connection is not None:
        try:
            connection.row_factory=sqlite3.Row
            kursor=connection.cursor()
            query="SELECT * FROM item WHERE nama_item=(?)"
            kursor.execute(query,(item_name,))
            output=kursor.fetchone()
            if output:
                return output
            else :
                return None
        except sqlite3.Error as e:
            print(f"Gagal melakukan pencarian : {e}")
            return None
        finally:
            if connection:
                connection.close()
    return

def mencari_item_kategori(kategori_name:str):
    """Fungsi untuk mencari item berdasarkan kategori"""
    connection=create_Connection()
    if connection is not None:
        try:
            connection.row_factory=sqlite3.Row
            kursor=connection.cursor()
            query="SELECT * FROM item WHERE nama_item LIKE ?"
            item=f'%{kategori_name}%'
            kursor.execute(query,(item,))
            output=kursor.fetchall()
            if output:
                return output
            else:
                return []
        except sqlite3.Error as e:
            print(f"Gagal melakukan pencarian : {e}")
            return []
        finally:
            if connection:
                connection.close()
    return []
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
            connection.row_factory=sqlite3.Row 
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
            
def create_new_transaction(data_transaksi:tuple):
    """Fungsi untuk membuat transaksi : akan mengisi table transaksi dan detail transaksi"""
    connection=create_Connection()
    if not connection:
        print("Gagal membuat koneksi")
        return False,None
    
    try:
        data_umum,keranjang_item=data_transaksi
        id_user,total_nominal_transaksi,status_transaksi=data_umum
        kursor=connection.cursor()
        id_transaksi_baru=str(uuid.uuid4())
        query_transaksi="INSERT INTO transaksi(id_transaksi,total_nominal_transaksi,id_user,status_transaksi) VALUES (?,?,?,?)"
        kursor.execute(query_transaksi,(id_transaksi_baru,total_nominal_transaksi,id_user,status_transaksi,))
        query_detail="INSERT INTO detail_transaksi(id_transaksi,id_item,jumlah_item,nominal_saat_transaksi) VALUES (?,?,?,?)"
        query_stok="UPDATE item SET stock_item=stock_item-(?) WHERE id_item=(?) AND stock_item>=(?)"

        for item in keranjang_item:
            id_item,jumlah_item,nominal_saat_transaksi=item
            kursor.execute(query_detail,(id_transaksi_baru,id_item,jumlah_item,nominal_saat_transaksi))
            kursor.execute(query_stok,(jumlah_item,id_item,jumlah_item))
            if kursor.rowcount==0:
                raise sqlite3.Error(f"stok untuk item {id_item} tidak mencukupi")

        connection.commit()
        print(f"Transaksi {id_transaksi_baru} berhasil dibuat")
        return True, id_transaksi_baru
    except sqlite3.Error as e:
        print(f"Terjadi kesalahan, transaksi gagal : {e}")
        connection.rollback()
        return False, None
    finally:
        if connection:
            connection.close()
    


