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
    "HASIL_OPERASI_GEOMETRI"
)

os.makedirs(hasil_folder, exist_ok=True)

file_gambar = [
    file for file in os.listdir(dataset_folder)
    if file.lower().endswith(
        (".jpg", ".jpeg", ".png", ".bmp")
    )
]

if not file_gambar:
    print("Tidak ada gambar di dalam folder DATASET GAMBAR.")
    exit()

file_gambar = file_gambar[0]

path_gambar = os.path.join(
    dataset_folder,
    file_gambar
)

image = Image.open(path_gambar).convert("RGB")

hasil_horizontal = image.transpose(
    Image.Transpose.FLIP_LEFT_RIGHT
)

hasil_vertikal = image.transpose(
    Image.Transpose.FLIP_TOP_BOTTOM
)

nama_file = os.path.splitext(file_gambar)[0]

nama_horizontal = (
    "flipping_horizontal_"
    + nama_file
    + ".jpg"
)

nama_vertikal = (
    "flipping_vertikal_"
    + nama_file
    + ".jpg"
)

output_horizontal = os.path.join(
    hasil_folder,
    nama_horizontal
)

output_vertikal = os.path.join(
    hasil_folder,
    nama_vertikal
)

hasil_horizontal.save(output_horizontal)

hasil_vertikal.save(output_vertikal)

print("------------------------------------------")
print(f"File gambar      : {file_gambar}")
print("Operasi          : Flipping Citra")
print("Flipping         : Horizontal dan Vertikal")
print(f"Hasil horizontal : {output_horizontal}")
print(f"Hasil vertikal   : {output_vertikal}")
print("------------------------------------------")

plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Citra Awal")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(hasil_horizontal)
plt.title("Flipping Horizontal")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(hasil_vertikal)
plt.title("Flipping Vertikal")
plt.axis("off")

plt.suptitle(
    "Operasi Geometri Flipping Citra"
)

plt.tight_layout()
plt.show()


print()
print("==========================================")
print("          FLIPPING CITRA SELESAI")
print("==========================================")
print("Hasil telah disimpan di:")
print(output_horizontal)
print(output_vertikal)