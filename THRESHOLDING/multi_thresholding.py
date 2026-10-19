
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# ==========================================
# LOKASI FOLDER
# ==========================================
script_folder = os.path.dirname(
    os.path.abspath(__file__)
)

project_folder = os.path.dirname(
    script_folder
)

dataset_folder = os.path.join(
    project_folder,
    "DATASET GAMBAR 1",
    "Images"
)

output_folder = os.path.join(
    script_folder,
    "HASIL_THRESHOLDING"
)

os.makedirs(
    output_folder,
    exist_ok=True
)

# ==========================================
# NAMA GAMBAR INPUT
# ==========================================
input_filename = (
    "0a64655c-4052-4e5f-a696-2a6cf25d10c9"
    "___GCREC_Bact.Sp 6017.JPG"
)

image_path = os.path.join(
    dataset_folder,
    input_filename
)

# ==========================================
# INFORMASI AWAL
# ==========================================
print("==========================================")
print("           MULTI THRESHOLDING")
print("==========================================")

print("Lokasi gambar:")
print(image_path)
print()

# ==========================================
# MEMERIKSA FILE GAMBAR
# ==========================================
if not os.path.isfile(image_path):

    print("GAMBAR TIDAK DITEMUKAN!")
    print()
    print("Pastikan nama file sesuai:")
    print(input_filename)

    raise SystemExit

# ==========================================
# MEMBACA GAMBAR
# ==========================================
img = cv2.imread(image_path)

if img is None:

    print("Gambar gagal dibaca!")

    raise SystemExit

print("Gambar berhasil dibaca!")
print()

# ==========================================
# KONVERSI CITRA MENJADI GRAYSCALE
# ==========================================
gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

# ==========================================
# MENENTUKAN NILAI MULTI THRESHOLDING
# ==========================================
T1 = 80
T2 = 160

# ==========================================
# PROSES MULTI THRESHOLDING
# ==========================================
# Intensitas <= T1       : 0 (hitam)
# T1 < intensitas <= T2  : 127 (abu-abu)
# Intensitas > T2        : 255 (putih)

multi = np.zeros_like(gray)

multi[gray <= T1] = 0

multi[
    (gray > T1) &
    (gray <= T2)
] = 127

multi[gray > T2] = 255

# ==========================================
# MENYIMPAN HASIL
# ==========================================
output_filename = (
    "multi_thresholding_"
    + os.path.splitext(input_filename)[0]
    + ".png"
)

output_path = os.path.join(
    output_folder,
    output_filename
)

berhasil = cv2.imwrite(
    output_path,
    multi
)

if not berhasil:

    print("Gagal menyimpan hasil Multi Thresholding!")

    raise SystemExit

# ==========================================
# MENAMPILKAN INFORMASI HASIL
# ==========================================
print("==========================================")
print("       HASIL MULTI THRESHOLDING")
print("==========================================")

print("File gambar   :", input_filename)
print("Operasi       : Multi Thresholding")
print("Threshold 1   :", T1)
print("Threshold 2   :", T2)
print("Nilai keluaran: 0, 127, 255")
print("Hasil disimpan:", os.path.abspath(output_path))

print("==========================================")

# ==========================================
# KONVERSI BGR MENJADI RGB UNTUK VISUALISASI
# ==========================================
img_rgb = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2RGB
)

# ==========================================
# VISUALISASI CITRA
# ==========================================
plt.figure(
    figsize=(15, 5)
)

# Citra awal
plt.subplot(1, 3, 1)

plt.imshow(img_rgb)

plt.title(
    "Citra Awal"
)

plt.axis("off")

# Citra grayscale
plt.subplot(1, 3, 2)

plt.imshow(
    gray,
    cmap="gray",
    vmin=0,
    vmax=255
)

plt.title(
    "Citra Grayscale"
)

plt.axis("off")

# Hasil Multi Thresholding
plt.subplot(1, 3, 3)

plt.imshow(
    multi,
    cmap="gray",
    vmin=0,
    vmax=255
)

plt.title(
    f"Multi Thresholding\nT1 = {T1}, T2 = {T2}"
)

plt.axis("off")

plt.suptitle(
    "Hasil Pengolahan Citra dengan Multi Thresholding"
)

plt.tight_layout()

plt.show()

# ==========================================
# SELESAI
# ==========================================
print()
print("==========================================")
print("     MULTI THRESHOLDING BERHASIL")
print("==========================================")
