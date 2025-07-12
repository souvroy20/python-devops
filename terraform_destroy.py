import subprocess

# directory = r"C:\IMPORTANT\PTHN_DEVOPS\terraform-project"
directory = "terraform-project"


def destroy_terraform_command(command):

    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout


destroy_command = f"terraform -chdir={directory} destroy -auto-approve"
destroy = destroy_terraform_command(destroy_command)
print(destroy)
