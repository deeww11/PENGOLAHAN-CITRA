import numpy as np
import matplotlib.pyplot as plt


def normalisasi_histogram(data_histogram):
    """
    Mengubah histogram normal menjadi histogram ternormalisasi.
    """

    histogram_normalisasi = {}

    for nama_channel, histogram in data_histogram.items():
        jumlah_pixel = np.sum(histogram)

        if jumlah_pixel == 0:
            histogram_normalisasi[nama_channel] = histogram
        else:
            histogram_normalisasi[nama_channel] = (
                histogram / jumlah_pixel
            )

    return histogram_normalisasi


def tampilkan_histogram_normalisasi(
    data_histogram_normalisasi,
    jenis_citra
):
    """
    Menampilkan histogram yang sudah ternormalisasi.
    """

    plt.figure(figsize=(10, 5))

    if jenis_citra == "biner":
        plt.plot(
            range(256),
            data_histogram_normalisasi["Biner"]
        )
        plt.title("Histogram Ternormalisasi Citra Biner")

    elif jenis_citra == "grayscale":
        plt.plot(
            range(256),
            data_histogram_normalisasi["Grayscale"]
        )
        plt.title("Histogram Ternormalisasi Citra Grayscale")

    elif jenis_citra == "rgb":
        plt.plot(
            range(256),
            data_histogram_normalisasi["Red"],
            label="Red"
        )

        plt.plot(
            range(256),
            data_histogram_normalisasi["Green"],
            label="Green"
        )

        plt.plot(
            range(256),
            data_histogram_normalisasi["Blue"],
            label="Blue"
        )

        plt.title("Histogram Ternormalisasi Citra RGB")
        plt.legend()

    plt.xlabel("Nilai Intensitas")
    plt.ylabel("Frekuensi")
    plt.xlim([0, 255])
    plt.grid()
    plt.show()