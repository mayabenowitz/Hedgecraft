import pandas as pd
import numpy as np
import preproc as pre
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator
import seaborn as sns


def plt_stocks():
    df = pre.preproc()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    xtick_locator = AutoDateLocator()
    xtick_formatter = AutoDateFormatter(xtick_locator)

    df["UNH"].plot()
    df["NKE"].plot()
    ax.xaxis.set_major_locator(xtick_locator)
    ax.xaxis.set_major_formatter(xtick_formatter)
    plt.show()


if __name__ == "__main__":
    plt_stocks()
