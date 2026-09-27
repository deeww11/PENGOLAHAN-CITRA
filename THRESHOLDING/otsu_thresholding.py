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

os.makedirs(
    hasil_folder,
    exist_ok=True
)

file_gambar = (
    "IMG_0230_JPG.rf."
    "6aa737da228dfd6ab26b74bbcd84b98e.jpg"
)

path_gambar = os.path.join(
    dataset_folder,
    file_gambar
)

if not os.path.exists(path_gambar):

    print(
        f"Gambar {file_gambar} tidak ditemukan."
    )

    exit()

image = Image.open(
    path_gambar
).convert("RGB")

grayscale = image.convert("L")

histogram = grayscale.histogram()

total_pixel = (
    grayscale.width *
    grayscale.height
)

jumlah_intensitas_total = 0

for i in range(256):

    jumlah_intensitas_total += (
        i * histogram[i]
    )


jumlah_background = 0

jumlah_intensitas_background = 0

nilai_threshold_otsu = 0

nilai_variansi_maksimum = 0


for threshold in range(256):

    jumlah_background += (
        histogram[threshold]
    )

    if jumlah_background == 0:
        continue


    jumlah_foreground = (
        total_pixel -
        jumlah_background
    )

    if jumlah_foreground == 0:
        break


    jumlah_intensitas_background += (
        threshold *
        histogram[threshold]
    )


    mean_background = (
        jumlah_intensitas_background /
        jumlah_background
    )


    jumlah_intensitas_foreground = (
        jumlah_intensitas_total -
        jumlah_intensitas_background
    )


    mean_foreground = (
        jumlah_intensitas_foreground /
        jumlah_foreground
    )


    probabilitas_background = (
        jumlah_background /
        total_pixel
    )


    probabilitas_foreground = (
        jumlah_foreground /
        total_pixel
    )


    variansi_antar_kelas = (
        probabilitas_background *
        probabilitas_foreground *
        (
            mean_background -
            mean_foreground
        ) ** 2
    )


    if (
        variansi_antar_kelas >
        nilai_variansi_maksimum
    ):

        nilai_variansi_maksimum = (
            variansi_antar_kelas
        )

        nilai_threshold_otsu = (
            threshold
        )

threshold = nilai_threshold_otsu

hasil = Image.new(
    "L",
    grayscale.size
)

pixels_grayscale = (
    grayscale.load()
)

hasil_pixels = (
    hasil.load()
)


for y in range(
    grayscale.height
):

    for x in range(
        grayscale.width
    ):

        nilai_pixel = (
            pixels_grayscale[x, y]
        )

        if nilai_pixel >= threshold:

            hasil_pixels[x, y] = 255

        else:

            hasil_pixels[x, y] = 0

nama_file = os.path.splitext(
    file_gambar
)[0]

nama_hasil = (
    "otsu_thresholding_"
    + nama_file
    + ".jpg"
)

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(
    output_file
)

print("------------------------------------------")
print("METODE OTSU THRESHOLDING")
print("------------------------------------------")
print(
    f"File gambar      : {file_gambar}"
)
print(
    f"Nilai T Otsu     : {threshold}"
)
print(
    "Penentuan T      : Otomatis"
)
print(
    f"Hasil disimpan   : {output_file}"
)
print("------------------------------------------")

plt.figure(
    figsize=(15, 4)
)

plt.subplot(1, 3, 1)

plt.imshow(
    image
)

plt.title(
    "Citra Awal"
)

plt.axis(
    "off"
)

plt.subplot(1, 3, 2)

plt.imshow(
    grayscale,
    cmap="gray"
)

plt.title(
    "Citra Grayscale"
)

plt.axis(
    "off"
)

plt.subplot(1, 3, 3)

plt.imshow(
    hasil,
    cmap="gray"
)

plt.title(
    f"Otsu Thresholding\n"
    f"T = {threshold}"
)

plt.axis(
    "off"
)


plt.suptitle(
    "Otsu Thresholding"
)

plt.tight_layout()

plt.show()

plt.figure(
    figsize=(10, 5)
)

plt.bar(
    range(256),
    histogram,
    width=1
)

plt.axvline(
    threshold,
    linestyle="--",
    linewidth=2,
    label=f"T Otsu = {threshold}"
)


plt.title(
    "Histogram Citra Grayscale"
)

plt.xlabel(
    "Intensitas Piksel"
)

plt.ylabel(
    "Jumlah Piksel"
)

plt.xlim(
    0,
    255
)

plt.legend()

plt.tight_layout()

plt.show()

print()

print(
    "=========================================="
)

print(
    "       OTSU THRESHOLDING SELESAI"
)

print(
    "=========================================="
)