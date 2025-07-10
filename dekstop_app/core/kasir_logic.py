from data import data_manager_sqlite as db
import bcrypt

def register_new_user(username:str,password:str,role:str):
    """Fungsi untuk menambahkan user yang akan ditambahkan ke databse"""
    if len(password)<8:
        print("Error : password minimal 8")
        return False
    
    password_bytes=password.encode('utf-8')
    salt=bcrypt.gensalt()
    hasil_hashed=bcrypt.hashpw(password_bytes,salt)
    
    connection=db.add_user(username,hasil_hashed,role)
    return connection