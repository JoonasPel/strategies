import matplotlib.pyplot as plt

def draw_graphs(params_history):
    
    # SHORT_OUT_THRESHOLD graph
    y_points = [row[1] for row in params_history]
    x_points = list(range(len(y_points)))
    plt.scatter(x_points, y_points)
    plt.title("SHORT_OUT_THRESHOLD")
    plt.show()

    # STOP_LOSS_THRESHOLD graph
    y_points = [row[2] for row in params_history]
    x_points = list(range(len(y_points)))
    plt.scatter(x_points, y_points)
    plt.title("STOP_LOSS_THRESHOLD")
    plt.show()

    # MINS_TO_CHECK_FROM_HIS graph
    y_points = [row[3] for row in params_history]
    x_points = list(range(len(y_points)))
    plt.scatter(x_points, y_points)
    plt.title("MINS_TO_CHECK_FROM_HIS")
    plt.show()

    # HIST_VALUE_THRESHOLD graph
    y_points = [row[4] for row in params_history]
    x_points = list(range(len(y_points)))
    plt.scatter(x_points, y_points)
    plt.title("HIST_VALUE_THRESHOLD")
    plt.show()

    # SHORT_OUT_TIMEOUT graph
    y_points = [row[5] for row in params_history]
    x_points = list(range(len(y_points)))
    plt.scatter(x_points, y_points)
    plt.title("SHORT_OUT_TIMEOUT")
    plt.show()
