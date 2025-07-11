import os
import datetime
# Get disk space information (Linux/macOS)
# output = os.system("df -h")

# Get disk space information (Windows)
# output = os.system("dir")

def check_date(command):
    print(os.system(command))

# check_date("date")

def check_dir(command):
    print(os.system(command))

# check_dir("dir")
# Multiple commands can be run using the run_command function.
# def run_command(command):
#     print(os.system(command))
# run_command("dir")
# run_command("systeminfo | find \"Total Physical Memory\"")

def run_command(command):
    return os.system(command)
# run_command("dir")
# run_command("systeminfo | find \"Total Physical Memory\"")

def run_multiple_commands():
      return datetime.datetime.now()
show=run_multiple_commands()
print(show)