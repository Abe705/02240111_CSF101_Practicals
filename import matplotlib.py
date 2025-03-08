import matplotlib.pyplot as plt
import networkx as nx

def create_wbs():
    G = nx.DiGraph()
    
    # Define nodes
    G.add_edges_from([
        ("Auto Motion Light System", "1. Site Selection & Feasibility"),
        ("1. Site Selection & Feasibility", "1.1 Identify locations"),
        ("1. Site Selection & Feasibility", "1.2 Analyze power needs"),
        ("1. Site Selection & Feasibility", "1.3 Environmental factors"),
        
        ("Auto Motion Light System", "2. Planning & Design"),
        ("2. Planning & Design", "2.1 Define requirements"),
        ("2. Planning & Design", "2.2 Create wiring plan"),
        ("2. Planning & Design", "2.3 Select sensors & lights"),
        
        ("Auto Motion Light System", "3. Procurement"),
        ("3. Procurement", "3.1 Purchase sensors"),
        ("3. Procurement", "3.2 Acquire LED lights & wiring"),
        ("3. Procurement", "3.3 Get tools & hardware"),
        
        ("Auto Motion Light System", "4. Installation & Testing"),
        ("4. Installation & Testing", "4.1 Install wiring & power"),
        ("4. Installation & Testing", "4.2 Mount sensors & lights"),
        ("4. Installation & Testing", "4.3 Configure & calibrate"),
        ("4. Installation & Testing", "4.4 Conduct testing & debugging"),
    ])
    
    # Draw the graph
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10, font_weight="bold")
    plt.title("Work Breakdown Structure (WBS) - Auto Motion Light System")
    plt.show()

create_wbs()
