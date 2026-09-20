import cv2
import matplotlib.pyplot as plt


def hitung_histogram(citra, jenis_citra):

    if jenis_citra == "biner":

        histogram = cv2.calcHist(
            [citra],
            [0],
            None,
            [256],
            [0, 256]
        )

        return {
            "Biner": histogram.flatten()
        }

    elif jenis_citra == "grayscale":

        histogram = cv2.calcHist(
            [citra],
            [0],
            None,
            [256],
            [0, 256]
        )

        return {
            "Grayscale": histogram.flatten()
        }

    elif jenis_citra == "rgb":


        histogram_b = cv2.calcHist(
            [citra],
            [0],
            None,
            [256],
            [0, 256]
        )

        histogram_g = cv2.calcHist(
            [citra],
            [1],
            None,
            [256],
            [0, 256]
        )

        histogram_r = cv2.calcHist(
            [citra],
            [2],
            None,
            [256],
            [0, 256]
        )

        return {
            "Red": histogram_r.flatten(),
            "Green": histogram_g.flatten(),
            "Blue": histogram_b.flatten()
        }

    else:
        print("Jenis citra tidak dikenali.")
        return None


def tampilkan_histogram(data_histogram, jenis_citra):

    plt.figure(figsize=(10, 5))

    if jenis_citra == "biner":

        plt.plot(
            range(256),
            data_histogram["Biner"],
            color="black"
        )

        plt.title("Histogram Citra Biner")
        plt.xlabel("Nilai Intensitas")
        plt.ylabel("Jumlah Pixel")

    elif jenis_citra == "grayscale":

        plt.plot(
            range(256),
            data_histogram["Grayscale"],
            color="gray"
        )

        plt.title("Histogram Citra Grayscale")
        plt.xlabel("Nilai Intensitas")
        plt.ylabel("Jumlah Pixel")

    elif jenis_citra == "rgb":

        # Channel Red
        plt.plot(
            range(256),
            data_histogram["Red"],
            label="Red",
            color="red"
        )

        # Channel Green
        plt.plot(
            range(256),
            data_histogram["Green"],
            label="Green",
            color="green"
        )

        # Channel Blue
        plt.plot(
            range(256),
            data_histogram["Blue"],
            label="Blue",
            color="blue"
        )

        plt.title("Histogram Citra RGB")
        plt.xlabel("Nilai Intensitas")
        plt.ylabel("Jumlah Pixel")
        plt.legend()

    plt.xlim([0, 255])
    plt.grid()
    plt.show()