
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os


# ==========================================================
# 1. MENENTUKAN FOLDER
# ==========================================================

script_folder = os.path.dirname(
    os.path.abspath(__file__)
)

hasil_folder = os.path.join(
    script_folder,
    "HASIL_THRESHOLDING"
)


# ==========================================================
# 2. NAMA FILE HASIL THRESHOLDING
# ==========================================================

nama_dasar = (
    "0a64655c-4052-4e5f-a696-2a6cf25d10c9"
    "___GCREC_Bact.Sp 6017"
)

file_binary = (
    "binary_thresholding_"
    + nama_dasar
    + ".png"
)

file_multi = (
    "multi_thresholding_"
    + nama_dasar
    + ".png"
)

file_otsu = (
    "otsu_thresholding_"
    + nama_dasar
    + ".png"
)


# ==========================================================
# 3. MEMBUAT PATH FILE
# ==========================================================

path_binary = os.path.join(
    hasil_folder,
    file_binary
)

path_multi = os.path.join(
    hasil_folder,
    file_multi
)

path_otsu = os.path.join(
    hasil_folder,
    file_otsu
)


# ==========================================================
# 4. MEMERIKSA KEBERADAAN FILE
# ==========================================================

print("=" * 60)
print("          PERBANDINGAN THRESHOLDING")
print("=" * 60)

daftar_file = {
    "Binary Thresholding": path_binary,
    "Multi Thresholding": path_multi,
    "Otsu Thresholding": path_otsu
}

for nama_metode, path in daftar_file.items():

    if not os.path.isfile(path):
        print(f"\nFile {nama_metode} tidak ditemukan:")
        print(path)
        print(
            "\nPastikan ketiga program thresholding "
            "sudah dijalankan."
        )
        raise SystemExit

print("Semua file hasil thresholding ditemukan.")
print()


# ==========================================================
# 5. MEMBACA HASIL THRESHOLDING
# ==========================================================

binary = Image.open(
    path_binary
).convert("L")

multi = Image.open(
    path_multi
).convert("L")

otsu = Image.open(
    path_otsu
).convert("L")


# Mengubah citra menjadi array NumPy
binary_array = np.array(binary)
multi_array = np.array(multi)
otsu_array = np.array(otsu)


# Memastikan ukuran citra sama
if not (
    binary_array.shape ==
    multi_array.shape ==
    otsu_array.shape
):
    print("Ukuran citra hasil thresholding berbeda.")
    print("Binary:", binary_array.shape)
    print("Multi :", multi_array.shape)
    print("Otsu  :", otsu_array.shape)
    raise SystemExit


# ==========================================================
# 6. FUNGSI MENGHITUNG PIXEL BINARY DAN OTSU
# ==========================================================

def hitung_binary(citra):

    jumlah_hitam = np.sum(citra == 0)
    jumlah_putih = np.sum(citra == 255)

    total_pixel = citra.size

    persen_hitam = (
        jumlah_hitam / total_pixel
    ) * 100

    persen_putih = (
        jumlah_putih / total_pixel
    ) * 100

    return {
        "hitam": int(jumlah_hitam),
        "putih": int(jumlah_putih),
        "abu": 0,
        "persen_hitam": persen_hitam,
        "persen_abu": 0.0,
        "persen_putih": persen_putih
    }


# ==========================================================
# 7. FUNGSI MENGHITUNG PIXEL MULTI THRESHOLDING
# ==========================================================

def hitung_multi(citra):

    jumlah_hitam = np.sum(citra == 0)
    jumlah_abu = np.sum(citra == 127)
    jumlah_putih = np.sum(citra == 255)

    total_pixel = citra.size

    persen_hitam = (
        jumlah_hitam / total_pixel
    ) * 100

    persen_abu = (
        jumlah_abu / total_pixel
    ) * 100

    persen_putih = (
        jumlah_putih / total_pixel
    ) * 100

    return {
        "hitam": int(jumlah_hitam),
        "abu": int(jumlah_abu),
        "putih": int(jumlah_putih),
        "persen_hitam": persen_hitam,
        "persen_abu": persen_abu,
        "persen_putih": persen_putih
    }


# ==========================================================
# 8. MENGHITUNG DISTRIBUSI PIXEL
# ==========================================================

hasil_binary = hitung_binary(
    binary_array
)

hasil_multi = hitung_multi(
    multi_array
)

hasil_otsu = hitung_binary(
    otsu_array
)


# ==========================================================
# 9. MENAMPILKAN HASIL BINARY THRESHOLDING
# ==========================================================

print("-" * 60)
print("BINARY THRESHOLDING")
print("-" * 60)

print("Pixel hitam  :", hasil_binary["hitam"])
print("Pixel putih  :", hasil_binary["putih"])

print(
    f"Persen hitam : "
    f'{hasil_binary["persen_hitam"]:.2f}%'
)

print(
    f"Persen putih : "
    f'{hasil_binary["persen_putih"]:.2f}%'
)


# ==========================================================
# 10. MENAMPILKAN HASIL MULTI THRESHOLDING
# ==========================================================

print()
print("-" * 60)
print("MULTI THRESHOLDING")
print("-" * 60)

print("Pixel hitam   :", hasil_multi["hitam"])
print("Pixel abu-abu :", hasil_multi["abu"])
print("Pixel putih   :", hasil_multi["putih"])

print(
    f'Persen hitam  : '
    f'{hasil_multi["persen_hitam"]:.2f}%'
)

print(
    f'Persen abu-abu: '
    f'{hasil_multi["persen_abu"]:.2f}%'
)

print(
    f'Persen putih  : '
    f'{hasil_multi["persen_putih"]:.2f}%'
)


# ==========================================================
# 11. MENAMPILKAN HASIL OTSU THRESHOLDING
# ==========================================================

print()
print("-" * 60)
print("OTSU THRESHOLDING")
print("-" * 60)

print("Pixel hitam  :", hasil_otsu["hitam"])
print("Pixel putih  :", hasil_otsu["putih"])

print(
    f'Persen hitam : '
    f'{hasil_otsu["persen_hitam"]:.2f}%'
)

print(
    f'Persen putih : '
    f'{hasil_otsu["persen_putih"]:.2f}%'
)


# ==========================================================
# 12. TABEL PERBANDINGAN
# ==========================================================

print()
print("=" * 70)
print("                    TABEL PERBANDINGAN")
print("=" * 70)

print(
    f"{'Metode':<20}"
    f"{'Hitam (%)':>12}"
    f"{'Abu-abu (%)':>15}"
    f"{'Putih (%)':>12}"
)

print("-" * 70)

for nama, data in [
    ("Binary", hasil_binary),
    ("Multi", hasil_multi),
    ("Otsu", hasil_otsu)
]:

    print(
        f"{nama:<20}"
        f'{data["persen_hitam"]:>12.2f}'
        f'{data["persen_abu"]:>15.2f}'
        f'{data["persen_putih"]:>12.2f}'
    )

print("=" * 70)


# ==========================================================
# 13. VISUALISASI PERBANDINGAN CITRA
# ==========================================================

plt.figure(
    figsize=(15, 5)
)

# Binary Thresholding
plt.subplot(1, 3, 1)

plt.imshow(
    binary_array,
    cmap="gray",
    vmin=0,
    vmax=255
)

plt.title(
    "Binary Thresholding"
)

plt.axis("off")


# Multi Thresholding
plt.subplot(1, 3, 2)

plt.imshow(
    multi_array,
    cmap="gray",
    vmin=0,
    vmax=255
)

plt.title(
    "Multi Thresholding"
)

plt.axis("off")


# Otsu Thresholding
plt.subplot(1, 3, 3)

plt.imshow(
    otsu_array,
    cmap="gray",
    vmin=0,
    vmax=255
)

plt.title(
    "Otsu Thresholding"
)

plt.axis("off")


plt.suptitle(
    "Perbandingan Hasil Thresholding"
)

plt.tight_layout()
plt.show()


# ==========================================================
# 14. GRAFIK DISTRIBUSI PIXEL
# ==========================================================

metode = [
    "Binary",
    "Multi",
    "Otsu"
]

persen_hitam = [
    hasil_binary["persen_hitam"],
    hasil_multi["persen_hitam"],
    hasil_otsu["persen_hitam"]
]

persen_abu = [
    hasil_binary["persen_abu"],
    hasil_multi["persen_abu"],
    hasil_otsu["persen_abu"]
]

persen_putih = [
    hasil_binary["persen_putih"],
    hasil_multi["persen_putih"],
    hasil_otsu["persen_putih"]
]

x = np.arange(len(metode))
lebar = 0.25

plt.figure(
    figsize=(10, 5)
)

plt.bar(
    x - lebar,
    persen_hitam,
    lebar,
    label="Hitam"
)

plt.bar(
    x,
    persen_abu,
    lebar,
    label="Abu-abu"
)

plt.bar(
    x + lebar,
    persen_putih,
    lebar,
    label="Putih"
)

plt.xticks(
    x,
    metode
)

plt.xlabel(
    "Metode Thresholding"
)

plt.ylabel(
    "Persentase Piksel (%)"
)

plt.title(
    "Perbandingan Distribusi Intensitas Piksel"
)

plt.legend()
plt.tight_layout()
plt.show()


# ==========================================================
# 15. SELESAI
# ==========================================================

print()
print("=" * 60)
print("          PERBANDINGAN SELESAI")
print("=" * 60)
