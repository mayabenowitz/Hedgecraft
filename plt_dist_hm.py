import pandas as pd
import numpy as np
import preproc as pre
import detrend as dd
import networkx as nx
import build_corr_nx as bnx
import matplotlib.pyplot as plt
import seaborn as sns
import time_series_nx as tsx


def dist_hm():

    df = dd.detrend()
    df.dropna(inplace=True)
    # builds closing price correlation network
    H = tsx.ts_corr_network(data=df, corr_param='dcor', prune=0.35)
    #H = bnx.build_nx()

    # grabs node labels from H (H.nodes attribute has dtype GraphObject) and appends to a list
    # we'll need to access this list to build the ditance dataframe
    node_list = []
    for nodes in H.nodes:
        node_list.append(nodes)

    # calculates the distance matrix of H with the Floyd-Warshall algorithm
    dist_matrix = nx.floyd_warshall_numpy(H, weight="weight")

    # initializes the distance dataframe with the first column of the distance matrix
    dist_df = pd.DataFrame(np.transpose(dist_matrix[0]), columns=[node_list[0]])

    # creates a new column in the distance dataframe for each stock ticker and preprocesses it for heatmap plotting
    for i in range(len(H.nodes)):
        dist_df[node_list[i]] = pd.DataFrame(np.transpose(dist_matrix[i]))
    dist_df.insert(loc=0, value=pd.DataFrame(node_list), column="Node")
    dist_df.set_index("Node", inplace=True, drop=True)

    # builds colorbar
    cmap = sns.cubehelix_palette(3, as_cmap=True, reverse=True)

    # plots an annotated heatmap (with the seaborn module) of the distance dataframe with the upper triangle masked
    # the distance dataframe is symetric and thus the upper triganle is redundent data ink
    mask = np.zeros_like(dist_df)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        ax = sns.heatmap(
            dist_df,
            xticklabels=dist_df.columns,
            yticklabels=dist_df.columns,
            cmap=cmap,
            annot=True,
            cbar=False,
            mask=mask,
        )
    plt.show()


if __name__ == "__main__":
    dist_hm()
