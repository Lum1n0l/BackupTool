import os
import sys
import shutil
import schedule
import time
import datetime
import build_srcfile


with open ("banner.txt", "r", encoding='utf-8') as file:
    for line in file:
        print(line.strip())
print("\n\n")
print("Main Menu: \n\n1) Configure Source Directories\n2) Run Backup Script\n3) Exit\n\n")
menu_selection = float(input("Please Select An Option: \n"))

if menu_selection == 1:
    build_srcfile.build_srcfile()
elif menu_selection == 2:
    pass
elif menu_selection == 3:
    sys.exit()


def backup(source_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        for source_dir in src_dirs:
            for filename in os.listdir(source_dir):
                src_file = os.path.join(source_dir, filename)
                dest_file = os.path.join(dest_dir, filename)
                if os.path.isfile(src_file):
                    if os.path.exists(dest_file):
                        if os.path.getmtime(src_file) == os.path.getmtime(dest_file):
                            print(f"Skipping {filename} - File Exists & Unchanged Since Last Backup")
                            continue
                    # deepcode ignore PT: <please specify a reason of ignoring this>
                    shutil.copy2(src_file, dest_file)
                    print(f"Backup Of {filename} Successful At: {time.ctime()}")
                else:
                    if os.path.exists(dest_file):
                        if os.path.getmtime(src_file) == os.path.getmtime(dest_file):
                            print(f"Skipping {filename} - Directory Exists & Unchanged Since Last Backup")
                            continue
                    shutil.copytree(src_file, dest_file)
                    print(f"Backup Of {filename} Successful At: {time.ctime()}")

    except Exception as e:
        print(f"Error during backup: {e}")
        pass

def read_src_directories(file_path):
    with open(file_path, 'r') as file:
        src_dirs = file.read().splitlines()
    return src_dirs

src_dir_file = "src_dirs.txt"
src_dirs = read_src_directories(src_dir_file)
dest_dir = input("Please Enter The Absolute Path To The Folder You Wish To Save Your Backup To: \n")

time_schedule = input("Backup Frequency? (Hourly/Daily/Weekly)")

if time_schedule == "Hourly":
    schedule.every(1).hour.do(backup, src_dirs, dest_dir)
elif time_schedule == "Daily":
    schedule.every(1).day.do(backup, src_dirs, dest_dir)
elif time_schedule == "Weekly":
    schedule.every(7).days.do(backup, src_dirs, dest_dir)
elif time_schedule == "TEST":
    schedule.every(1).minute.do(backup, src_dirs, dest_dir)
else:
    print("Invalid Selection")
    sys.exit()

backup_now = input("Backup Now? Y/N \n")
if backup_now == "Y":
    backup(src_dirs, dest_dir)

while True:
    schedule.run_pending()
    time.sleep(1)

