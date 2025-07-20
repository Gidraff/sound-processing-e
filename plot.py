"""# plot.py
This script reads data from a file named "plot_output" and generates a plot using matplotlib.
It sets the figure size, layout, and style, then plots the data with specified x and
"""

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

with open("plot_output", encoding="utf-8") as f:
    plt.style.use('dark_background')
    fig, axs = plt.subplots(1, 1)
    NUM_SAMPLES = 441

    lines = f.readlines()[:NUM_SAMPLES]
    y = [float(i.strip()) for i in lines]
    ticks = range(len(lines))

    axs.plot(ticks, y)
    axs.set_xticks(np.arange(0, NUM_SAMPLES, NUM_SAMPLES // 10), np.arange(0, 11, 1))
    axs.set_yticks([-1, -0.5, 0, 0.5, 1])

    plt.ylabel("Amplitude")
    plt.xlabel("Time (ms)")

    plt.show()
