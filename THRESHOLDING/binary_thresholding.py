
from PIL import Image
import matplotlib.pyplot as plt
import os

# ==========================================
# LOKASI FOLDER
# ==========================================
folder_utama = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

dataset_folder = os.path.join(
    folder_utama,
    "DATASET GAMBAR 1",
    "Images"
)

hasil_folder = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "HASIL_THRESHOLDING"
)

os.makedirs(hasil_folder, exist_ok=True)

# ==========================================
# NAMA GAMBAR INPUT
# ==========================================
file_gambar = (
    "0a64655c-4052-4e5f-a696-2a6cf25d10c9"
    "___GCREC_Bact.Sp 6017.JPG"
)

path_gambar = os.path.join(
    dataset_folder,
    file_gambar
)

# ==========================================
# MEMERIKSA GAMBAR
# ==========================================
if not os.path.exists(path_gambar):
    print(f"Gambar {file_gambar} tidak ditemukan.")
    print(f"Lokasi yang dicari: {path_gambar}")
    exit()

# ==========================================
# MEMBACA GAMBAR
# ==========================================
image = Image.open(
    path_gambar
).convert("RGB")

# ==========================================
# KONVERSI CITRA GRAYSCALE
# ==========================================
grayscale = image.convert("L")

# ==========================================
# MENENTUKAN NILAI THRESHOLD
# ==========================================
threshold = 128

# ==========================================
# PROSES BINARY THRESHOLDING
# ==========================================
hasil = Image.new(
    "L",
    grayscale.size
)

pixels_grayscale = grayscale.load()
hasil_pixels = hasil.load()

for y in range(grayscale.height):
    for x in range(grayscale.width):

        nilai_pixel = pixels_grayscale[x, y]

        if nilai_pixel >= threshold:
            hasil_pixels[x, y] = 255
        else:
            hasil_pixels[x, y] = 0

# ==========================================
# MENYIMPAN HASIL
# ==========================================
nama_file = os.path.splitext(file_gambar)[0]

nama_hasil = (
    "binary_thresholding_"
    + nama_file
    + ".png"
)

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(output_file, format="PNG")

# ==========================================
# MENAMPILKAN INFORMASI
# ==========================================
print("------------------------------------------")
print(f"File gambar      : {file_gambar}")
print("Operasi          : Binary Thresholding")
print(f"Nilai threshold  : {threshold}")
print(f"Hasil disimpan   : {os.path.abspath(output_file)}")
print("------------------------------------------")

# ==========================================
# VISUALISASI CITRA
# ==========================================
plt.figure(figsize=(15, 4))

# Citra awal
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Citra Awal")
plt.axis("off")

# Citra grayscale
plt.subplot(1, 3, 2)
plt.imshow(grayscale, cmap="gray", vmin=0, vmax=255)
plt.title("Citra Grayscale")
plt.axis("off")

# Hasil binary thresholding
plt.subplot(1, 3, 3)
plt.imshow(hasil, cmap="gray", vmin=0, vmax=255)
plt.title(f"Binary Thresholding\nT = {threshold}")
plt.axis("off")

plt.suptitle("Binary Thresholding")
plt.tight_layout()
plt.show()

# ==========================================
# SELESAI
# ==========================================
print()
print("==========================================")
print("      BINARY THRESHOLDING SELESAI")
print("==========================================")
