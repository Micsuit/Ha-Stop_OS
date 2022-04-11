"""
Hex Viewer made in Python. Used to open files.
"""

from textwrap import wrap
from sysINF.SYS_INF import type_stor
from errors.system_error import *
import os
from applications.hxvw import database_hex
from time import strftime
from applications.hxvw import version_program

def hxvw_main(file):
    FILESIZE_LIMIT = 65535 # Bytes
    file_size_byte = os.path.getsize(file)
    print(f"\n============================ Hex Viewer {version_program.version} ============================\n")
    print(f"File size: {type_stor.convert_show(os.path.getsize(file))}")
    if file_size_byte > FILESIZE_LIMIT: print(FileTooLarge().str_return()); return -1
    else:
        with open(file, "rb") as f:
            HXDTRW = f.read().hex()
            HXDTLT = wrap(HXDTRW, 2)
            HXDTLT_text = HXDTLT.copy()
            HXDTLN = 0
            for n, i in enumerate(HXDTLT):
                if i.upper() in database_hex.HEX_NOT_TEXT:
                    HXDTLT_text[n] = "2e" # 2e = "."
            HXDTOT = "\n[00000000]   "
            HXDTOT_no_text = "\n[00000000]   "
            HXDTTT_decoded = ""
            hex_line = 0

            for i in range(len(HXDTLT)):
                i1 = i + 1
                HXDTLN += 3
                HXDTOT += HXDTLT[i] + " "
                HXDTOT_no_text += HXDTLT [i] + " "
                HXDTTT_decoded += bytearray.fromhex(HXDTLT_text[i]).decode("ansi", errors="ignore")
                if i1 % 16 == 0 and i != 0 or i+1 == len(HXDTLT):
                    if i+1 == len(HXDTLT):
                        HXDTOT += " " * ((16*3+3)-HXDTLN)
                        HXDTOT_no_text += " " * ((16*3+3)-HXDTLN)
                        HXDTOT += HXDTTT_decoded + "\n"
                    else:
                        HXDTOT += " "*3
                        HXDTOT_no_text += " "*3
                        hex_line += 16
                        HXDTLN = 0
                        HXDTOT += HXDTTT_decoded
                        HXDTTT_decoded = ""
                        HXDTOT += "\n"
                        HXDTOT_no_text += "\n"
                        HXDTOT += "[" + "0" * (8 - len(str(hex(hex_line)[2:]))) + str(hex(hex_line)[2:]) + "]   "
                        HXDTOT_no_text += "[" + "0" * (8 - len(str(hex(hex_line)[2:]))) + str(hex(hex_line)[2:]) + "]   "
        print(HXDTOT)
        

        user_info_file = input("Do you want to save the output in a file? (Y)es or (N)o: ")

        if user_info_file.lower().strip() == "y":
            with open(f"{file} + _trace{strftime('%H%M%S')}.txt", "w") as file_trace:
                file_trace.write(f"File created by Hex Viewer at {strftime('%H:%M:%S')}...\n\n {HXDTOT_no_text}")
            print(f"Output saved in {os.getcwd()}\\{file}_trace.txt")
