import sys
import networkx as nx
import matplotlib.pyplot as plt

edge_path = sys.argv[1]
D = nx.DiGraph()
with open(edge_path) as f:
    for line in f:
        line = line.strip("\n").split(';')
        contr1, contr2, strength = line[0], line[1], line[2]
        D.add_weighted_edges_from([(contr1, contr2, int(strength))])
print("node number:", D.number_of_nodes())
print("edge number:", D.number_of_edges())
nx.draw_networkx(D, pos=nx.random_layout(D), node_color='b', edge_color='r', with_labels=True, node_shape='o', width=0.3, style='solid', font_size=10, node_size=16)
plt.savefig("img/knowledge_transfer.png")
nx.write_gexf(D, 'img/knowledge_transfer.gexf')
plt.show()