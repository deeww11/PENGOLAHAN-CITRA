from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os


# ==========================================================
# 1. MENENTUKAN FOLDER
# ==========================================================

folder_utama = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

hasil_folder = os.path.join(
    folder_utama,
    "HASIL_THRESHOLDING"
)


# ==========================================================
# 2. NAMA FILE HASIL THRESHOLDING
# ==========================================================

file_binary = (
    "binary_thresholding_"
    "IMG_0230_JPG.rf.6aa737da228dfd6ab26b74bbcd84b98e.jpg"
)

file_multi = (
    "multi_thresholding_IMG_0230.png"
)

file_otsu = (
    "otsu_thresholding_"
    "IMG_0230_JPG.rf.6aa737da228dfd6ab26b74bbcd84b98e.jpg"
)


# ==========================================================
# 3. MEMBUAT PATH
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
# 4. CEK FILE
# ==========================================================

print("==============================================")
print("       PERBANDINGAN THRESHOLDING")
print("==============================================")

if not os.path.exists(path_binary):

    print("File Binary tidak ditemukan:")
    print(path_binary)
    exit()


if not os.path.exists(path_multi):

    print("File Multi tidak ditemukan:")
    print(path_multi)
    exit()


if not os.path.exists(path_otsu):

    print("File Otsu tidak ditemukan:")
    print(path_otsu)
    exit()


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


# Ubah menjadi array

binary_array = np.array(binary)

multi_array = np.array(multi)

otsu_array = np.array(otsu)


# ==========================================================
# 6. FUNGSI MENGHITUNG PIXEL BINARY / OTSU
# ==========================================================

def hitung_binary(citra):

    jumlah_hitam = np.sum(
        citra == 0
    )

    jumlah_putih = np.sum(
        citra == 255
    )

    total_pixel = (
        jumlah_hitam +
        jumlah_putih
    )

    persen_hitam = (
        jumlah_hitam /
        total_pixel
    ) * 100

    persen_putih = (
        jumlah_putih /
        total_pixel
    ) * 100

    return (
        jumlah_hitam,
        jumlah_putih,
        persen_hitam,
        persen_putih
    )


# ==========================================================
# 7. FUNGSI MENGHITUNG PIXEL MULTI
# ==========================================================

def hitung_multi(citra):

    jumlah_hitam = np.sum(
        citra == 0
    )

    jumlah_abu = np.sum(
        citra == 127
    )

    jumlah_putih = np.sum(
        citra == 255
    )

    total_pixel = (
        jumlah_hitam +
        jumlah_abu +
        jumlah_putih
    )

    persen_hitam = (
        jumlah_hitam /
        total_pixel
    ) * 100

    persen_abu = (
        jumlah_abu /
        total_pixel
    ) * 100

    persen_putih = (
        jumlah_putih /
        total_pixel
    ) * 100

    return (
        jumlah_hitam,
        jumlah_abu,
        jumlah_putih,
        persen_hitam,
        persen_abu,
        persen_putih
    )


# ==========================================================
# 8. PERHITUNGAN BINARY
# ==========================================================

(
    binary_hitam,
    binary_putih,
    binary_persen_hitam,
    binary_persen_putih
) = hitung_binary(
    binary_array
)


# ==========================================================
# 9. PERHITUNGAN MULTI
# ==========================================================

(
    multi_hitam,
    multi_abu,
    multi_putih,
    multi_persen_hitam,
    multi_persen_abu,
    multi_persen_putih
) = hitung_multi(
    multi_array
)


# ==========================================================
# 10. PERHITUNGAN OTSU
# ==========================================================

(
    otsu_hitam,
    otsu_putih,
    otsu_persen_hitam,
    otsu_persen_putih
) = hitung_binary(
    otsu_array
)


# ==========================================================
# 11. MENAMPILKAN HASIL PERHITUNGAN
# ==========================================================

print("----------------------------------------------")
print("BINARY THRESHOLDING")
print("----------------------------------------------")

print(
    "Pixel hitam  :",
    binary_hitam
)

print(
    "Pixel putih  :",
    binary_putih
)

print(
    "Persen hitam :",
    round(
        binary_persen_hitam,
        2
    ),
    "%"
)

print(
    "Persen putih :",
    round(
        binary_persen_putih,
        2
    ),
    "%"
)


print()
print("----------------------------------------------")
print("MULTI THRESHOLDING")
print("----------------------------------------------")

print(
    "Pixel hitam  :",
    multi_hitam
)

print(
    "Pixel abu-abu:",
    multi_abu
)

print(
    "Pixel putih  :",
    multi_putih
)

print(
    "Persen hitam :",
    round(
        multi_persen_hitam,
        2
    ),
    "%"
)

print(
    "Persen abu-abu:",
    round(
        multi_persen_abu,
        2
    ),
    "%"
)

print(
    "Persen putih :",
    round(
        multi_persen_putih,
        2
    ),
    "%"
)


print()
print("----------------------------------------------")
print("OTSU THRESHOLDING")
print("----------------------------------------------")

print(
    "Pixel hitam  :",
    otsu_hitam
)

print(
    "Pixel putih  :",
    otsu_putih
)

print(
    "Persen hitam :",
    round(
        otsu_persen_hitam,
        2
    ),
    "%"
)

print(
    "Persen putih :",
    round(
        otsu_persen_putih,
        2
    ),
    "%"
)


# ==========================================================
# 12. TABEL PERBANDINGAN
# ==========================================================

print()
print("==============================================================")
print("                 TABEL PERBANDINGAN")
print("==============================================================")

print(
    f"{'Metode':<15}"
    f"{'Hitam (%)':<15}"
    f"{'Abu-abu (%)':<15}"
    f"{'Putih (%)':<15}"
)

print("-" * 60)

print(
    f"{'Binary':<15}"
    f"{binary_persen_hitam:<15.2f}"
    f"{'-':<15}"
    f"{binary_persen_putih:<15.2f}"
)

print(
    f"{'Multi':<15}"
    f"{multi_persen_hitam:<15.2f}"
    f"{multi_persen_abu:<15.2f}"
    f"{multi_persen_putih:<15.2f}"
)

print(
    f"{'Otsu':<15}"
    f"{otsu_persen_hitam:<15.2f}"
    f"{'-':<15}"
    f"{otsu_persen_putih:<15.2f}"
)

print("==============================================================")


# ==========================================================
# 13. MENAMPILKAN VISUAL PERBANDINGAN
# ==========================================================

plt.figure(
    figsize=(16, 5)
)


# Binary

plt.subplot(
    1,
    3,
    1
)

plt.imshow(
    binary,
    cmap="gray"
)

plt.title(
    "Binary Thresholding"
)

plt.axis("off")


# Multi

plt.subplot(
    1,
    3,
    2
)

plt.imshow(
    multi,
    cmap="gray"
)

plt.title(
    "Multi Thresholding"
)

plt.axis("off")


# Otsu

plt.subplot(
    1,
    3,
    3
)

plt.imshow(
    otsu,
    cmap="gray"
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
    binary_persen_hitam,
    multi_persen_hitam,
    otsu_persen_hitam
]

persen_putih = [
    binary_persen_putih,
    multi_persen_putih,
    otsu_persen_putih
]

x = np.arange(
    len(metode)
)

lebar = 0.35


plt.figure(
    figsize=(9, 5)
)

plt.bar(
    x - lebar / 2,
    persen_hitam,
    lebar,
    label="Hitam"
)

plt.bar(
    x + lebar / 2,
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
    "Persentase Pixel (%)"
)

plt.title(
    "Perbandingan Distribusi Pixel"
)

plt.legend()

plt.tight_layout()

plt.show()


print()
print("==============================================")
print("       PERBANDINGAN SELESAI")
print("==============================================")