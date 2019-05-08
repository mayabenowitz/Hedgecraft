import pandas as pd
import numpy as np
import preproc as pre
import detrend as dtr
import networkx as nx
import build_corr_nx as bnx
import matplotlib.pyplot as plt
import seaborn as sns
from networkx.algorithms import approximation


def sandbox_nx():
    H = bnx.build_nx()

    #    paths_ll = []

    #    for u in nodes:
    #        for v in nodes:
    #            if u == v:
    #                pass
    #            else:
    #                paths_ll.append([p for p in nx.all_shortest_paths(H, source=u, target=v)])
    #
    #    paths_l = [p for sublist in paths_ll for p in sublist]
    #
    #    max_len_paths = []
    #
    #    for p in paths_l:
    #        if len(p) == nx.diameter(H) + 1:
    #            max_len_paths.append(p)
    #    print(len(max_len_paths))

    #    paths=[]
    #    for u in H.nodes:
    #        for v in H.nodes:
    #            if u == v:
    #                pass
    #            else:
    #                paths.append([p for p in nx.shortest_path(H, source=u, target=v)])

    preds = nx.preferential_attachment(H)
    df = pd.DataFrame(preds)
    df = df.pivot(index=0, columns=1, values=2)
    print(df)


#    perph = nx.periphery(H)
#    print(perph)

if __name__ == "__main__":
    sandbox_nx()
