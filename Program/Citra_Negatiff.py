import cv2
import os
import glob
import matplotlib.pyplot as plt

folder_input = "../DATASET GAMBAR"

folder_output = "../HASIL_CITRA_NEGATIF"

os.makedirs(folder_output, exist_ok=True)

daftar_gambar = glob.glob(
    os.path.join(folder_input, "*.jpg")
)

if len(daftar_gambar) == 0:
    print("Tidak ada gambar ditemukan!")
    exit()

print(f"Jumlah gambar yang ditemukan: {len(daftar_gambar)}")

for i, path_gambar in enumerate(daftar_gambar):

    gambar = cv2.imread(path_gambar)

    if gambar is None:
        print(f"Gagal membaca: {path_gambar}")
        continue

    citra_negatif = 255 - gambar

    nama_file = os.path.basename(path_gambar)

    path_hasil = os.path.join(
        folder_output,
        "negatif_" + nama_file
    )

    cv2.imwrite(path_hasil, citra_negatif)

    print(f"[{i+1}/{len(daftar_gambar)}] Berhasil: {nama_file}")

print("\nSemua gambar berhasil diproses!")
print(f"Hasil disimpan di: {folder_output}")