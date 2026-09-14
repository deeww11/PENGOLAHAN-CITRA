import cv2
import os
import glob
import matplotlib.pyplot as plt

folder_input = "DATASET GAMBAR"

folder_output = "HASIL_GRAYSCALE"

os.makedirs(folder_output, exist_ok=True)

daftar_gambar = glob.glob(os.path.join(folder_input, "*.jpg"))

if len(daftar_gambar) == 0:
    print("Tidak ada gambar ditemukan!")
    exit()

print(f"Jumlah gambar yang ditemukan: {len(daftar_gambar)}")

for i, path_gambar in enumerate(daftar_gambar):

    gambar = cv2.imread(path_gambar)

    if gambar is None:
        print(f"Gagal membaca: {path_gambar}")
        continue

    citra_grayscale = cv2.cvtColor(
        gambar,
        cv2.COLOR_BGR2GRAY
    )

    nama_file = os.path.basename(path_gambar)

    path_hasil = os.path.join(
        folder_output,
        f"grayscale_{nama_file}"
    )

    cv2.imwrite(path_hasil, citra_grayscale)

    print(f"[{i+1}/{len(daftar_gambar)}] Berhasil: {path_hasil}")

gambar_asli = cv2.imread(daftar_gambar[0])

gambar_grayscale = cv2.cvtColor(
    gambar_asli,
    cv2.COLOR_BGR2GRAY
)

gambar_asli_rgb = cv2.cvtColor(
    gambar_asli,
    cv2.COLOR_BGR2RGB
)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gambar_asli_rgb)
plt.title("Gambar Berwarna")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gambar_grayscale, cmap="gray")
plt.title("Citra Grayscale")
plt.axis("off")

plt.tight_layout()
plt.show()

print("\nSemua gambar berhasil diubah menjadi grayscale!")
print(f"Hasil disimpan di folder: {folder_output}")