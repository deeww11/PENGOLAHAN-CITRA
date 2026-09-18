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

c = 3

file_gambar = [
    file for file in os.listdir(dataset_folder)
    if file.lower().endswith(
        (".jpg", ".jpeg", ".png", ".bmp")
    )
]

if not file_gambar:
    print("Tidak ada gambar di dalam folder DATASET GAMBAR.")
    exit()


for file in file_gambar:

    path_gambar = os.path.join(
        dataset_folder,
        file
    )

    image = Image.open(path_gambar).convert("RGB")

    hasil = Image.new(
        "RGB",
        image.size
    )

    pixels = image.load()
    hasil_pixels = hasil.load()

    for y in range(image.height):

        for x in range(image.width):

            r, g, b = pixels[x, y]

            r_baru = min(255, r * c)
            g_baru = min(255, g * c)
            b_baru = min(255, b * c)

            hasil_pixels[x, y] = (
                r_baru,
                g_baru,
                b_baru
            )

    nama_file = os.path.splitext(file)[0]
    nama_hasil = nama_file + "_perkalian.jpg"

    output_file = os.path.join(
        hasil_folder,
        nama_hasil
    )

    hasil.save(output_file)

    print("------------------------------------------")
    print(f"File gambar       : {file}")
    print(f"Nilai skalar      : {c}")
    print(f"Operasi           : Perkalian")
    print(f"Hasil disimpan    : {output_file}")
    print("------------------------------------------")

    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Citra Awal")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(hasil)
    plt.title(f"Citra Setelah Dikalikan {c}")
    plt.axis("off")

    plt.suptitle(
        "Perkalian Citra dengan Skalar"
    )

    plt.tight_layout()
    plt.show()