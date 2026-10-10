from PIL import Image
import matplotlib.pyplot as plt
import os
import math

folder_utama = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

dataset_folder = os.path.join(
    folder_utama,
    "DATASET GAMBAR"
)

hasil_folder = os.path.join(
    folder_utama,
    "HASIL_FILTER"
)

os.makedirs(hasil_folder, exist_ok=True)

file_gambar = (
    "IMG_0258_JPG.rf."
    "1bb8833eac9343137e2471c6b48e7df2.jpg"
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

# Parameter Bilateral Filter
radius = 1
sigma_spatial = 1.0
sigma_intensity = 50.0

# Proses Bilateral Filter dengan kernel 3 x 3
for y in range(radius, tinggi - radius):
    for x in range(radius, lebar - radius):

        # Nilai RGB pixel pusat
        pusat_r, pusat_g, pusat_b = pixel_asli[x, y]

        jumlah_r = 0.0
        jumlah_g = 0.0
        jumlah_b = 0.0
        jumlah_bobot = 0.0

        # Mengambil pixel di sekitar pixel pusat
        for ky in range(-radius, radius + 1):
            for kx in range(-radius, radius + 1):

                px = x + kx
                py = y + ky

                r, g, b = pixel_asli[px, py]

                # 1. Bobot jarak spasial
                jarak = kx**2 + ky**2

                bobot_spasial = math.exp(
                    -jarak / (2 * sigma_spatial**2)
                )

                # 2. Bobot perbedaan intensitas warna
                selisih_r = r - pusat_r
                selisih_g = g - pusat_g
                selisih_b = b - pusat_b

                selisih_warna = (
                    selisih_r**2
                    + selisih_g**2
                    + selisih_b**2
                )

                bobot_intensitas = math.exp(
                    -selisih_warna
                    / (2 * sigma_intensity**2)
                )

                # 3. Menggabungkan kedua bobot
                bobot = bobot_spasial * bobot_intensitas

                # 4. Menghitung jumlah RGB berbobot
                jumlah_r += r * bobot
                jumlah_g += g * bobot
                jumlah_b += b * bobot

                jumlah_bobot += bobot

        # 5. Normalisasi nilai RGB
        if jumlah_bobot > 0:
            nilai_r = int(jumlah_r / jumlah_bobot)
            nilai_g = int(jumlah_g / jumlah_bobot)
            nilai_b = int(jumlah_b / jumlah_bobot)

            pixel_hasil[x, y] = (
                max(0, min(255, nilai_r)),
                max(0, min(255, nilai_g)),
                max(0, min(255, nilai_b))
            )

# Mempertahankan pixel asli pada bagian tepi
for x in range(lebar):
    pixel_hasil[x, 0] = pixel_asli[x, 0]
    pixel_hasil[x, tinggi - 1] = pixel_asli[x, tinggi - 1]

for y in range(tinggi):
    pixel_hasil[0, y] = pixel_asli[0, y]
    pixel_hasil[lebar - 1, y] = pixel_asli[lebar - 1, y]

# Menyimpan hasil Bilateral Filter
nama_hasil = (
    "bilateral_filter_"
    + os.path.splitext(file_gambar)[0]
    + ".jpg"
)

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(output_file)

print("------------------------------------------")
print(f"File gambar      : {file_gambar}")
print("Operasi          : Bilateral Filter")
print("Ukuran kernel    : 3 x 3")
print(f"Sigma Spatial    : {sigma_spatial}")
print(f"Sigma Intensity  : {sigma_intensity}")
print(f"Hasil            : {output_file}")
print("------------------------------------------")

# Menampilkan perbandingan citra
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Citra Awal")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(hasil)
plt.title("Hasil Bilateral Filter 3 x 3")
plt.axis("off")

plt.tight_layout()
plt.show()

print()
print("==========================================")
print("      BILATERAL FILTER SELESAI")
print("==========================================")