import random

def get_params():
    # defaults
    params = {
        "SHORTING_FEE": 0.0002,  # 0.02% for opening a margin position + 0.02% for every 4 hours
        "SHORT_OUT_THRESHOLD": 0.01,  # if 0.01 means out when 1% lower value
        "STOP_LOSS_THRESHOLD": 0.01,  # if 0.01 means out when 1% higher value
        "MINS_TO_CHECK_FROM_HISTORY": 300,  # how many minutes for data checked for history
        "HIST_VALUE_THRESHOLD": 0.10,  # if we find a history value thats X % lower than NOW, we short in.
        "SHORT_OUT_TIMEOUT": 66  # how many minutes to wait while we are short IN before going short out WHATEVER value is       
    }
    # change in some range. fee not changed
    params["SHORT_OUT_THRESHOLD"] = random.randrange(2, 30) / 1000
    params["STOP_LOSS_THRESHOLD"] = random.randrange(2, 30) / 1000
    params["MINS_TO_CHECK_FROM_HISTORY"] = random.randrange(30, 300)
    params["HIST_VALUE_THRESHOLD"] = random.randrange(8, 20) / 100
    params["SHORT_OUT_TIMEOUT"] = random.randrange(20, 200)
    return params