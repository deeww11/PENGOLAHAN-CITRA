import cv2
import os
import random


# ==========================================
# MENENTUKAN LOKASI FOLDER DATASET
# ==========================================

folder_histogram = os.path.dirname(
    os.path.abspath(__file__)
)

folder_project = os.path.dirname(
    folder_histogram
)

folder_dataset = os.path.join(
    folder_project,
    "DATASET GAMBAR"
)


# ==========================================
# MENGAMBIL GAMBAR SECARA OTOMATIS
# ==========================================

def ambil_gambar_otomatis():

    daftar_gambar = [
        file for file in os.listdir(folder_dataset)
        if file.lower().endswith(
            (".jpg", ".jpeg", ".png", ".bmp")
        )
    ]

    if not daftar_gambar:

        print(
            "Tidak ada gambar di dalam "
            "folder DATASET GAMBAR."
        )

        return None


    # Memilih satu gambar secara acak
    nama_file = random.choice(
        daftar_gambar
    )


    path_gambar = os.path.join(
        folder_dataset,
        nama_file
    )


    citra = cv2.imread(
        path_gambar
    )


    if citra is None:

        print("Gambar gagal dibaca.")

        return None


    print("\n===================================")
    print("           INPUT CITRA")
    print("===================================")

    print(
        "Gambar yang diambil secara otomatis:",
        nama_file
    )


    return citra


# ==========================================
# MEMILIH JENIS CITRA
# ==========================================

def pilih_jenis_citra(citra):

    print("\n===================================")
    print("        PILIH JENIS CITRA")
    print("===================================")

    print("1. Citra Biner")
    print("2. Citra Grayscale")
    print("3. Citra Berwarna (RGB)")


    while True:

        pilihan = input(
            "\nMasukkan pilihan: "
        )


        # ==================================
        # CITRA BINER
        # ==================================

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


            print(
                "Jenis citra: Biner"
            )


            return (
                citra_biner,
                "biner"
            )


        # ==================================
        # CITRA GRAYSCALE
        # ==================================

        elif pilihan == "2":

            citra_grayscale = cv2.cvtColor(
                citra,
                cv2.COLOR_BGR2GRAY
            )


            print(
                "Jenis citra: Grayscale"
            )


            return (
                citra_grayscale,
                "grayscale"
            )


        # ==================================
        # CITRA RGB
        # ==================================

        elif pilihan == "3":

            citra_rgb = cv2.cvtColor(
                citra,
                cv2.COLOR_BGR2RGB
            )


            print(
                "Jenis citra: RGB"
            )


            return (
                citra_rgb,
                "rgb"
            )


        else:

            print(
                "Pilihan tidak tersedia. "
                "Silakan pilih 1, 2, atau 3."
            )


# ==========================================
# FUNGSI UTAMA INPUT CITRA
# ==========================================

def input_citra():

    citra = ambil_gambar_otomatis()


    if citra is None:

        return None, None


    citra, jenis_citra = pilih_jenis_citra(
        citra
    )


    return citra, jenis_citra