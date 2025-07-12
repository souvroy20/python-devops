# single function approach
import subprocess

directory = "terraform-project"


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
        ("Terraform Format Check",
         f"terraform -chdir={directory} fmt -check -recursive"),  # ✅ format
        ("TFLint", f"tflint {directory}"),  # ✅ lint
        ("Init", f"terraform -chdir={directory} init -upgrade"),
        ("Validate", f"terraform -chdir={directory} validate"),
        ("Refresh", f"terraform -chdir={directory} refresh"),
        ("Plan", f"terraform -chdir={directory} plan"),
        ("Apply", f"terraform -chdir={directory} apply -auto-approve"),
    ]

    for name, command in steps:
        success = run_terraform_command(name, command)
        if not success:
            break
    print("\n🔚 All steps completed.")


# import subprocess


# # directory = r"C:\IMPORTANT\PTHN_DEVOPS\terraform-project"
# directory = "terraform-project"


# # init
# def init_terraform_command(command):

#     result = subprocess.run(command, shell=True,
#                             capture_output=True, text=True)
#     if result.returncode != 0:
#         return f"Error: {result.stderr}"
#     return result.stdout


# init_command = f"terraform -chdir={directory} init"
# init = init_terraform_command(init_command)
# print(init)

# # plan


# def plan_terraform_command(command):

#     result = subprocess.run(command, shell=True,
#                             capture_output=True, text=True)
#     if result.returncode != 0:
#         return f"Error: {result.stderr}"
#     return result.stdout


# plan_command = f"terraform -chdir={directory} plan"
# plan = plan_terraform_command(plan_command)
# print(plan)

# # apply


# def apply_terraform_command(command):

#     result = subprocess.run(command, shell=True,
#                             capture_output=True, text=True)
#     if result.returncode != 0:
#         return f"Error: {result.stderr}"
#     return result.stdout


# apply_command = f"terraform -chdir={directory} apply -auto-approve"
# apply = apply_terraform_command(apply_command)
# print(apply)


# # destroy command
# # def destroy_terraform_command(command):

# #     result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# #     if result.returncode != 0:
# #         return f"Error: {result.stderr}"
# #     return result.stdout

# # destroy_command = f"terraform -chdir={directory} destroy -auto-approve"
# # destroy= destroy_terraform_command(destroy_command)
# # print(destroy)

# ################################
