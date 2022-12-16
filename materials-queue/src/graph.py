import networkx as nx


graph = nx.nx_agraph.read_dot("roadmap.dot")
print("\nHere is the map information: \n")
print(graph.nodes["london"])