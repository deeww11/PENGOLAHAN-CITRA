
from PIL import Image
import matplotlib.pyplot as plt
import os

folder_utama = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

dataset_folder = os.path.join(
    folder_utama,
    "DATASET GAMBAR 1",
    "Images"
)

hasil_folder = os.path.join(
    folder_utama,
    "HASIL_FILTER"
)

os.makedirs(hasil_folder, exist_ok=True)

file_gambar = (
    "0a64655c-4052-4e5f-a696-2a6cf25d10c9"
    "___GCREC_Bact.Sp 6017.JPG"
)

path_gambar = os.path.join(
    dataset_folder,
    file_gambar
)

if not os.path.exists(path_gambar):
    print(f"Gambar {file_gambar} tidak ditemukan.")
    print(f"Periksa folder: {dataset_folder}")
    raise SystemExit

image = Image.open(path_gambar).convert("RGB")
lebar, tinggi = image.size

hasil = Image.new("RGB", (lebar, tinggi))

pixel_asli = image.load()
pixel_hasil = hasil.load()

# Proses Mean Filter dengan kernel 3 x 3
for y in range(1, tinggi - 1):
    for x in range(1, lebar - 1):

        jumlah_r = 0
        jumlah_g = 0
        jumlah_b = 0

        # Mengambil 9 pixel di sekitar pixel pusat
        for ky in range(-1, 2):
            for kx in range(-1, 2):

                r, g, b = pixel_asli[x + kx, y + ky]

                jumlah_r += r
                jumlah_g += g
                jumlah_b += b

        rata_r = jumlah_r / 9
        rata_g = jumlah_g / 9
        rata_b = jumlah_b / 9

        pixel_hasil[x, y] = (
            int(rata_r),
            int(rata_g),
            int(rata_b)
        )

for x in range(lebar):
    pixel_hasil[x, 0] = pixel_asli[x, 0]
    pixel_hasil[x, tinggi - 1] = pixel_asli[x, tinggi - 1]

for y in range(tinggi):
    pixel_hasil[0, y] = pixel_asli[0, y]
    pixel_hasil[lebar - 1, y] = pixel_asli[lebar - 1, y]

nama_hasil = (
    "mean_filter_FIX_"
    + os.path.splitext(file_gambar)[0]
    + ".jpg"
)

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(output_file)

print("------------------------------------------")
print(f"File gambar : {file_gambar}")
print("Operasi     : Mean Filter")
print("Ukuran      : 3 x 3")
print(f"Hasil       : {output_file}")
print("------------------------------------------")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Citra Awal")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(hasil)
plt.title("Hasil Mean Filter 3 x 3")
plt.axis("off")

plt.tight_layout()
plt.show()

print()
print("==========================================")
print("        MEAN FILTER SELESAI")
print("==========================================")