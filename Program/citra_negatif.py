import cv2
import numpy as np
import matplotlib.pyplot as plt

gambar = cv2.imread("gambar.jpg")

if gambar is None:
    print("Gambar tidak ditemukan!")
    exit()

gambar_rgb = cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)

citra_negatif = 255 - gambar_rgb

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(gambar_rgb)
plt.title("Gambar Asli")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(citra_negatif)
plt.title("Citra Negatif")
plt.axis("off")

plt.tight_layout()
plt.show()

citra_negatif_bgr = cv2.cvtColor(citra_negatif, cv2.COLOR_RGB2BGR)
cv2.imwrite("hasil_citra_negatif.jpg", citra_negatif_bgr)

print("Citra negatif berhasil dibuat.")
print("Hasil disimpan sebagai: hasil_citra_negatif.jpg")