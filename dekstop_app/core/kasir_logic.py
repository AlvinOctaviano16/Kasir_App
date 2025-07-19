from data import cari_user,add_user,mencari_item_kode,create_new_transaction
import bcrypt

def register_new_user(username:str,password:str,role:str):
    """Fungsi untuk membuat user yang akan ditambahkan ke databse"""
    if len(password)<8:
        print("Error : password minimal 8")
        return False
    
    password_bytes=password.encode('utf-8')
    salt=bcrypt.gensalt()
    hasil_hashed=bcrypt.hashpw(password_bytes,salt)

    connection=add_user(username,hasil_hashed,role)
    return connection

def verifikasi_login(username:str,password:str):
    """Fungsi untuk login"""
    user_data=cari_user(username)
    if user_data:
        user_id,user_name,hash_password,role=user_data
        password_bytes=password.encode('utf-8')
        if bcrypt.checkpw(password_bytes,hash_password):
            print("Berhasil melakukan login")
            return {"id_user":user_id, "nama_user":user_name, "role":role}
        else:
            print("Password Anda salah")
            return None
    print("Tidak dapat menemukan akun dengan username tersebut")    
    return None

def mencari_item_kode_logic(kode:str):
    """Mencari item menggunakan kode_item"""
    item=mencari_item_kode(kode)
    return item

def proses_transaksi(id_user:int,keranjang:list,total_nominal_transaksi:int):
    """Fungsi logika , bagaimana logika penjualan saat transaksi dilakukan"""
    if not keranjang:
        return False, "Keranjang belanja kosong"
    

    try:
        # if data_transaksi is not None:
        database=[
            (item['id_item'],item['kode_item'],item['nama_item'],item['jumlah_item'],item['nominal_saat_transaksi'])
            for item in keranjang
        ]
        data_umum=(id_user,total_nominal_transaksi, "Selesai")
        data_transaksi=(data_umum,database)
        success,id_transaksi=create_new_transaction(data_transaksi)
        if success:
            print(f"Logika: Penjualan berhasil diproses dengan ID: {id_transaksi}")
            return True, id_transaksi
        else:
            print("Logika: Penjualan gagal diproses oleh database.")
            return False,"Gagal menyimpan transaksi."
    except Exception as e:
        print(f"Logik : Terjadi exception tak terduga {e}")
        return False, "Terjadi kesalahan sistem"
        