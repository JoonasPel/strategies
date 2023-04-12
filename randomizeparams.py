import random
import pickle

def get_params():
    # defaults
    # params = {
    #     "SHORTING_FEE": 0.0002,  # 0.02% for opening a margin position + 0.02% for every 4 hours
    #     "SHORT_OUT_THRESHOLD": 0.01,  # if 0.01 means out when 1% lower value
    #     "STOP_LOSS_THRESHOLD": 0.01,  # if 0.01 means out when 1% higher value
    #     "MINS_TO_CHECK_FROM_HISTORY": 300,  # how many minutes for data checked for history
    #     "HIST_VALUE_THRESHOLD": 0.10,  # if we find a history value thats X % lower than NOW, we short in.
    #     "SHORT_OUT_TIMEOUT": 66  # how many minutes to wait while we are short IN before going short out WHATEVER value is       
    # }
    
    with open("params.pkl", "rb") as file:
        params = pickle.load(file)
    params["SHORT_OUT_TIMEOUT"] = 126
    # randomly change one param -2% or +2%. DONT CHANGE FEE ! I know this is bad way to do it
    key, value = 0, 0
    while True:
        key, value = random.choice(list(params.items()))
        if key not in {"SHORTING_FEE", "SHORT_OUT_TIMEOUT"}:
            break
    multiplier = random.randint(85, 115) / 100
    new_value = value * multiplier
    # rounding the value depends of what parameter it is
    if key in {"MINS_TO_CHECK_FROM_HISTORY", "SHORT_OUT_TIMEOUT"}:
        params[key] = round(new_value)
    else:
        params[key] = round(new_value, 4)  # not too much decimals to prevent overfit
    print(params)

    # # change in some range. fee not changed
    # params["SHORT_OUT_THRESHOLD"] = random.randrange(2, 30) / 1000
    # params["STOP_LOSS_THRESHOLD"] = random.randrange(2, 30) / 1000
    # params["MINS_TO_CHECK_FROM_HISTORY"] = random.randrange(30, 300)
    # params["HIST_VALUE_THRESHOLD"] = random.randrange(8, 20) / 100
    # params["SHORT_OUT_TIMEOUT"] = random.randrange(20, 200)
    return params

def save_params(params):
    with open("params.pkl", "wb") as file:
        pickle.dump(params, file)
