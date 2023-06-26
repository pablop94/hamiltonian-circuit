import networkx as nx
from matplotlib import pyplot as plt


def draw_graph(grafo, path):
    G = nx.Graph()
    G.add_nodes_from(range(len(grafo)))
    for i, row in enumerate(grafo):
        for j, peso in enumerate(row):
            if i != j:
                axis_data = {'weight': peso}

                G.add_edge(i, j, **axis_data)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold')
    colors = nx.get_node_attributes(G, 'color')
    nx.draw_networkx_labels(G, pos, colors)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path,
        edge_color="tab:red",
    )
    plt.savefig(f"resultados/grafo-{len(grafo)}.png")
    plt.close()
