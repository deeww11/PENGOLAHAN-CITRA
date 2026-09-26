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
    "HASIL_THRESHOLDING"
)

os.makedirs(hasil_folder, exist_ok=True)

file_gambar = "IMG_0230_JPG.rf.6aa737da228dfd6ab26b74bbcd84b98e.jpg"

path_gambar = os.path.join(
    dataset_folder,
    file_gambar
)

if not os.path.exists(path_gambar):
    print(f"Gambar {file_gambar} tidak ditemukan.")
    exit()

path_gambar = os.path.join(
    dataset_folder,
    file_gambar
)

image = Image.open(path_gambar).convert("RGB")

grayscale = image.convert("L")

threshold = 128

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

nama_file = os.path.splitext(file_gambar)[0]

nama_hasil = (
    "binary_thresholding_"
    + nama_file
    + ".jpg"
)

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(output_file)

print("------------------------------------------")
print(f"File gambar      : {file_gambar}")
print("Operasi          : Binary Thresholding")
print(f"Nilai threshold  : {threshold}")
print(f"Hasil disimpan   : {output_file}")
print("------------------------------------------")

plt.figure(figsize=(15, 4))


plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Citra Awal")
plt.axis("off")


plt.subplot(1, 3, 2)
plt.imshow(grayscale, cmap="gray")
plt.title("Citra Grayscale")
plt.axis("off")


plt.subplot(1, 3, 3)
plt.imshow(hasil, cmap="gray")
plt.title("Binary Thresholding")
plt.axis("off")


plt.suptitle(
    "Binary Thresholding"
)

plt.tight_layout()
plt.show()


print()
print("==========================================")
print("      BINARY THRESHOLDING SELESAI")
print("==========================================")