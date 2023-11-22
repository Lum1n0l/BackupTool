                __________                __              ___________           .__   
                \______   \_____    ____ |  | ____ _______\__    ___/___   ____ |  |  
                |    |  _/\__  \ _/ ___\|  |/ /  |  \____ \|    | /  _ \ /  _ \|  |  
                |    |   \ / __ \\  \___|    <|  |  /  |_> >    |(  <_> |  <_> )  |__
                 |______  /(____  /\___  >__|_ \____/|   __/|____| \____/ \____/|____/
                        \/      \/     \/     \/     |__|   V1.0B - dajtp


A Basic Python Tool For Backing Up Files To Another Location!
This tool can be used to backup your files to any other location on your system. 

## To Use:
    - Open a Terminal/Powershell Session
    - Ensure your have Python installed on your system, preferably >= 3.12.0.
    - Install dependencies via pip - pip install -r requirements.txt
    - Run the build_srcfile.py script to select the directories you wish to backup. 
    - Run the backuptool.py script to select your backup destination & backup frequency. 
    - Leave the script running

The Backup Script will output to the terminal when it backs up your files, it will also skip any files already backed up that haven't been modified since they were last backed up by the script. 

This tool is unfinished, use with caution! 