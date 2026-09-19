from PIL import Image
import os
import numpy as np

folder_histogram = os.path.dirname(os.path.abspath(__file__))

folder_project = os.path.dirname(folder_histogram)

folder_dataset = os.path.join(
    folder_project,
    "DATASET GAMBAR"
)

file_gambar = [
    file for file in os.listdir(folder_dataset)
    if file.lower().endswith((
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp"
    ))
]

if len(file_gambar) == 0:
    print("Tidak ada gambar di folder DATASET GAMBAR.")
    exit()

print("====================================")
print("       DATASET GAMBAR")
print("====================================")

for i, file in enumerate(file_gambar, start=1):
    print(f"{i}. {file}")

while True:

    try:
        pilihan = int(input("\nPilih nomor gambar: "))

        if 1 <= pilihan <= len(file_gambar):
            break
        else:
            print("Nomor gambar tidak tersedia.")

    except ValueError:
        print("Masukkan angka.")


nama_file = file_gambar[pilihan - 1]

path_gambar = os.path.join(
    folder_dataset,
    nama_file
)

gambar = Image.open(path_gambar)

print("\n====================================")
print("          INFORMASI GAMBAR")
print("====================================")

print("Nama gambar :", nama_file)
print("Ukuran      :", gambar.size)
print("Mode        :", gambar.mode)

gambar_grayscale = gambar.convert("L")

data_pixel = np.array(gambar_grayscale)

mean = np.mean(data_pixel)

variansi = np.var(data_pixel)

standar_deviasi = np.std(data_pixel)

print("\n====================================")
print("       HASIL STATISTIK CITRA")
print("====================================")

print(f"Mean              : {mean:.2f}")

print(f"Variansi          : {variansi:.2f}")

print(f"Standar Deviasi   : {standar_deviasi:.2f}")

print("====================================")