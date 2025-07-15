from data import cari_user,add_user,mencari_item_kode
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
            return {"id":user_id, "username":user_name, "role":role}
        else:
            print("Password Anda salah")
            return None
    print("Tidak dapat menemukan akun dengan username tersebut")    
    return None

def mencari_item_kode_logic(kode:str):
    """Mencari item menggunakan kode_item"""
    item=mencari_item_kode(kode)
    return item