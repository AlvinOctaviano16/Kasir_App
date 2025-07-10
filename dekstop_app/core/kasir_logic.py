from data import data_manager_sqlite as db
import bcrypt

def register_new_user(username:str,password:str,role:str):
    """Fungsi untuk membuat user yang akan ditambahkan ke databse"""
    if len(password)<8:
        print("Error : password minimal 8")
        return False
    
    password_bytes=password.encode('utf-8')
    salt=bcrypt.gensalt()
    hasil_hashed=bcrypt.hashpw(password_bytes,salt)

    connection=db.add_user(username,hasil_hashed,role)
    return connection

def verifikasi_login(username:str,password:str):
    """Fungsi untuk login"""
    user_data=db.cari_user(username)
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