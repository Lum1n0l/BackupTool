import os
import sys
import shutil
import schedule
import time
import datetime

print("Welcome To The Python Backup Tool!")

def backup(source_dir, dest_dir):
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        for source_dir in src_dirs:
            for filename in os.listdir(source_dir):
                src_file = os.path.join(source_dir, filename)
                if os.path.isfile(src_file):
                    dest_file = os.path.join(dest_dir, filename)
                    if os.path.exists(dest_file):
                        if os.path.getmtime(src_file) == os.path.getmtime(dest_file):
                            print(f"Skipping {filename} - File Exists & Unchanged Since Last Backup")
                            continue
                    shutil.copy2(src_file, dest_file)
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

