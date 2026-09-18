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
    "HASIL_OPERASI_ARITMETIKA"
)

os.makedirs(hasil_folder, exist_ok=True)


file_0215 = "IMG_0215_JPG.rf.72f64552ad2cd18b9534adce25f54cc5.jpg"

file_0216 = "IMG_0216_JPG.rf.2f2281def8c9e88325cf0bcfb3689634.jpg"

path_0215 = os.path.join(
    dataset_folder,
    file_0215
)

path_0216 = os.path.join(
    dataset_folder,
    file_0216
)

if not os.path.exists(path_0215):
    print("Gambar 0215 tidak ditemukan.")
    exit()

if not os.path.exists(path_0216):
    print("Gambar 0216 tidak ditemukan.")
    exit()

image_0215 = Image.open(path_0215).convert("RGB")
image_0216 = Image.open(path_0216).convert("RGB")

if image_0215.size != image_0216.size:

    print("Ukuran gambar berbeda.")
    print(f"Ukuran 0215 : {image_0215.size}")
    print(f"Ukuran 0216 : {image_0216.size}")

    image_0216 = image_0216.resize(
        image_0215.size
    )

    print("Ukuran gambar 0216 telah disesuaikan.")

hasil = Image.new(
    "RGB",
    image_0215.size
)

pixels_0215 = image_0215.load()
pixels_0216 = image_0216.load()
hasil_pixels = hasil.load()


for y in range(image_0215.height):

    for x in range(image_0215.width):

        r1, g1, b1 = pixels_0215[x, y]

        r2, g2, b2 = pixels_0216[x, y]

        r_baru = int((r1 * r2) / 255)
        g_baru = int((g1 * g2) / 255)
        b_baru = int((b1 * b2) / 255)

        hasil_pixels[x, y] = (
            r_baru,
            g_baru,
            b_baru
        )

nama_hasil = "perkalian_0215_dan_0216.jpg"

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(output_file)


print("------------------------------------------")
print("Operasi           : Perkalian Citra")
print("Gambar pertama    : 0215")
print("Gambar kedua      : 0216")
print(f"Hasil             : {nama_hasil}")
print(f"Lokasi            : {output_file}")
print("------------------------------------------")

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(image_0215)
plt.title("Citra 0215")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(image_0216)
plt.title("Citra 0216")
plt.axis("off")


plt.subplot(1, 3, 3)
plt.imshow(hasil)
plt.title("Hasil Perkalian")
plt.axis("off")


plt.suptitle(
    "Operasi Perkalian Citra 0215 × 0216"
)

plt.tight_layout()
plt.show()

print()
print("==========================================")
print("       PERKALIAN CITRA SELESAI")
print("==========================================")
print("Hasil telah disimpan di:")
print(output_file)