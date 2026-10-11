
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
grayscale = image.convert("L")

lebar, tinggi = grayscale.size

kernel_gx = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

kernel_gy = [
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
]

hasil = Image.new("L", (lebar, tinggi))

pixel_asli = grayscale.load()
pixel_hasil = hasil.load()

gradien = [
    [0.0 for x in range(lebar)]
    for y in range(tinggi)
]

nilai_maksimum = 0.0

for y in range(1, tinggi - 1):
    for x in range(1, lebar - 1):

        gx = 0
        gy = 0

        for ky in range(3):
            for kx in range(3):

                px = x + kx - 1
                py = y + ky - 1

                nilai_pixel = pixel_asli[px, py]

                gx += nilai_pixel * kernel_gx[ky][kx]
                gy += nilai_pixel * kernel_gy[ky][kx]

        magnitudo = math.sqrt(gx ** 2 + gy ** 2)

        gradien[y][x] = magnitudo

        if magnitudo > nilai_maksimum:
            nilai_maksimum = magnitudo

for y in range(1, tinggi - 1):
    for x in range(1, lebar - 1):

        if nilai_maksimum > 0:
            nilai_normal = (
                gradien[y][x] / nilai_maksimum
            ) * 255
        else:
            nilai_normal = 0

        pixel_hasil[x, y] = int(
            max(0, min(255, nilai_normal))
        )

for x in range(lebar):
    pixel_hasil[x, 0] = 0
    pixel_hasil[x, tinggi - 1] = 0

for y in range(tinggi):
    pixel_hasil[0, y] = 0
    pixel_hasil[lebar - 1, y] = 0

nama_hasil = (
    "sobel_operator_IMG"
    + os.path.splitext(file_gambar)[0].replace(
        "IMG_0258_JPG.rf.", ""
    )
    + ".png"
)

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(output_file)

print("------------------------------------------")
print(f"File gambar : {file_gambar}")
print("Operasi     : Sobel Operator")
print("Ukuran      : 3 x 3")
print("Kernel      : Gx dan Gy")
print(f"Hasil       : {output_file}")
print("------------------------------------------")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.imshow(grayscale, cmap="gray")
plt.title("Citra Grayscale")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(hasil, cmap="gray")
plt.title("Hasil Sobel Operator 3 x 3")
plt.axis("off")

plt.tight_layout()
plt.show()

print()
print("==========================================")
print("       SOBEL OPERATOR SELESAI")
print("==========================================")
