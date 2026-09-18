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

file_gambar = "IMG_0210_JPG.rf.88fef2f797fa888a725ec075a039aa57.jpg"

faktor_zoom = 10

path_gambar = os.path.join(
    dataset_folder,
    file_gambar
)

if not os.path.exists(path_gambar):
    print(f"Gambar {file_gambar} tidak ditemukan.")
    exit()

image = Image.open(path_gambar).convert("RGB")

lebar_baru = image.width * faktor_zoom
tinggi_baru = image.height * faktor_zoom

hasil = image.resize(
    (lebar_baru, tinggi_baru),
    Image.Resampling.LANCZOS
)

nama_hasil = "zooming_0210.jpg"

output_file = os.path.join(
    hasil_folder,
    nama_hasil
)

hasil.save(output_file)

print("------------------------------------------")
print("Operasi           : Zooming")
print("Gambar            : 0210")
print(f"Faktor zoom       : {faktor_zoom}x")
print(f"Ukuran awal       : {image.size}")
print(f"Ukuran hasil      : {hasil.size}")
print(f"Hasil             : {nama_hasil}")
print(f"Lokasi            : {output_file}")
print("------------------------------------------")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Citra Awal - 0210")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(hasil)
plt.title(f"Hasil Zooming {faktor_zoom}x")
plt.axis("off")


plt.suptitle(
    "Operasi Zooming Citra"
)

plt.tight_layout()
plt.show()

print()
print("==========================================")
print("          ZOOMING CITRA SELESAI")
print("==========================================")
print("Hasil telah disimpan di:")
print(output_file)