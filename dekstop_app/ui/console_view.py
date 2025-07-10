def menampilkan_banyak_item(database:list):
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

def menampilkan_satu_item(database:tuple):
    """Fungsi untuk menampilkan satu item"""
    if(database):
        print(database)
        return True
    else:
        print("Item tersebu tidak dapat ditemukan")
    return False