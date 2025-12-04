import networkx as nx
from pycliques2 import __version__

print(f"Package Version: {__version__}")
print(f"NetworkX Version: {nx.__version__}")

G = nx.complete_graph(5)
print(f"Graph created: {G}")
