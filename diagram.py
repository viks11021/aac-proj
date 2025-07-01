from diagrams import Diagram
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.network import VPC
from diagrams.gcp.database import SQL

def generate_diagram(components, filename="output/architecture"):
    with Diagram("GCP Architecture", outfilename=filename, show=False):
        nodes = {}
        for c in components:
            if c['type'] == 'compute_instance':
                nodes[c['name']] = ComputeEngine(c['name'])
            elif c['type'] == 'cloudsql':
                nodes[c['name']] = SQL(c['name'])
            elif c['type'] == 'vpc':
                nodes[c['name']] = VPC(c['name'])

        for i in range(len(components) - 1):
            nodes[components[i]['name']] >> nodes[components[i + 1]['name']]