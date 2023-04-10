# run simulation with values data
def simulation(values, params, ENABLE_PRINTS):
    # save params from dict to variables to make it faster to read them. major difference
    SHORTING_FEE = params["SHORTING_FEE"]
    SHORT_OUT_THRESHOLD = params["SHORT_OUT_THRESHOLD"]
    STOP_LOSS_THRESHOLD = params["STOP_LOSS_THRESHOLD"]
    MINS_TO_CHECK_FROM_HISTORY = params["MINS_TO_CHECK_FROM_HISTORY"]
    HIST_VALUE_THRESHOLD = params["HIST_VALUE_THRESHOLD"]
    SHORT_OUT_TIMEOUT = params["SHORT_OUT_TIMEOUT"]

    total_profit = 0
    i = -1
    length = len(values)
    while i<length-1:
        i += 1
        current_value = values[i]
        short_outted = False
        # make sure we dont try to simulate values too close to edges. they dont have enough hist/futur
        if (i < (MINS_TO_CHECK_FROM_HISTORY + 3) or i > (length - SHORT_OUT_TIMEOUT - 3)):
            continue

        for history_value in values[i-MINS_TO_CHECK_FROM_HISTORY:i]:
            if history_value < current_value * (1 - HIST_VALUE_THRESHOLD):
                # short in for avg price happened. calculate short out price:
                future_values = values[i+1:i+SHORT_OUT_TIMEOUT]
                for val in future_values:
                    # after or is stop loss
                    if val <= (current_value * (1-SHORT_OUT_THRESHOLD)) or \
                        val >= current_value * (1+STOP_LOSS_THRESHOLD):
                        # short out happens
                        profit_from_trade = (current_value - val) - (current_value * SHORTING_FEE)
                        total_profit += profit_from_trade
                        if ENABLE_PRINTS:
                            print(f"""
                            value when short in -> {current_value}
                            value when short out -> {val}
                            \n""")
                        short_outted = True
                        break
                # if didnt find good value to short out. out now with whatever the value is
                if not short_outted:
                    value_at_out = values[i+SHORT_OUT_TIMEOUT+1]
                    profit_from_trade = (current_value - value_at_out) - (current_value * SHORTING_FEE)
                    total_profit += profit_from_trade
                    if ENABLE_PRINTS:
                        print(f"time limit. val in {current_value}, val out {value_at_out}")
                # jump in time so we dont short almost the same opportunity every minute.
                i += MINS_TO_CHECK_FROM_HISTORY
                break
    if ENABLE_PRINTS:
        print(f"profit --> {total_profit}")
    return total_profit
