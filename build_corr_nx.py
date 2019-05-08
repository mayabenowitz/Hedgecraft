import pandas as pd
import numpy as np
import preproc as pre
import detrend as dtr
import networkx as nx
import dist_corr as dc

# TODO: develop distance correlation network


def build_nx():
    df = dc.dist_corr()

    # converts the dataframe to a matrix (need this to generate the graph from the networkx package)
    cor_matrix = df.values.astype("float")

    sim_matrix = 1 - cor_matrix

    # transforms the similarity matrix into a weighted graph
    G = nx.from_numpy_matrix(sim_matrix)

    # extracts the indices (i.e., the stock names) from the correlation dataframe
    stocks = df.index.values

    # relabel nodes as the stock names
    G = nx.relabel_nodes(G, lambda x: stocks[x])

    # prints the edges with their corresponding weights
    G.edges(data=True)

    # copy correlation network
    H = G.copy()

    # removes edges from H with data from G
    for (u, v, wt) in G.edges.data("weight"):
        # removes edges with absolute correlations less than or equal to 0.35
        if wt >= 1 - 0.35:
            H.remove_edge(u, v)
        # remove self-edges from H using data from G.
        # this is needed for graph-theoretic analyses
        if u == v:
            H.remove_edge(u, v)

    return H


if __name__ == "__main__":
    build_nx()
