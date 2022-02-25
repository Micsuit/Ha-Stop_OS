import sys, time, os
from sysINF import SYS_INF
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
DATETIME = "datime"

def shutdown_cm():
    print(f"Turning off {SYS_INF.SYSTEM_NAME}...")
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
    if os.path.isdir(folder):
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
        flrfol_size = SYS_INF.type_stor.convert_show(os.path.getsize(flrfol))
        flrfol_date = time.strftime('%d/%m/%Y', time.localtime(os.path.getmtime(flrfol)))
        
        if os.path.isfile(flrfol):
            print(f"\n     - {flrfol} | {flrfol_size} | {flrfol_date} | FILE")
        else:
            print(f"\n     - {flrfol} | {flrfol_date} | FOLDER")

def writescreen_cm():
    pass

def open_file_cm():
    pass

def getstatspc_cm():
    pass

def datetime_cm():
    pass
    
