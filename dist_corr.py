import pandas as pd
import numpy as np
import preproc as pre
import detrend as dtr
import networkx as nx
import dcor

# TODO: develop distance correlation network


def dist_corr():
    df = dtr.detrend()
    df.dropna(inplace=True)

    # store the column names as a list
    col_names = df.columns.tolist()

    df_dcor = pd.DataFrame(index=col_names, columns=col_names)

    k = 0
    for i in col_names:

        v1 = df.loc[:, i].values
        for j in col_names[k:]:

            v2 = df.loc[:, j].values
            rez = dcor.distance_correlation(v1, v2)
            df_dcor.at[i, j] = rez
            df_dcor.at[j, i] = rez
        k += 1

    return df_dcor


if __name__ == "__main__":
    dist_corr()
