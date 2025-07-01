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
