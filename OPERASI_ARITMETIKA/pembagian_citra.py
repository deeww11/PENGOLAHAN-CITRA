from PIL import Image
import matplotlib.pyplot as plt
import os

# Menentukan folder utama
folder_utama = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Folder dataset
dataset_folder = os.path.join(
    folder_utama,
    "DATASET GAMBAR"
)

# Folder hasil
hasil_folder = os.path.join(
    folder_utama,
    "HASIL_OPERASI_ARITMETIKA"
)

os.makedirs(hasil_folder, exist_ok=True)


# Mengambil daftar file gambar
file_gambar = [
    file for file in os.listdir(dataset_folder)
    if file.lower().endswith(
        (".jpg", ".jpeg", ".png", ".bmp")
    )
]

# Memastikan terdapat minimal 2 gambar
if len(file_gambar) < 2:
    print("Dataset harus memiliki minimal 2 gambar.")
    exit()


# Mengambil gambar pertama dan kedua
file_gambar1 = file_gambar[0]
file_gambar2 = file_gambar[1]

path_gambar1 = os.path.join(
    dataset_folder,
    file_gambar1
)

path_gambar2 = os.path.join(
    dataset_folder,
    file_gambar2
)


# Membuka kedua citra
image1 = Image.open(path_gambar1).convert("RGB")
image2 = Image.open(path_gambar2).convert("RGB")


# Menyamakan ukuran citra kedua dengan citra pertama
if image1.size != image2.size:
    image2 = image2.resize(image1.size)


# Membuat citra hasil
hasil = Image.new(
    "RGB",
    image1.size
)

pixels1 = image1.load()
pixels2 = image2.load()
hasil_pixels = hasil.load()


# Proses pembagian citra
for y in range(image1.height):
    for x in range(image1.width):

        r1, g1, b1 = pixels1[x, y]
        r2, g2, b2 = pixels2[x, y]

        # Menghindari pembagian dengan nol
        r_baru = min(255, int(r1 / r2 * 255)) if r2 != 0 else 255
        g_baru = min(255, int(g1 / g2 * 255)) if g2 != 0 else 255
        b_baru = min(255, int(b1 / b2 * 255)) if b2 != 0 else 255

        hasil_pixels[x, y] = (
            r_baru,
            g_baru,
            b_baru
        )


# Nama file hasil
nama_file1 = os.path.splitext(file_gambar1)[0]
nama_file2 = os.path.splitext(file_gambar2)[0]

nama_hasil = (
    nama_file1
    + "_dibagi_"
    + nama_file2
    + ".jpg"
)

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)


# Menyimpan hasil
hasil.save(output_file)


# Menampilkan informasi
print("------------------------------------------")
print(f"Citra pertama    : {file_gambar1}")
print(f"Citra kedua      : {file_gambar2}")
print("Operasi          : Pembagian Citra")
print(f"Hasil disimpan   : {output_file}")
print("------------------------------------------")


# Menampilkan citra
plt.figure(figsize=(15, 4))

plt.subplot(1, 3, 1)
plt.imshow(image1)
plt.title("Citra 1")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(image2)
plt.title("Citra 2")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(hasil)
plt.title("Hasil Pembagian")
plt.axis("off")

plt.suptitle("Operasi Pembagian Dua Buah Citra")
plt.tight_layout()
plt.show()