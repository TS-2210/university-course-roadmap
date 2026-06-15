import networkx as nx
import json
def load_module_data():
    with open("module_data.json", "r") as f:
        return json.load(f)

def get_prerequisites(course, data):
    G = nx.DiGraph()
    prerequisites = []
    for module in data:
        G.add_node(module["name"], code=module["code"], year=module["year"])
        for pre in module.get("prerequisites", []):
            G.add_edge(pre, module["name"])
    if course in G:
        prerequisites = list(nx.ancestors(G, course))
    return prerequisites

data = load_module_data()
print(get_prerequisites("Cybersecurity: Principles and Secure Software Systems", data))
