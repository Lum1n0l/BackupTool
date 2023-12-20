# Script to prompt user for paths to files to be backed up - then build out a .txt list of directories to be fed into backuptool. 

try:
    import sys
    def build_srcfile():
        print("Lets Choose What To Backup....")

        with open ("src_dirs.txt", "w") as file:
            while True:
                src_dir = input("Please Enter The Absolute Path To The Folder You Wish To Backup: \n")
                file.write(src_dir + "\n")
                if input("Add Another Directory? Y/N \n") == "N":
                    break

        print("Directories Saved To src_dirs.txt")
        print("Please Run backuptool.py To Backup Your Files")
        sys.exit()
except Exception as e:
    print(f"Error: {e}")
    pass