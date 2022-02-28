import sys, time, os
from sysINF.SYS_INF import *
from errors.system_error import *
import time

SHUTDOWN = "shutdown" # shutdown the system
GOTO = "goto" # go to folder, "cd" in cmd
CREATEFILE = "createfil" # create a file
CREATEFOLDER = "createfol" # create a folder
DELETEFILE = "deletefil" # delete a file
DELETEFOLDER = "deletefol" # delete a folder
FILESINFOLDER = "filfol" # make a list of files (and folders) in the current folder, "dir" in cmd
WRITESCREEN = "writescrn" # write a message in the screen, "echo" in cmd
OPEN = "open" # open a file
GETSTATSPC = "statspc" # get stats from pc, like ram, cpu and etc...
DATETIME = "datime" # Get current date and time
COPY = "copy" # copy files and folders to another directories (probably is only being added in a future ver)
HELP = "help" # Get commands available

cmd_help = {SHUTDOWN: "Shutdown the system",
            GOTO: "Go to a folder",
            CREATEFILE: "Create a file",
            CREATEFOLDER: "Create a folder", 
            DELETEFILE: "Delete a folder", 
            FILESINFOLDER: "Make a list of files and folders in the current folder",
            WRITESCREEN: "Write a message on to the screen",
            OPEN + " (to do)": "Open a file",
            GETSTATSPC: "Get stats from pc, like RAM, CPU...",
            DATETIME: "Get current date and time",
            COPY + " (to do)": "Copy files or folders to another directories",
            HELP: "Get all commands available"}

def shutdown_cm():
    print(f"Turning off {SYSTEM_NAME}...")
    time.sleep(3)
    sys.exit()
    
def goto_cm(folder, curr_dir):
    error = None
    if curr_dir == "H:" and folder == "..":
        pass
    elif os.path.exists(folder):
        if os.path.isdir(folder):
            os.chdir(folder)
        else:
            error = IsFileError(folder)
    else:
        error = FolderWasNotFound(folder)
        
    if error: return error.str_return()
    else: return None

def createfile_cm(file):
    error = None
    try:
        with open(r"{}".format(file), "x") as fich_open:
            fich_open.close()
    except FileExistsError:
        error = FileAlreadyExists(file)
    
    if error: return error.str_return()
    else: return None

def createfolder_cm(folder):
    error = None
    if os.path.isdir(folder) or os.path.isfile(folder):
        error = FolderAlreadyExists(folder)
    else:
        os.mkdir(folder)
        
    if error: return error.str_return()
    else:
        return None

def delfile_cm(file):
    error = None
    if os.path.exists(file):
        if os.path.isfile(file):
            try:
                os.remove(file)
            except:
                error = UnknownError("Error removing file...")
        else:
            error = IsFolderError(file)
    else:
        error = FileWasNotFound(file)
        
    if error: return error.str_return()
    else: return None

def delfolder_cm(folder):
    error = None
    if os.path.exists(folder):
        if os.path.isdir(folder):
            try:
                os.rmdir(folder)
            except:
                error = UnknownError("Error removing folder...")
        else:
            error = IsFileError(folder)
    else:
        error = FolderWasNotFound(folder)
        
    if error: return error.str_return()
    else: return None

def filfol_cm(curr_folder):
    print(f"Files and folders in \"{curr_folder}\":")
    
    base_files_data = os.listdir()
    
    for flrfol in base_files_data:
        flrfol_size = type_stor.convert_show(os.path.getsize(flrfol))
        flrfol_date = time.strftime('%d/%m/%Y', time.localtime(os.path.getmtime(flrfol)))
        
        if os.path.isfile(flrfol): print(f"\n     - {flrfol} | {flrfol_size} | {flrfol_date} | FILE")
        else: print(f"\n     - {flrfol} | {flrfol_date} | FOLDER")

def writescreen_cm(msg_to_wrt):
    if msg_to_wrt: print(msg_to_wrt)
    else: print("")
    
def getstatspc_cm():
    print("="*25 + " System Information " + "="*25)
    print(f"""\n[System Parameters]\n\nSystem Name: {SYSTEM_NAME}\n\
System Version: {SYSTEM_VER}\n\
Year the system was created: {YEAR_MADE}\n\
System Creator: {AUTHOR}\n\
System Disk: {SYSTEM_DISK_FOLDER}\n\n[System Specs]\n\n\
RAM: {PC_RAM}\n\
CPU: {PC_CPU}\n\
Storage: {SYS_STORAGE}\n""")
    print("="*25 + " System Information " + "="*25)

def datetime_cm():
    print(f"Current date: {time.strftime('%d/%m/%Y %H:%M:%S')}")

def help_cm():
    print("List of all commands:")
    for key, value in cmd_help.items():
        print(f"\n  - {key.upper()}: {value}")

def open_file_cm():
    pass
    
