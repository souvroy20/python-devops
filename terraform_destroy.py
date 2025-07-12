import subprocess

# directory = r"C:\IMPORTANT\PTHN_DEVOPS\terraform-project"
directory = "terraform-project"


def destroy_terraform_command(command):
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        return f"❌ Error:\n{result.stderr}"
    return result.stdout


if __name__ == "__main__":
    # You can update this to take as input or arg if needed
    directory = "terraform-project"

    init_command = f"terraform -chdir={directory} init"
    destroy_command = f"terraform -chdir={directory} destroy -auto-approve"

    print("🔧 Running Terraform init...")
    init = destroy_terraform_command(init_command)
    print(init)

    print("💥 Running Terraform destroy...")
    destroy = destroy_terraform_command(destroy_command)
    print(destroy)

    if "Error:" not in destroy:
        print("\n Terraform destroy completed successfully!")
    else:
        print("\n Terraform destroy encountered an error.")

# def destroy_terraform_command(command):

#     result = subprocess.run(command, shell=True,
#                             capture_output=True, text=True)
#     if result.returncode != 0:
#         return f"Error: {result.stderr}"
#     return result.stdout

# init_command = f"terraform -chdir={directory} init"
# destroy_command = f"terraform -chdir={directory} destroy -auto-approve"
# init = destroy_terraform_command(init_command)
# print(init)
# destroy = destroy_terraform_command(destroy_command)
# print(destroy)
# print("\nTerraform destroy completed successfully!")

# if __name__ == "__main__":
#     destroy_terraform_command()
