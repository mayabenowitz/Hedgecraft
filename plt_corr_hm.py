import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import dist_corr as dc


# TODO plot side-by-side heatmap for detrended and non-detrended time series


def plt_corr_hm():
    df = dc.dist_corr().astype("float")

    cmap = sns.cubehelix_palette(3, as_cmap=True, reverse=True)
    sns.heatmap(df, xticklabels=df.columns, yticklabels=df.columns, cmap=cmap)
    plt.show()


if __name__ == "__main__":
    plt_corr_hm()
