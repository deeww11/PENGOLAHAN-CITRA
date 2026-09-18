from PIL import Image
import matplotlib.pyplot as plt
import os

# Menentukan folder utama PENGOLAHAN-CITRA
folder_utama = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Folder dataset gambar
dataset_folder = os.path.join(
    folder_utama,
    "DATASET GAMBAR"
)

# Folder hasil
hasil_folder = os.path.join(
    folder_utama,
    "OPERASI_ARITMETIKA"
)

# Membuat folder hasil jika belum ada
os.makedirs(hasil_folder, exist_ok=True)

# Nilai skalar perkalian
c = 3

# Mengambil semua file gambar dari folder DATASET GAMBAR
file_gambar = [
    file for file in os.listdir(dataset_folder)
    if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
]

# Mengecek apakah terdapat gambar
if not file_gambar:
    print("Tidak ada gambar di dalam folder DATASET GAMBAR.")
    exit()

# Memproses setiap gambar
for file in file_gambar:

    # Membuka gambar
    path_gambar = os.path.join(dataset_folder, file)
    image = Image.open(path_gambar).convert("RGB")

    # Membuat gambar hasil
    hasil = Image.new("RGB", image.size)

    # Mengakses piksel
    pixels = image.load()
    hasil_pixels = hasil.load()

    # Proses perkalian setiap piksel
    for y in range(image.height):
        for x in range(image.width):

            # Mengambil nilai RGB
            r, g, b = pixels[x, y]

            # Rumus:
            # B(x,y) = c × A(x,y)
            r_baru = min(255, r * c)
            g_baru = min(255, g * c)
            b_baru = min(255, b * c)

            # Menyimpan nilai piksel baru
            hasil_pixels[x, y] = (
                r_baru,
                g_baru,
                b_baru
            )

    # Membuat nama file hasil
    nama_file = os.path.splitext(file)[0]

    output_file = os.path.join(
        hasil_folder,
        nama_file + "_perkalian.jpg"
    )

    # Menyimpan hasil
    hasil.save(output_file)

    print(f"Berhasil memproses: {file}")
    print(f"Hasil disimpan di: {output_file}")

    # Menampilkan citra awal dan hasil
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Citra Awal")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(hasil)
    plt.title(f"Citra Setelah Dikalikan {c}")
    plt.axis("off")

    plt.suptitle("Perkalian Citra dengan Skalar")

    plt.tight_layout()
    plt.show()