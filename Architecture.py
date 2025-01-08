import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph for the system architecture
G = nx.DiGraph()

# Define nodes
nodes = {
    "Robot Simulation": (0, 4),
    "Camera Module": (2, 4),
    "Image Processing": (4, 4),
    "Machine Learning Model": (6, 4),
    "Condition Prediction": (8, 4),
    "Database Storage": (6, 2),
    "Chatbot Interface": (4, 2),
    "User Interaction": (2, 2),
}

# Add nodes to the graph
for node, pos in nodes.items():
    G.add_node(node, pos=pos)

# Define edges
edges = [
    ("Robot Simulation", "Camera Module"),
    ("Camera Module", "Image Processing"),
    ("Image Processing", "Machine Learning Model"),
    ("Machine Learning Model", "Condition Prediction"),
    ("Condition Prediction", "Database Storage"),
    ("Condition Prediction", "Chatbot Interface"),
    ("Chatbot Interface", "User Interaction"),
]

# Add edges to the graph
G.add_edges_from(edges)

# Draw the graph
plt.figure(figsize=(12, 6))
pos = nx.get_node_attributes(G, 'pos')
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
    arrowsize=20,
    edge_color="black"
)
plt.title("System Architecture Diagram", fontsize=16)
plt.show()
