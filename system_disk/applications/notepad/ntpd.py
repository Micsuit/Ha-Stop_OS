"""
Used to open text files in the system.
"""

import sys
from errors.system_error import *
from applications.notepad import version_program

def is_inv_phr(str_phr) -> bool:
    try: str_phr.encode("ascii")
    except UnicodeEncodeError: return True
    return False

def norm_str(str_nrm) -> str:
    import unicodedata
    text = str(unicodedata.normalize('NFKD', str_nrm).encode('ascii', 'ignore').decode("utf-8"))
    return text
    
    

def read_file(file):
    print("\n\nText:")
    with open(file, "r") as file_read:
        print(f"\"{file_read.read()}\"")
            
            
def write_file(file):
    enter_count = 0
    line_count = 0
    with open(file, "a") as file_write:
        while enter_count < 3:
            line_count += 1
            wrt_line_usr = input(f"Line {line_count}: ")
            if is_inv_phr(wrt_line_usr):
                wrt_line_usr = norm_str(wrt_line_usr)
                InvalidCharacters(wrt_line_usr).show_warning()
                
            if wrt_line_usr == "": enter_count += 1
            else: enter_count = 0; file_write.write(f"\n{wrt_line_usr}")


def append_file(file):
    enter_count = 0
    with open(file, "r") as file_temp:
        list_file = file_temp.readlines() 
    line_count = len(list_file)
    with open(file, "a") as file_append:
        while enter_count < 3:
            line_count += 1
            wrt_line_usr = input(f"Line {line_count}: ")
            if is_inv_phr(wrt_line_usr):
                wrt_line_usr = norm_str(wrt_line_usr)
                InvalidCharacters(wrt_line_usr).show_warning()
            if wrt_line_usr == "": enter_count += 1
            else: enter_count = 0; file_append.write(f"\n{wrt_line_usr}")
        

def open_file(file):
    print(f"\n============================ Notepad {version_program.version} ============================\n")
    argv_user = input("(R)ead, (W)rite or (A)ppend? ")
    if argv_user.strip().lower() == "r": read_file(file)
    elif argv_user.strip().lower() == "w": write_file(file)
    elif argv_user.strip().lower() == "a": append_file(file)
    elif argv_user.strip().lower() == "quit": pass
    elif argv_user == "" or argv_user.isspace(): ArgvNotFound().show_warning(); read_file(file)
    else: ArgvNotIdentified(argv_user).show_warning(); read_file(file)
    

if __name__ == "__main__":
    print("Don't open this application from main!\nRun it trough your system.")
    