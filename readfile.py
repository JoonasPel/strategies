import csv
import os
import numpy as np

def readfile(skip_x_rows):
    print("Loading data...")
    files = os.listdir("crypto_data/")
    csv_files = list(filter(lambda f: f.endswith('.csv'), files))

    for file_name in csv_files:
        print(f"opening {file_name} ")
        file = open('crypto_data/' + file_name)
        # first row should be url that we skip. if not, raise error.
        if file.readline() != "https://www.CryptoDataDownload.com\n":
            raise NameError("first row of csv files is not url")
        csv_reader = csv.DictReader(file, delimiter=',')
        values = np.empty((0, 1), float)
        r = 0
        for row in csv_reader:
            r += 1
            if r < skip_x_rows:
                continue
            values = np.append(values, float(row['open']))
        values = np.flip(values, axis=0)
        file.close()
        print("data loading done")
        return values