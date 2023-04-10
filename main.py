import time
from simulation import simulation
from savedata import save_to_csv
from randomizeparams import get_params
from readfile import readfile


if __name__ == '__main__':
    print("Loading data...")
    values = readfile(444440)
    print("file openings done")

    ENABLE_PRINTS = False
    i = 0
    while i < 500:
        params = get_params()  

        t0 = time.time()
        profit = simulation(values, params, ENABLE_PRINTS)
        time_elapsed = time.time() - t0
        if time_elapsed > 35:
            print(params)
            print(f"time elapsed: {time_elapsed}")

        data = [round(profit, 3)] + list(params.values())
        save_to_csv(data)
        print(f"loop {i} done")
        i += 1
    