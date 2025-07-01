import os
from parser import load_architecture_config
from generator import generate_component
from diagram import generate_diagram

def main():
    config = load_architecture_config("examples/sample_vm.yaml")
    components = config["app"]["components"]

    output_dir = "output/generated_tf"
    os.makedirs(output_dir, exist_ok=True)

    for comp in components:
        generate_component(comp, output_dir)

    # Write provider.tf
    with open(f"{output_dir}/provider.tf", "w") as f:
        f.write("""provider \"google\" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

terraform {
  required_providers {
    google = {
      source  = \"hashicorp/google\"
      version = \"~> 4.0\"
    }
  }

  required_version = \">= 1.3.0\"
}
""")

    # Write variables.tf
    with open(f"{output_dir}/variables.tf", "w") as f:
        f.write("""variable \"project_id\" {}
variable \"region\" {}
variable \"zone\" {}
""")

    # Write terraform.tfvars
    with open(f"{output_dir}/terraform.tfvars", "w") as f:
        f.write(f"""project_id = \"YOUR_GCP_PROJECT_ID\"
region     = \"{config['app']['region']}\"
zone       = \"{components[0]['zone']}\"
""")

    # Generate architecture diagram
    generate_diagram(components, filename="output/architecture")

if __name__ == "__main__":
    main()
