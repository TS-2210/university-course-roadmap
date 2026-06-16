import networkx as nx
import json
def load_module_data():
    with open("module_data.json", "r") as f:
        return json.load(f)

def load_career_data():
    with open("careers.json", "r") as f:
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

def get_skills_for_career(career, career_data):
    for key, val in career_data.items():
        if key == career:
            return val

def score_module(career, career_data, module_data):
    skills = get_skills_for_career(career, career_data)
    scores = {}
    for module in module_data:
        module_skills = module.get("tags", [])
        score = len(set(skills) & set(module_skills))
        scores.update({module["name"]: score})
    desc = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return desc[:3]

def module_roadmap(module_selected, data):
    prereqs = get_prerequisites(module_selected, data)
    y1 = [module for module in prereqs if module[4]=="1"]
    y2 = [module for module in prereqs if module[4]=="2"]
    print("Year 1:", y1)
    print("Year 2:", y2)
    print("Leads to year 3:", module_selected)

data = load_module_data()
career_data = load_career_data()
print(get_prerequisites("Cybersecurity: Principles and Secure Software Systems", data))
print(get_skills_for_career("data scientist", career_data))
print(score_module("cybersecurity engineer", career_data, data))
module_roadmap("Natural Language Processing", data)