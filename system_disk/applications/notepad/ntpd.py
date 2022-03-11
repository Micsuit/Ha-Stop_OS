"""
Used to open .txt files in the system.
Currently empty lol
"""

from errors.system_error import *

def read_file(file):
    print("\n\n\nText:")
    with open(file, "r") as file_read:
        print(f"\"{file_read.read()}\"")
            
            
def write_file(file):
    pass


def append_file(file):
    pass

def open_file(file):
    argv_user = input("(R)ead, (W)rite or (A)ppend? ")
    if argv_user.strip().lower() == "r": read_file(file)
    elif argv_user.strip().lower() == "w": write_file(file)
    elif argv_user.strip().lower() == "a": append_file(file)
    else: ArgvNotIdentified().show_warning(); read_file(file)
    

if __name__ == "__main__":
    print("Don't open this application from main!\nRun it trough your system.")
    