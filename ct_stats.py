import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import detrend as dtr
import networkx as nx
import build_corr_nx as bnx


def ct_stats():
    # import the correlation network
    H = bnx.build_nx()

    close_ct_d = nx.closeness_centrality(H, distance="weight")
    between_ct_d = nx.betweenness_centrality(H, weight="weight")
    degree_ct_d = nx.degree_centrality(H)
    katz_ct_d = nx.katz_centrality(
        H,
        weight="weight",
        alpha=1 / (max(nx.adjacency_spectrum(H)) + 1),
        beta=close_ct_d,
    )

    degree_ct_s = pd.Series(degree_ct_d).round(3)
    close_ct_s = pd.Series(close_ct_d).round(3)
    between_ct_s = pd.Series(between_ct_d).round(3)
    katz_ct_s = pd.Series(katz_ct_d).round(3).astype("float")

    close_ct_s.reset_index()
    degree_ct_s.reset_index()
    between_ct_s.reset_index()
    katz_ct_s.reset_index()

    degree_ct_df = (
        pd.DataFrame({"stock_rank_1": degree_ct_s.index, "degree": degree_ct_s.values})
        .sort_values(by="degree", ascending=True)
        .reset_index()
        .drop("index", axis=1)
    )

    close_ct_df = (
        pd.DataFrame({"stock_rank_2": close_ct_s.index, "closeness": close_ct_s.values})
        .sort_values(by="closeness", ascending=True)
        .reset_index()
        .drop("index", axis=1)
    )

    between_ct_df = (
        pd.DataFrame(
            {"stock_rank_3": between_ct_s.index, "between": between_ct_s.values}
        )
        .sort_values(by="between", ascending=True)
        .reset_index()
        .drop("index", axis=1)
    )

    katz_ct_df = (
        pd.DataFrame({"stock_rank_4": katz_ct_s.index, "katz": katz_ct_s.values})
        .sort_values(by="katz", ascending=True)
        .reset_index()
        .drop("index", axis=1)
    )

    df1 = degree_ct_df.join(close_ct_df)
    df2 = df1.join(between_ct_df)
    ct_df = df2.join(katz_ct_df)
    return print(ct_df)


if __name__ == "__main__":
    ct_stats()
