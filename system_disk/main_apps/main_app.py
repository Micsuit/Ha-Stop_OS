"""
Main CMD program
"""

from sysINF.SYS_INF import *
from errors.system_error import *
import os
from main_apps.command_list import *
import pathvalidate

class command:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}: {self.value}"
        else: return f"{self.type}"

class get_commands:
    def __init__(self, text):
        self.text = text
        self.pos = 1
        self.cmd_str = ""
        if self.text:
            self.current_char = self.text[self.pos - 1]
        else:
            self.text = "  "
            self.current_char = self.text[self.pos - 1]
        self.word = ""

    def only_dots(self, filename) -> bool:
        if filename == len(filename) * filename[0] and filename[0] == ".": return True
        else: return False

    def blank_file(self):
        #len_text = len(self.text)
        #print(f"\"{self.current_char}\", {self.text[self.pos-1:len(self.text)]}, {self.pos}, {len_text}")
        #print([self.current_char == None, self.text[self.pos-1:len(self.text)].isspace(), self.pos == len(self.text)])
        return any([self.current_char == None, self.text[self.pos-1:len(self.text)].isspace(), self.pos-1 == len(self.text)])

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos - 1] if self.pos <= len(self.text) else None

    def get_command(self):
        error = None
        if not self.text.isspace() and not self.text == "":
            while self.current_char in " \t":
                self.advance()
            self.word = self.make_word().lower()
            if self.word == GOTO:
                if self.blank_file():
                    error = FolderNotDefined()
                else:
                    while self.current_char in " \t" and self.pos < len(self.text):
                        self.advance()
                    value = self.make_word()
                    self.cmd_str = command("GOTO", value)
            elif self.word == CREATEFILE:
                if self.blank_file(): error = FileNotDefined()
                else:
                    while self.current_char in " \t" and self.pos < len(self.text):
                        self.advance()
                    value = self.make_word()
                    if pathvalidate.is_valid_filename(value) and not self.only_dots(value):
                        self.cmd_str = command("CREATEFIL", value)
                    else:
                        error = InvalidFileName(value)
            elif self.word == CREATEFOLDER:
                if self.blank_file(): error = FolderNotDefined()
                else:
                    while self.current_char in " \t" and self.pos < len(self.text):
                        self.advance()
                    value = self.make_word()
                    if pathvalidate.is_valid_filepath(value) and not self.only_dots(value):
                        self.cmd_str = command("CREATEFOL", value)
                    else:
                        error = InvalidFolderName(value)
            elif self.word == DELETEFILE:
                if self.blank_file(): error = FileNotDefined()
                else:
                    while self.current_char in " \t" and self.pos < len(self.text):
                        self.advance()
                    value = self.make_word()
                    self.cmd_str = command("DELETEFIL", value)
            elif self.word == DELETEFOLDER:
                if self.blank_file(): error = FolderNotDefined()
                else:
                    while self.current_char in " \t" and self.pos < len(self.text):
                        self.advance()
                    value = self.make_word()
                    self.cmd_str = command("DELETEFOL", value)
            elif self.word == WRITESCREEN:
                self.advance()
                value = self.make_word()
                if value.isspace() or value == "": value = "*Nothing*"
                self.cmd_str = command("WRITESCRN", value)
            elif self.word == OPEN:
                if self.blank_file(): error = FileNotDefined()
                else:
                    while self.current_char in " \t" and self.pos < len(self.text):
                        self.advance()
                    value = self.make_word()
                    self.cmd_str = command("OPEN", value)
            elif self.word == MOVE:
                if self.blank_file(): error = FolderFileNotFoundMove()
                else:
                    while self.current_char in " \t" and self.pos < len(self.text): self.advance()
                    path1 = self.make_word()
                    if path1.isspace() or path1 == "":
                        error = FolderFileNotFoundMove()
                    else:
                        if self.current_char:
                            while self.current_char in " >\t" and self.pos < len(self.text): self.advance()
                        if self.blank_file(): error = FolderFileNotFoundToMove()
                        else:
                            path2 = self.make_word()
                            self.cmd_str = command("MOVE", f"{path1} >>> {path2}")
                
            
            elif self.word == SHUTDOWN:
                self.cmd_str = command("SHUTDOWN")
                    
            elif self.word == FILESINFOLDER:
                self.cmd_str = command("FILFOL")
                
            elif self.word == DATETIME:
                self.cmd_str = command("DATIME")
            
            elif self.word == GETSTATSPC:
                self.cmd_str = command("STATSPC")
                
            elif self.word == HELP:
                self.cmd_str = command("HELP")
                
            elif self.word == CALC:
                self.cmd_str = command("CALC")
                
            
            else:
                error = CommandNotIdentified(self.word)
                        
            return self.cmd_str, error
        
        else:
            return "", error
                    
    def make_word(self):
        not_in, word_text = "", ""
        if self.word in [GOTO, WRITESCREEN, CREATEFOLDER, CREATEFILE, DELETEFILE, DELETEFOLDER, OPEN]: not_in = "\t"
        elif self.word == MOVE: not_in = ">\t"
        else: not_in = " \t"
        
        while self.pos <= len(self.text) and not self.current_char in not_in:
            word_text += self.current_char
            self.advance()

            if not self.current_char: break
        
        return word_text

def int_cmd(cmd):
    global current_dir
    type_cmd = cmd.type.lower()
    #print(type_cmd)
    if cmd.value: value_cmd = cmd.value
    
    if type_cmd == SHUTDOWN: shutdown_cm()
    
    elif type_cmd == GOTO:
        gt = goto_cm(value_cmd, current_dir)
        if gt: return gt
        
    elif type_cmd == CREATEFILE:
        crf = createfile_cm(value_cmd)
        if crf: return crf
        
    elif type_cmd == CREATEFOLDER:
        crfl = createfolder_cm(value_cmd)
        if crfl: return crfl
        
    elif type_cmd == DELETEFILE:
        dlf = delfile_cm(value_cmd)
        if dlf: return dlf
        
    elif type_cmd == DELETEFOLDER:
        dlfd = delfolder_cm(value_cmd)
        if dlfd: return dlfd
        
    elif type_cmd == FILESINFOLDER: filfol_cm(current_dir)
        
    elif type_cmd == WRITESCREEN: writescreen_cm(value_cmd)
    
    elif type_cmd == GETSTATSPC: getstatspc_cm()
    
    elif type_cmd == DATETIME: datetime_cm()
    
    elif type_cmd == HELP: help_cm()
    
    elif type_cmd == MOVE:
        pathsfiles = value_cmd.split(" >>> ")
        
        path1, path2 = pathsfiles[0].rstrip(), pathsfiles[1].rstrip()
    
        mpy = move_cm(path1, path2)
        
        if mpy: return mpy
        
    elif type_cmd == OPEN:
        opn = open_file_cm(value_cmd)
        
        if opn: return opn
        
    elif type_cmd == CALC:
        clc = calc_cm()
        
        if clc: return clc
    
    else: return CommandNotYetImplemented(type_cmd).str_return()
        
            
def run(command):
    command_get, _error = get_commands(command).get_command()
    
    if _error: return _error.str_return()
    
    if command_get: return int_cmd(command_get)
    else: pass
        

def main_app_sys():
    equal_sign = "<" + "="*30 + ">"
    print(f"\n\n{equal_sign}\n{SYSTEM_NAME} {SYSTEM_VER}\nMade in {YEAR_MADE} by {AUTHOR}.\n{equal_sign}\n")

    while True:
        global current_dir
        current_dir = str(SYSTEM_DISK_FOLDER + os.getcwd().split(REAL_SYSTEM_DISK_FOLDER)[1])

        user_input = input(current_dir + ">")

        print(run(user_input) if run(user_input) else "")

