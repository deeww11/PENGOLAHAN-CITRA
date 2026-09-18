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

# Nilai translasi
geser_x = 100
geser_y = 50

# Membuat gambar hasil dengan ukuran yang sama
hasil = Image.new(
    "RGB",
    image.size,
    (0, 0, 0)
)

# Melakukan translasi
hasil.paste(
    image,
    (geser_x, geser_y)
)

nama_file = os.path.splitext(file_gambar)[0]
nama_hasil = "translasi_" + nama_file + ".jpg"

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(output_file)

print("------------------------------------------")
print(f"File gambar      : {file_gambar}")
print(f"Geser horizontal : {geser_x} piksel")
print(f"Geser vertikal   : {geser_y} piksel")
print("Operasi          : Translasi Citra")
print(f"Hasil disimpan   : {output_file}")
print("------------------------------------------")

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Citra Awal")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(hasil)
plt.title(
    f"Citra Setelah Translasi ({geser_x}, {geser_y})"
)
plt.axis("off")

plt.suptitle("Operasi Geometri Translasi Citra")
plt.tight_layout()
plt.show()