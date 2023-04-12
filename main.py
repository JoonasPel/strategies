import time
import signal
from simulation import simulation
from savedata import save_to_csv
from randomizeparams import get_params, save_params
from readfile import readfile
from drawgraphs import draw_graphs

def handler(signum, frame):
    print("Ctrl C catched, drawing graphs")
    draw_graphs(params_history)
    res = input("input y to exit: ")
    if res == 'y':
        exit(1)

if __name__ == '__main__':
    # catch ctrl C to draw some graphs
    signal.signal(signal.SIGINT, handler)

    # load different crypto data
    data = readfile(0)

    ENABLE_PRINTS = False
    params_history = []  # to draw graphs how params changed over time
    best_profit_so_far = 0.3
    loops_since_best_profit = -1
    i = 0
    while i < 50000:
        params = get_params()

        #t0 = time.time()
        # to simulation to all cryptos loaded
        total_profit = 0
        for crypto_x_values in data:
            normalized_profit = simulation(crypto_x_values, params, ENABLE_PRINTS)
            normalized_profit = round(normalized_profit, 4)
            total_profit += normalized_profit
            print(normalized_profit)
        print(f"total --> {total_profit}")
        # time_elapsed = time.time() - t0
        # if time_elapsed > 35:
        #     print(params)
        #     print(f"time elapsed: {time_elapsed}")

        # if made more profit than best so far, save params used.
        if total_profit > best_profit_so_far:
            print("new best profit")
            params_history.append(list(params.values()))
            save_params(params)
            best_profit_so_far = total_profit
            loops_since_best_profit = 0
        elif loops_since_best_profit != -1:
            loops_since_best_profit += 1

        results = [round(total_profit, 3)] + list(params.values())
        save_to_csv(results)
        print(f"loop {i} done. since best profit: {loops_since_best_profit}")
        i += 1
    