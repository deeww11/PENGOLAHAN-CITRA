import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

script_folder = os.path.dirname(os.path.abspath(__file__))

project_folder = os.path.dirname(script_folder)

dataset_folder = os.path.join(
    project_folder,
    "DATASET GAMBAR"
)

output_folder = os.path.join(
    project_folder,
    "HASIL_THRESHOLDING"
)

os.makedirs(output_folder, exist_ok=True)

input_filename = "IMG_0230_JPG.rf.6aa737da228dfd6ab26b74bbcd84b98e.jpg"

image_path = os.path.join(
    dataset_folder,
    input_filename
)

print("==========================================")
print("MULTI THRESHOLDING")
print("==========================================")

print("Lokasi gambar:")
print(image_path)
print()


if not os.path.exists(image_path):

    print("❌ FILE GAMBAR TIDAK DITEMUKAN!")
    print()
    print("Pastikan nama file sesuai:")
    print(input_filename)

    input("\nTekan ENTER untuk keluar...")
    exit()


img = cv2.imread(image_path)


if img is None:

    print("❌ GAMBAR GAGAL DIBACA!")

    input("\nTekan ENTER untuk keluar...")
    exit()


print("✅ Gambar berhasil dibaca!")
print()

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

T1 = 80
T2 = 160


multi = np.zeros_like(gray)

multi[gray <= T1] = 0

multi[
    (gray > T1) &
    (gray <= T2)
] = 127

multi[gray > T2] = 255

output_filename = "multi_thresholding_IMG_0230.png"

output_path = os.path.join(
    output_folder,
    output_filename
)

cv2.imwrite(
    output_path,
    multi
)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)

plt.imshow(
    gray,
    cmap="gray"
)

plt.title("Grayscale")

plt.axis("off")

plt.subplot(1, 2, 2)

plt.imshow(
    multi,
    cmap="gray"
)

plt.title(
    f"Multi Thresholding\nT1 = {T1}, T2 = {T2}"
)

plt.axis("off")


plt.tight_layout()

plt.show()

print("==========================================")
print("✅ MULTI THRESHOLDING BERHASIL")
print("==========================================")

print("Input:")
print(input_filename)

print()

print("Threshold 1 :", T1)
print("Threshold 2 :", T2)

print()

print("Hasil disimpan di:")

print(output_path)

print("==========================================")

input("\nTekan ENTER untuk selesai...")