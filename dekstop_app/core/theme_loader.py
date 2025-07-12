from pathlib import Path

def load_theme(theme:str):
    """Fungsi untuk menemukan file qss dan load theme"""
    base_dir=Path(__file__).resolve().parent.parent
    theme_path=base_dir/"assets"/"themes"/theme

    if not theme_path.is_file():
        print(f"Peringatan: Berkas tema tidak ditemukan di {theme_path}")
        return ""
    try:
        with open(theme_path,"r") as f:
            stylesheet=f.read()
        return stylesheet
    except Exception as e:
        print(f"Gagal membaca berkas tema {theme_path}. Kesalahan : {e}")
        return ""