import shutil
import os
import datetime

def backup_files(source_dir, backup_dir):

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    backup_path = os.path.join(backup_dir, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_path.replace('.tar.gz', ''), 'gztar', source_dir)
    # shutil.make_archive(backup_path.replace('.tar.gz', ''), 'gztar', source_dir)
    print(f"Backup created: {backup_path}")

source_dir = r"C:\IMPORTANT\PTHN_DEVOPS"
backup_dir = r"C:\IMPORTANT\PTHN_DEVOPS\backup"

backup_files(source_dir, backup_dir)
