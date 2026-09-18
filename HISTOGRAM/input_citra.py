import cv2
import os
import random


def ambil_gambar_otomatis():

    folder_dataset = "../DATASET GAMBAR"

    daftar_gambar = [
        file for file in os.listdir(folder_dataset)
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
    ]

    if not daftar_gambar:
        print("Tidak ada gambar di dalam folder dataset.")
        return None

    nama_file = random.choice(daftar_gambar)

    path_gambar = os.path.join(
        folder_dataset,
        nama_file
    )

    citra = cv2.imread(path_gambar)

    if citra is None:
        print("Gambar gagal dibaca.")
        return None

    print("\n=== INPUT CITRA ===")
    print("Gambar yang diambil secara otomatis:", nama_file)

    return citra


def pilih_jenis_citra(citra):
    print("\n=== PILIH JENIS CITRA ===")
    print("1. Citra Biner")
    print("2. Citra Grayscale")
    print("3. Citra Berwarna (RGB)")

    while True:
        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":

            grayscale = cv2.cvtColor(
                citra,
                cv2.COLOR_BGR2GRAY
            )

            _, citra_biner = cv2.threshold(
                grayscale,
                127,
                255,
                cv2.THRESH_BINARY
            )

            print("Jenis citra: Biner")

            return citra_biner, "biner"

        elif pilihan == "2":

            citra_grayscale = cv2.cvtColor(
                citra,
                cv2.COLOR_BGR2GRAY
            )

            print("Jenis citra: Grayscale")

            return citra_grayscale, "grayscale"

        elif pilihan == "3":

            citra_rgb = cv2.cvtColor(
                citra,
                cv2.COLOR_BGR2RGB
            )

            print("Jenis citra: RGB")

            return citra_rgb, "rgb"

        else:
            print(
                "Pilihan tidak tersedia. "
                "Silakan pilih 1, 2, atau 3."
            )


def input_citra():

    citra = ambil_gambar_otomatis()

    if citra is None:
        return None, None

    citra, jenis_citra = pilih_jenis_citra(citra)

    return citra, jenis_citra