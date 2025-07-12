import subprocess


# directory = r"C:\IMPORTANT\PTHN_DEVOPS\terraform-project"
directory = "terraform-project"


# init
def init_terraform_command(command):

    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout


init_command = f"terraform -chdir={directory} init"
init = init_terraform_command(init_command)
print(init)

# plan


def plan_terraform_command(command):

    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout


plan_command = f"terraform -chdir={directory} plan"
plan = plan_terraform_command(plan_command)
print(plan)

# apply


def apply_terraform_command(command):

    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout


apply_command = f"terraform -chdir={directory} apply -auto-approve"
apply = apply_terraform_command(apply_command)
print(apply)


# destroy command
# def destroy_terraform_command(command):

#     result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#     if result.returncode != 0:
#         return f"Error: {result.stderr}"
#     return result.stdout

# destroy_command = f"terraform -chdir={directory} destroy -auto-approve"
# destroy= destroy_terraform_command(destroy_command)
# print(destroy)

################################
