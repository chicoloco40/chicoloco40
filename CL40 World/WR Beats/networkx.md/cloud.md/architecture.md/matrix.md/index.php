import networkx as nx
import plotly.graph_objects as go

# 1. Initialize System Matrix Graph
G = nx.DiGraph()

# 2. Define System Layers and Core Entities (Layer: [Nodes])
layers = {
    0: ["CL40 World Syndicate", "WR Beats International"],
    1: ["Global Sovereign Pipeline"],
    2: ["Infrastructure Core", "Owner Authorization"],
    3: ["Global Node Integration"],
    4: ["Data Architecture"],
    5: ["Data Analytics", "Python 3D", "InChI Molecular Sync"],
    6: ["High-Velocity Processing"],
    7: ["Execution Layer Matrix"],
    8: ["Eye 👁️ For An Eye", "Universal Conciencia"],
    9: ["Global Harmonization Hub"],
    10: ["Level +1: Sovereign Verification Protocol"],
    11: ["Level +2: Quantum Ledger Distribution"],
    12: ["Level +3: Regional Settlement Gateways"],
    13: ["Euro-Zone", "APAC-Pacific", "Americas Core"],
    14: ["Level +5: Localized Edge Telemetry"],
    15: ["Level +6: Terminal Impact Endpoints"],
    16: ["CL40 Sovereign Foundation"]
}

# 3. Establish System Routing Edges
edges = [
    ("CL40 World Syndicate", "Global Sovereign Pipeline"),
    ("WR Beats International", "Global Sovereign Pipeline"),
    ("Global Sovereign Pipeline", "Infrastructure Core"),
    ("Global Sovereign Pipeline", "Owner Authorization"),
    ("Infrastructure Core", "Global Node Integration"),
    ("Owner Authorization", "Global Node Integration"),
    ("Global Node Integration", "Data Architecture"),
    ("Data Architecture", "Data Analytics"),
    ("Data Architecture", "Python 3D"),
    ("Data Architecture", "InChI Molecular Sync"),
    ("Data Analytics", "High-Velocity Processing"),
    ("Python 3D", "High-Velocity Processing"),
    ("InChI Molecular Sync", "High-Velocity Processing"),
    ("High-Velocity Processing", "Execution Layer Matrix"),
    ("Execution Layer Matrix", "Eye 👁️ For An Eye"),
    ("Execution Layer Matrix", "Universal Conciencia"),
    ("Eye 👁️ For An Eye", "Global Harmonization Hub"),
    ("Universal Conciencia", "Global Harmonization Hub"),
    ("Global Harmonization Hub", "Level +1: Sovereign Verification Protocol"),
    ("Level +1: Sovereign Verification Protocol", "Level +2: Quantum Ledger Distribution"),
    ("Level +2: Quantum Ledger Distribution", "Level +3: Regional Settlement Gateways"),
    ("Level +3: Regional Settlement Gateways", "Euro-Zone"),
    ("Level +3: Regional Settlement Gateways", "APAC-Pacific"),
    ("Level +3: Regional Settlement Gateways", "Americas Core"),
    ("Euro-Zone", "Level +5: Localized Edge Telemetry"),
    ("APAC-Pacific", "Level +5: Localized Edge Telemetry"),
    ("Americas Core", "Level +5: Localized Edge Telemetry"),
    ("Level +5: Localized Edge Telemetry", "Level +6: Terminal Impact Endpoints"),
    ("Level +6: Terminal Impact Endpoints", "CL40 Sovereign Foundation")
]

G.add_edges_from(edges)

# 4. Programmatic 3D Coordinate Mapping Generator
pos_3d = {}
for depth, nodes in layers.items():
    z_coord = 100 - (depth * 6)  # Strict descending vertical execution plane
    num_nodes = len(nodes)
    for i, node in enumerate(nodes):
        if num_nodes == 1:
            x_coord, y_coord = 0.0, 0.0
        else:
            x_coord = (i - (num_nodes - 1) / 2.0) * 5.0
            y_coord = ((i % 2) - 0.5) * 2.5  # Staggered offset depth alignment
        pos_3d[node] = (x_coord, y_coord, z_coord)

# 5. Extract Structural Data for Rendering Pipelines
edge_x, edge_y, edge_z = [], [], []
for edge in G.edges():
    x0, y0, z0 = pos_3d[edge[0]]
    x1, y1, z1 = pos_3d[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_z.extend([z0, z1, None])

node_x, node_y, node_z = [], [], []
node_text, node_color, node_size = [], [], []

for node in G.nodes():
    x, y, z = pos_3d[node]
    node_x.append(x)
    node_y.append(y)
    node_z.append(z)
    node_text.append(f"<b>Node:</b> {node}<br>Layer Level: Z={z}")
    
    # Stratify layout highlights (Neon Cyan vs Cyber Blue)
    if any(keyword in node for keyword in ["Level", "Global", "Sovereign"]):
        node_color.append("#00FFCC")
        node_size.append(14)
    else:
        node_color.append("#3366FF")
        node_size.append(10)

# 6. Assemble Plotly Visual Components
edge_trace = go.Scatter3d(
    x=edge_x, y=edge_y, z=edge_z,
    line=dict(color='#444857', width=2),
    hoverinfo='none',
    mode='lines'
)

node_trace = go.Scatter3d(
    x=node_x, y=node_y, z=node_z,
    mode='markers+text',
    text=[node for node in G.nodes()],
    textposition="top center",
    hoverinfo='text',
    hovertext=node_text,
    marker=dict(
        showscale=False,
        colorscale=[[0, '#3366FF'], [1, '#00FFCC']],
        color=node_color,
        size=node_size,
        line=dict(color='#FFFFFF', width=1.5)
    ),
    textfont=dict(size=9, color='#E2E8F0')
)

# 7. Render Layout Configuration
fig = go.Figure(data=[edge_trace, node_trace])
fig.update_layout(
    title=dict(
        text="CL40 World Syndicate | Professional Execution Matrix",
        font=dict(color='#FFFFFF', size=16),
        x=0.5
    ),
    paper_bgcolor='#0B0F19',
    plot_bgcolor='#0B0F19',
    margin=dict(l=0, r=0, b=0, t=50),
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        backgroundcolor='#0B0F19'
    ),
    showlegend=False
)

# To view the interactive console, execute: fig.show()
