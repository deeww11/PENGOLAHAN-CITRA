from PIL import Image
import matplotlib.pyplot as plt
import os

folder_utama = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

dataset_folder = os.path.join(
    folder_utama,
    "DATASET GAMBAR"
)

hasil_folder = os.path.join(
    folder_utama,
    "HASIL_KONVOLUSI"
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

# Kernel Gaussian 3 x 3
kernel = [
    [1/16, 2/16, 1/16],
    [2/16, 4/16, 2/16],
    [1/16, 2/16, 1/16]
]

hasil = Image.new("RGB", (lebar, tinggi))

pixel_asli = image.load()
pixel_hasil = hasil.load()

# Proses konvolusi manual
for y in range(1, tinggi - 1):
    for x in range(1, lebar - 1):

        jumlah_r = 0
        jumlah_g = 0
        jumlah_b = 0

        for ky in range(3):
            for kx in range(3):

                px = x + kx - 1
                py = y + ky - 1

                r, g, b = pixel_asli[px, py]
                bobot = kernel[ky][kx]

                jumlah_r += r * bobot
                jumlah_g += g * bobot
                jumlah_b += b * bobot

        pixel_hasil[x, y] = (
            int(jumlah_r),
            int(jumlah_g),
            int(jumlah_b)
        )

# Menangani tepi gambar dengan mempertahankan
# pixel asli pada bagian tepi
for x in range(lebar):
    pixel_hasil[x, 0] = pixel_asli[x, 0]
    pixel_hasil[x, tinggi - 1] = pixel_asli[x, tinggi - 1]

for y in range(tinggi):
    pixel_hasil[0, y] = pixel_asli[0, y]
    pixel_hasil[lebar - 1, y] = pixel_asli[lebar - 1, y]

nama_hasil = "gaussian_kernel_" + os.path.splitext(file_gambar)[0] + ".jpg"
output_file = os.path.join(hasil_folder, nama_hasil)

hasil.save(output_file)

print("------------------------------------------")
print(f"File gambar : {file_gambar}")
print("Operasi     : Gaussian Kernel")
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
plt.title("Hasil Gaussian Kernel 3 x 3")
plt.axis("off")

plt.tight_layout()
plt.show()

print()
print("==========================================")
print("      GAUSSIAN KERNEL SELESAI")
print("==========================================")