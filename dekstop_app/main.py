from data import data_manager_sqlite as db
from ui import console_view as view

def main():
    """Fungsi main untuk melakukan testing"""
    item=db.mencari_item("S0001")
    if item:
        view.menampilkan_satu_item(item)
    else:
        print("Item dengan kode tersebut tidak ditemukan.")
if __name__=="__main__":
    main()

    