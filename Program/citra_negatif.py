
import cv2
import os
import matplotlib.pyplot as plt

# Lokasi gambar input
path_gambar = os.path.join(
    "DATASET GAMBAR 1",
    "Images",
    "0a64655c-4052-4e5f-a696-2a6cf25d10c9___GCREC_Bact.Sp 6017.JPG"
)

# Folder untuk menyimpan hasil
folder_output = "HASIL_CITRA_NEGATIF"
os.makedirs(folder_output, exist_ok=True)

# Hapus hasil gambar sebelumnya
for nama_lama in os.listdir(folder_output):
    path_lama = os.path.join(folder_output, nama_lama)

    if os.path.isfile(path_lama):
        os.remove(path_lama)

print("Hasil citra negatif sebelumnya telah dihapus.")

# Membaca gambar
gambar = cv2.imread(path_gambar)

if gambar is None:
    print(f"Gagal membaca gambar: {path_gambar}")
    exit()

# Mengubah gambar menjadi citra negatif
citra_negatif = 255 - gambar

# Menyimpan hasil citra negatif
nama_file = os.path.basename(path_gambar)
path_hasil = os.path.join(
    folder_output,
    f"negatif_{nama_file}"
)

berhasil = cv2.imwrite(path_hasil, citra_negatif)

if not berhasil:
    print("Gagal menyimpan hasil citra negatif!")
    exit()

print("Berhasil mengubah gambar menjadi citra negatif!")
print(f"Hasil disimpan di: {os.path.abspath(path_hasil)}")

# Mengubah format BGR menjadi RGB untuk visualisasi
gambar_asli_rgb = cv2.cvtColor(
    gambar,
    cv2.COLOR_BGR2RGB
)

gambar_negatif_rgb = cv2.cvtColor(
    citra_negatif,
    cv2.COLOR_BGR2RGB
)

# Menampilkan gambar asli dan citra negatif
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gambar_asli_rgb)
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gambar_negatif_rgb)
plt.title("Citra Negatif")
plt.axis("off")

plt.tight_layout()
plt.show()
