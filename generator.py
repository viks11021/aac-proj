import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

def generate_component(component, output_dir):
    template_name = f"{component['type']}.tf.j2"
    template = env.get_template(template_name)
    rendered = template.render(component=component)

    output_path = os.path.join(output_dir, f"{component['type']}.tf")
    with open(output_path, 'w') as f:
        f.write(rendered)


### architecture-as-code/diagram.py

from diagrams import Diagram
from diagrams.gcp.compute import ComputeEngine
from diagrams.gcp.network import VPC
from diagrams.gcp.database import SQL
from diagrams.gcp.iam import ServiceAccount

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
            elif c['type'] == 'sa':
                nodes[c['name']] = ServiceAccount(c['name'])    

        for i in range(len(components) - 1):
            nodes[components[i]['name']] >> nodes[components[i + 1]['name']]