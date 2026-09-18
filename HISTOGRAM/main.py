import cv2
from input_citra import input_citra
from histogram import hitung_histogram, tampilkan_histogram
from normalisasi import (
    normalisasi_histogram,
    tampilkan_histogram_normalisasi
)

def main():

    print("===================================")
    print("       PROGRAM HISTOGRAM CITRA")
    print("===================================")

    citra, jenis_citra = input_citra()

    if citra is None:
        print("\nProgram dihentikan.")
        return

    print("\n===================================")
    print("          INPUT BERHASIL")
    print("===================================")
    print("Jenis citra :", jenis_citra)
    print("Ukuran citra:", citra.shape)

    if jenis_citra == "rgb":

        citra_tampil = cv2.cvtColor(
            citra,
            cv2.COLOR_RGB2BGR
        )

    else:
        citra_tampil = citra

    cv2.imshow(
        "Citra yang Diproses",
        citra_tampil
    )

    print("\nTekan tombol apa saja pada jendela gambar untuk keluar.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("\n===================================")
    print("        PROSES HISTOGRAM")
    print("===================================")

    data_histogram = hitung_histogram(
        citra,
        jenis_citra
    )

    print("Histogram berhasil dihitung.")

    tampilkan_histogram(
        data_histogram,
        jenis_citra
    )

    print("\n===================================")
    print("   HISTOGRAM TERNORMALISASI")
    print("===================================")

    data_histogram_normalisasi = normalisasi_histogram(
        data_histogram
    )

    print("Histogram berhasil dinormalisasi.")

    tampilkan_histogram_normalisasi(
        data_histogram_normalisasi,
        jenis_citra
    )

if __name__ == "__main__":
    main()