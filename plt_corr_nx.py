import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import build_corr_nx as bcx


def plt_corr_nx():
    H = bcx.build_nx()

    # function to display the network from the correlation matrix
    def show_corr_nx(H):

        # creates a list of the edges of G and their corresponding weights
        edges, weights = zip(*nx.get_edge_attributes(H, "weight").items())

        # draw the network with the Kamada-Kawai path-length cost-function
        pos = nx.kamada_kawai_layout(H)

        # figure size
        plt.figure(figsize=(20, 20))

        # computes the degree (number of connections) of each node
        deg = H.degree

        # list of node names
        nodelist = []
        # list of node sizes
        node_sizes = []

        # iterates over deg and appends the node names and degrees
        for n, d in deg:
            nodelist.append(n)
            node_sizes.append(d)

        # draw nodes
        nx.draw_networkx_nodes(
            H,
            pos,
            node_color="#DA70D6",
            nodelist=nodelist,
            node_size=np.power(node_sizes, 2.5),
            alpha=0.8,
            font_weight="bold",
        )

        # node label styles
        nx.draw_networkx_labels(H, pos, font_size=8, font_family="sans-serif")

        # color map
        cmap = sns.cubehelix_palette(3, as_cmap=True, reverse=True)

        # draw edges
        nx.draw_networkx_edges(
            H,
            pos,
            edge_list=edges,
            style="solid",
            edge_color=weights,
            edge_cmap=cmap,
            edge_vmin=min(weights),
            edge_vmax=max(weights),
        )

        # builds a colorbar
        sm = plt.cm.ScalarMappable(
            cmap=cmap, norm=plt.Normalize(vmin=min(weights), vmax=max(weights))
        )
        sm._A = []
        plt.colorbar(sm)

        # displays network without axes
        plt.axis("off")
        # plt.savefig('dija_correlation_network.jpg')
        plt.show()

    return show_corr_nx(H)


if __name__ == "__main__":
    plt_corr_nx()
