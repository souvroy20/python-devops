# Single funtion to handle all commands
import subprocess

# directory = r"C:\IMPORTANT\PTHN_DEVOPS\terraform-project"
directory = "terraform-project"


def execute_terraform_command(command, description):
    print(f"\n{description}...")
    result = subprocess.run(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"Error: {result.stderr}")


init_command = f"terraform -chdir={directory} init"
plan_command = f"terraform -chdir={directory} plan"
apply_command = f"terraform -chdir={directory} apply -auto-approve"

execute_terraform_command(init_command, "Initializing Terraform")
execute_terraform_command(plan_command, "Planning Terraform")
execute_terraform_command(apply_command, "Applying Terraform")
