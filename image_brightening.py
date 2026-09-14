from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import os

folder = os.path.dirname(os.path.abspath(__file__))
dataset_folder = os.path.join(folder, "DATASET GAMBAR")
hasil_folder = os.path.join(folder, "HASIL_BRIGHTENING")
os.makedirs(hasil_folder, exist_ok=True)

brightness_factor = 1.35

file_gambar = [
    file for file in os.listdir(dataset_folder)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]

for file in file_gambar:

    # Lokasi gambar original
    input_path = os.path.join(dataset_folder, file)

    # Membuka gambar
    image = Image.open(input_path).convert("RGB")

    # Melakukan image brightening
    brightened_image = ImageEnhance.Brightness(
        image
    ).enhance(brightness_factor)

    # Nama file hasil
    nama_file, ekstensi = os.path.splitext(file)

    output_path = os.path.join(
        hasil_folder,
        nama_file + "_brightening" + ekstensi
    )

    brightened_image.save(output_path)

    print(f"Berhasil: {file}")
    print(f"Disimpan: {output_path}")

print("\n===================================")
print("SEMUA GAMBAR BERHASIL DIPROSES")
print("===================================")
print(f"Folder hasil: {hasil_folder}")