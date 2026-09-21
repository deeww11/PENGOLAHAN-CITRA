import numpy as np


def hitung_statistik(citra, jenis_citra):

    if jenis_citra in ["biner", "grayscale"]:

        data_pixel = np.array(citra)

        mean = np.mean(data_pixel)

        variansi = np.var(data_pixel)

        standar_deviasi = np.std(data_pixel)

        hasil = {
            "mean": mean,
            "variansi": variansi,
            "standar_deviasi": standar_deviasi
        }

        return hasil

    elif jenis_citra == "rgb":

        data_pixel = np.array(citra)

        # Jika citra RGB memiliki 3 channel
        mean_r = np.mean(data_pixel[:, :, 0])
        mean_g = np.mean(data_pixel[:, :, 1])
        mean_b = np.mean(data_pixel[:, :, 2])

        variansi_r = np.var(data_pixel[:, :, 0])
        variansi_g = np.var(data_pixel[:, :, 1])
        variansi_b = np.var(data_pixel[:, :, 2])

        standar_r = np.std(data_pixel[:, :, 0])
        standar_g = np.std(data_pixel[:, :, 1])
        standar_b = np.std(data_pixel[:, :, 2])

        hasil = {
            "mean": {
                "R": mean_r,
                "G": mean_g,
                "B": mean_b
            },

            "variansi": {
                "R": variansi_r,
                "G": variansi_g,
                "B": variansi_b
            },

            "standar_deviasi": {
                "R": standar_r,
                "G": standar_g,
                "B": standar_b
            }
        }

        return hasil


def tampilkan_statistik(hasil, jenis_citra):

    print("\n===================================")
    print("        HASIL STATISTIK CITRA")
    print("===================================")

    if jenis_citra in ["biner", "grayscale"]:

        print(f"Mean              : {hasil['mean']:.2f}")

        print(f"Variansi          : {hasil['variansi']:.2f}")

        print(
            f"Standar Deviasi   : "
            f"{hasil['standar_deviasi']:.2f}"
        )


    # ==========================================
    # RGB
    # ==========================================

    elif jenis_citra == "rgb":

        print("\n--- MEAN ---")

        print(f"Red   : {hasil['mean']['R']:.2f}")

        print(f"Green : {hasil['mean']['G']:.2f}")

        print(f"Blue  : {hasil['mean']['B']:.2f}")


        print("\n--- VARIANSI ---")

        print(f"Red   : {hasil['variansi']['R']:.2f}")

        print(f"Green : {hasil['variansi']['G']:.2f}")

        print(f"Blue  : {hasil['variansi']['B']:.2f}")


        print("\n--- STANDAR DEVIASI ---")

        print(
            f"Red   : "
            f"{hasil['standar_deviasi']['R']:.2f}"
        )

        print(
            f"Green : "
            f"{hasil['standar_deviasi']['G']:.2f}"
        )

        print(
            f"Blue  : "
            f"{hasil['standar_deviasi']['B']:.2f}"
        )


    print("===================================")