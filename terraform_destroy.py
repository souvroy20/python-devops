import subprocess

# directory = r"C:\IMPORTANT\PTHN_DEVOPS\terraform-project"
DIRECTORY = "terraform-project"


def run_terraform_command(name, command):
    print(f"\n🔹 Running: {name}")
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ {name} failed!\n{result.stderr}")
        return False
    else:
        print(f"✅ {name} succeeded.\n{result.stdout}")
        return True


if __name__ == "__main__":
    steps = [
        ("Init", f"terraform -chdir={DIRECTORY} init -upgrade"),
        ("Destroy", f"terraform -chdir={DIRECTORY} destroy -auto-approve"),
    ]

    for name, command in steps:
        if not run_terraform_command(name, command):
            break
    print("\n🔚 All steps completed.")


# import subprocess

# # directory = r"C:\IMPORTANT\PTHN_DEVOPS\terraform-project"
# directory = "terraform-project"


# def destroy_terraform_command(command):
#     result = subprocess.run(command, shell=True,
#                             capture_output=True, text=True)
#     if result.returncode != 0:
#         return f"❌ Error:\n{result.stderr}"
#     return result.stdout


# if __name__ == "__main__":
#     # You can update this to take as input or arg if needed
#     directory = "terraform-project"

#     init_command = f"terraform -chdir={directory} init"
#     destroy_command = f"terraform -chdir={directory} destroy -auto-approve"

#     print("🔧 Running Terraform init...")
#     init = destroy_terraform_command(init_command)
#     print(init)

#     print("💥 Running Terraform destroy...")
#     destroy = destroy_terraform_command(destroy_command)
#     print(destroy)

#     if "Error:" not in destroy:
#         print("\n Terraform destroy completed successfully!")
#     else:
#         print("\n Terraform destroy encountered an error.")

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
