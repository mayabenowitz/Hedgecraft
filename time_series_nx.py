import numpy as np
import pandas as pd
import networkx as nx
import dcor

#TODO: change 1 - abs(pcor_matrix) to 2(1-pcor_matrix)^0.5
#TODO: add cross correlation
#TODO: raise import error if networkx, dcor, numpy, or pandas not imported
#TODO: raise type error if df has None or NaN values
#TODO: raise type error if data != dataframe
#TODO: raise value error if 'prune' doesn't fall between 0 and 1
#TODO: raise value error if df.columns != df.index
#TODO: add 'method' parameter: method=threshold or method=min_span_tree, let prune -> thresh_val
#TODO: add 'detrend' binary parameter: detrend=True or detrend=False


def ts_corr_network(data, corr_param = 'pcor', prune=0.35):

    if corr_param == "dcor":

        col_names = data.columns.tolist()
        data_dcor = pd.DataFrame(index=col_names, columns=col_names)

        k = 0
        for i in col_names:

            v_i = data.loc[:, i].values
            for j in col_names[k:]:

                v_j = data.loc[:, j].values
                dcor_val = dcor.distance_correlation(v_i, v_j)
                data_dcor.at[i, j] = dcor_val
                data_dcor.at[j, i] = dcor_val
            k += 1

        # converts the dataframe to a matrix (need this to generate the graph from the networkx package)
        dcor_matrix = data_dcor.values.astype("float")
        sim_matrix = 1 - dcor_matrix

        nodes = data_dcor.index.values

        # transforms the similarity matrix into a weighted graph
        G = nx.from_numpy_matrix(sim_matrix)

        # relabel nodes as the stock names
        G = nx.relabel_nodes(G, lambda x: nodes[x])

        # prints the edges with their corresponding weights
        G.edges(data=True)

        # copy correlation network
        H = G.copy()

        # remove self-edges from H (required for graph-theoretic analyses)
        for (u, v) in G.edges:
            if u == v:
                H.remove_edge(u,v)

        if prune != None:
            # removes weakly correlated edges from H
            for (u, v, wt) in G.edges.data("weight"):
                if wt >= 1 - prune:
                    H.remove_edge(u, v)

        return H

    if corr_param == "pcor":

        pcor_matrix = data.iloc[:, 1:].corr()
        nodes = pcor_matrix.index.values

        pcor_matrix = np.asmatrix(pcor_matrix)
        sim_matrix = 1 - abs(pcor_matrix)

        G = nx.from_numpy_matrix(sim_matrix)
        G = nx.relabel_nodes(G, lambda x: nodes[x])
        G.edges(data=True)

        H = G.copy()

        for (u, v) in G.edges:
            if u == v:
                H.remove_edge(u,v)

        if prune != None:
            for (u, v, wt) in G.edges.data("weight"):
                if wt >= 1 - prune:
                    H.remove_edge(u, v)

        return H
