import os
import csv
import numpy as np
from PIL import Image

# Lokasi folder program
folder_program = os.path.dirname(os.path.abspath(__file__))

# Lokasi folder utama TUGAS 1
folder_utama = os.path.dirname(folder_program)

# Lokasi gambar input
path_gambar = os.path.join(
    folder_utama,
    "DATASET GAMBAR 1",
    "Images",
    "0a64655c-4052-4e5f-a696-2a6cf25d10c9___GCREC_Bact.Sp 6017.JPG"
)

# Lokasi folder hasil
folder_output = os.path.join(
    folder_program,
    "HASIL_EKSTRAKSI FITUR"
)

# Membuat folder hasil jika belum tersedia
os.makedirs(folder_output, exist_ok=True)

# ==========================================
# 2. MEMBACA GAMBAR
# ==========================================

if not os.path.exists(path_gambar):
    raise FileNotFoundError(
        f"Gambar tidak ditemukan: {path_gambar}"
    )

gambar = Image.open(path_gambar).convert("RGB")

# Mengubah gambar menjadi array NumPy
data_gambar = np.array(gambar, dtype=np.float64)

print("======================================")
print("EKSTRAKSI FITUR WARNA - COLOR MOMENTS")
print("======================================")
print(f"Nama gambar : {os.path.basename(path_gambar)}")
print(f"Ukuran      : {gambar.size}")
print(f"Mode warna  : {gambar.mode}")


# ==========================================
# 3. MEMISAHKAN KANAL RGB
# ==========================================

kanal_r = data_gambar[:, :, 0].flatten()
kanal_g = data_gambar[:, :, 1].flatten()
kanal_b = data_gambar[:, :, 2].flatten()

kanal_warna = {
    "Red": kanal_r,
    "Green": kanal_g,
    "Blue": kanal_b
}


# ==========================================
# 4. FUNGSI PERHITUNGAN COLOR MOMENTS
# ==========================================

def hitung_color_moments(data):
    """
    Menghitung:
    1. Mean
    2. Standard Deviation
    3. Skewness
    """

    # Mean (rata-rata)
    mean = np.mean(data)

    # Standard Deviation (standar deviasi)
    std = np.std(data)

    # Skewness (kemencengan distribusi)
    if std == 0:
        skewness = 0.0
    else:
        skewness = np.mean(((data - mean) / std) ** 3)

    return mean, std, skewness


# ==========================================
# 5. EKSTRAKSI FITUR SETIAP KANAL RGB
# ==========================================

hasil_fitur = {}

for nama_kanal, data_kanal in kanal_warna.items():

    mean, std, skewness = hitung_color_moments(data_kanal)

    hasil_fitur[f"{nama_kanal}_Mean"] = mean
    hasil_fitur[f"{nama_kanal}_Std"] = std
    hasil_fitur[f"{nama_kanal}_Skewness"] = skewness


# ==========================================
# 6. MENAMPILKAN HASIL EKSTRAKSI
# ==========================================

print("\nHASIL EKSTRAKSI FITUR:")
print("--------------------------------------")

for nama_fitur, nilai in hasil_fitur.items():
    print(f"{nama_fitur:20s}: {nilai:.6f}")


# ==========================================
# 7. MENYIMPAN HASIL KE CSV
# ==========================================

nama_file = os.path.splitext(
    os.path.basename(path_gambar)
)[0]

path_csv = os.path.join(
    folder_output,
    f"hasil_color_moments_{nama_file}.csv"
)

# Menambahkan nama gambar dan label kelas
hasil_csv = {
    "Nama_Gambar": os.path.basename(path_gambar),
    **hasil_fitur,
    "Label": "Bacterial Spot"
}

with open(path_csv, mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=hasil_csv.keys()
    )

    writer.writeheader()
    writer.writerow(hasil_csv)


# ==========================================
# 8. INFORMASI HASIL
# ==========================================

print("\n======================================")
print("EKSTRAKSI FITUR SELESAI")
print("======================================")
print(f"Jumlah fitur : {len(hasil_fitur)}")
print(f"Hasil CSV    : {path_csv}")
print("======================================")
