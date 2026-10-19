
from PIL import Image
import matplotlib.pyplot as plt
import os

# ==========================================
# LOKASI GAMBAR INPUT
# ==========================================
# Folder utama: C:\PENGOLAHAN-CITRA
folder_utama = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Lokasi folder dataset
dataset_folder = os.path.join(
    folder_utama,
    "DATASET GAMBAR 1",
    "Images"
)

# Nama gambar yang sama dengan Grayscale
file_gambar = (
    "0a64655c-4052-4e5f-a696-2a6cf25d10c9"
    "___GCREC_Bact.Sp 6017.JPG"
)

path_gambar = os.path.join(
    dataset_folder,
    file_gambar
)

# ==========================================
# FOLDER UNTUK MENYIMPAN HASIL
# ==========================================
folder_output = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "HASIL_THRESHOLDING"
)

os.makedirs(
    folder_output,
    exist_ok=True
)

# ==========================================
# MEMERIKSA DAN MEMBACA GAMBAR
# ==========================================
if not os.path.isfile(path_gambar):

    print("Gambar tidak ditemukan!")
    print(f"Lokasi yang dicari: {path_gambar}")

    # Menampilkan nama file yang tersedia
    if os.path.isdir(dataset_folder):

        print("\nContoh file dalam folder Images:")

        for nama in os.listdir(dataset_folder)[:10]:
            print(nama)

    else:
        print(
            f"Folder dataset tidak ditemukan: {dataset_folder}"
        )

    raise SystemExit

try:
    image = Image.open(
        path_gambar
    ).convert("RGB")

except Exception as error:
    print(f"Gagal membaca gambar: {error}")
    raise SystemExit

# ==========================================
# KONVERSI CITRA MENJADI GRAYSCALE
# ==========================================
grayscale = image.convert("L")

# ==========================================
# MENGHITUNG HISTOGRAM CITRA GRAYSCALE
# ==========================================
histogram = grayscale.histogram()

total_pixel = (
    grayscale.width *
    grayscale.height
)

# Menghitung total intensitas seluruh piksel
jumlah_intensitas_total = sum(
    intensitas * histogram[intensitas]
    for intensitas in range(256)
)

# ==========================================
# INISIALISASI PERHITUNGAN OT SU THRESHOLDING
# ==========================================
jumlah_background = 0
jumlah_intensitas_background = 0

nilai_threshold_otsu = 0
nilai_variansi_maksimum = -1

# ==========================================
# MENENTUKAN THRESHOLD OT SU SECARA MANUAL
# ==========================================
# Kelas 0 : intensitas <= threshold
# Kelas 1 : intensitas > threshold

for t in range(256):

    # Menambahkan piksel intensitas t ke kelas background
    jumlah_background += histogram[t]

    jumlah_intensitas_background += (
        t * histogram[t]
    )

    # Jika kelas background kosong, lewati
    if jumlah_background == 0:
        continue

    # Menghitung jumlah piksel foreground
    jumlah_foreground = (
        total_pixel -
        jumlah_background
    )

    # Jika kelas foreground kosong, lewati
    if jumlah_foreground == 0:
        continue

    # Menghitung jumlah intensitas foreground
    jumlah_intensitas_foreground = (
        jumlah_intensitas_total -
        jumlah_intensitas_background
    )

    # Menghitung rata-rata intensitas setiap kelas
    mean_background = (
        jumlah_intensitas_background /
        jumlah_background
    )

    mean_foreground = (
        jumlah_intensitas_foreground /
        jumlah_foreground
    )

    # Menghitung probabilitas setiap kelas
    probabilitas_background = (
        jumlah_background /
        total_pixel
    )

    probabilitas_foreground = (
        jumlah_foreground /
        total_pixel
    )

    # Menghitung variansi antarkelas
    variansi_antar_kelas = (
        probabilitas_background *
        probabilitas_foreground *
        (
            mean_background -
            mean_foreground
        ) ** 2
    )

    # Memilih threshold dengan variansi terbesar
    if variansi_antar_kelas > nilai_variansi_maksimum:

        nilai_variansi_maksimum = (
            variansi_antar_kelas
        )

        nilai_threshold_otsu = t

# Nilai threshold optimal
threshold = nilai_threshold_otsu

# ==========================================
# PROSES BINARISASI CITRA
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

        # Intensitas <= threshold menjadi hitam
        if nilai_pixel <= threshold:
            hasil_pixels[x, y] = 0

        # Intensitas > threshold menjadi putih
        else:
            hasil_pixels[x, y] = 255

# ==========================================
# MENYIMPAN HASIL OT SU THRESHOLDING
# ==========================================
nama_file = os.path.splitext(
    os.path.basename(path_gambar)
)[0]

nama_hasil = (
    "otsu_thresholding_" +
    nama_file +
    ".png"
)

path_hasil = os.path.join(
    folder_output,
    nama_hasil
)

try:
    hasil.save(
        path_hasil,
        format="PNG"
    )

except Exception as error:
    print(f"Gagal menyimpan hasil: {error}")
    raise SystemExit

# ==========================================
# MENAMPILKAN INFORMASI HASIL
# ==========================================
print("=" * 55)
print("             OTSU THRESHOLDING")
print("=" * 55)

print(f"File gambar       : {os.path.basename(path_gambar)}")
print(f"Ukuran citra      : {grayscale.width} x {grayscale.height}")
print(f"Total piksel      : {total_pixel}")
print(f"Nilai threshold   : {threshold}")
print(f"Variansi maksimum : {nilai_variansi_maksimum:.4f}")
print("Penentuan threshold: Otomatis")
print(f"Hasil disimpan    : {os.path.abspath(path_hasil)}")

print("=" * 55)

# ==========================================
# VISUALISASI CITRA ASLI, GRAYSCALE,
# DAN HASIL OT SU THRESHOLDING
# ==========================================
plt.figure(
    figsize=(15, 5)
)

# Citra asli
plt.subplot(1, 3, 1)

plt.imshow(image)

plt.title(
    "Citra Awal"
)

plt.axis("off")

# Citra grayscale
plt.subplot(1, 3, 2)

plt.imshow(
    grayscale,
    cmap="gray",
    vmin=0,
    vmax=255
)

plt.title(
    "Citra Grayscale"
)

plt.axis("off")

# Hasil Otsu
plt.subplot(1, 3, 3)

plt.imshow(
    hasil,
    cmap="gray",
    vmin=0,
    vmax=255
)

plt.title(
    f"Otsu Thresholding\nT = {threshold}"
)

plt.axis("off")

plt.suptitle(
    "Perbandingan Citra Sebelum dan Sesudah Otsu Thresholding"
)

plt.tight_layout()

plt.show()

# ==========================================
# VISUALISASI HISTOGRAM DAN THRESHOLD
# ==========================================
plt.figure(
    figsize=(10, 5)
)

plt.bar(
    range(256),
    histogram,
    width=1
)

plt.axvline(
    threshold,
    linestyle="--",
    linewidth=2,
    label=f"Threshold Otsu = {threshold}"
)

plt.title(
    "Histogram Citra Grayscale"
)

plt.xlabel(
    "Intensitas Piksel"
)

plt.ylabel(
    "Jumlah Piksel"
)

plt.xlim(
    0,
    255
)

plt.legend()

plt.tight_layout()

plt.show()

# ==========================================
# SELESAI
# ==========================================
print()

print("=" * 55)
print("       OTSU THRESHOLDING SELESAI")
print("=" * 55)
