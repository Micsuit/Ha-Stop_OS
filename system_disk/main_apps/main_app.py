from sysINF.SYS_INF import *
from errors.system_error import *
import os
from main_apps.command_list import *
import pathvalidate

class command:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        if self.value: return f"{self.type}: {self.value}"
        else: return f"{self.type}"

class get_commands:
    def __init__(self, text):
        self.text = text
        self.pos = 1
        self.command_list = []
        if self.text:
            self.current_char = self.text[self.pos - 1]
        else:
            self.text = "  "
            self.current_char = self.text[self.pos - 1]
        self.word = ""

    def only_dots(self, filename) -> bool:
        no_dots = ""

        for letter in filename:
            if letter != ".":
                no_dots += letter
        
        if no_dots: return False
        else: return True

    def blank_file(self):
        return self.current_char == None or self.text[self.pos:len(self.text)].isspace() or self.text[self.pos:len(self.text)] == ""

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos - 1] if self.pos <= len(self.text) else None

    def make_list_commands(self):
        error = None
        while self.current_char != None:
            if not self.current_char in " \t":
                self.word = self.make_word().lower()
                if self.word == SHUTDOWN:
                    self.command_list.append(command("SHUTDOWN"))
                    if len(self.command_list) == 1:
                        break
                elif self.word == GOTO:
                    if self.blank_file():
                        error = FolderNotDefined()
                    else:
                        while self.current_char in " \t" and self.pos < len(self.text):
                            self.advance()
                        value = self.make_word()
                        self.command_list.append(command("GOTO", value))
                        if len(self.command_list) == 1:
                            break
                elif self.word == CREATEFILE:
                    if self.blank_file(): error = FileNotDefined()
                    else:
                        while self.current_char in " \t" and self.pos < len(self.text):
                            self.advance()
                        value = self.make_word()
                        if pathvalidate.is_valid_filename(value) and not self.only_dots(value):
                            self.command_list.append(command("CREATEFIL", value))
                            if len(self.command_list) == 1:
                                break
                        else:
                            error = InvalidFileName(value)
                elif self.word == CREATEFOLDER:
                    if self.blank_file(): error = FolderNotDefined()
                    else:
                        while self.current_char in " \t" and self.pos < len(self.text):
                            self.advance()
                        value = self.make_word()
                        if pathvalidate.is_valid_filepath(value) and not self.only_dots(value):
                            self.command_list.append(command("CREATEFOL", value))
                            if len(self.command_list) == 1:
                                break
                        else:
                            error = InvalidFolderName(value)
                elif self.word == DELETEFILE:
                    if self.blank_file(): error = FileNotDefined()
                    else:
                        while self.current_char in " \t" and self.pos < len(self.text):
                            self.advance()
                        value = self.make_word()
                        self.command_list.append(command("DELETEFIL", value))
                        if len(self.command_list) == 1:
                            break
                elif self.word == DELETEFOLDER:
                    if self.blank_file(): error = FolderNotDefined()
                    else:
                        while self.current_char in " \t" and self.pos < len(self.text):
                            self.advance()
                        value = self.make_word()
                        self.command_list.append(command("DELETEFOL", value))
                        if len(self.command_list) == 1:
                            break
                elif self.word == FILESINFOLDER:
                    self.command_list.append(command("FILFOL"))
                    if len(self.command_list) == 1:
                        break
                elif self.word == WRITESCREEN:
                    self.advance()
                    value = self.make_word()
                    if value.isspace() or value == "": value = "*Nothing*"
                    self.command_list.append(command("WRITESCRN", value))
                    if len(self.command_list) == 1:
                        break
                elif self.word == OPEN:
                    if self.blank_file(): error = FileNotDefined()
                    else:
                        while self.current_char in " \t" and self.pos < len(self.text):
                            self.advance()
                        value = self.make_word()
                        self.command_list.append(command("OPEN", value))
                        if len(self.command_list) == 1:
                            break
                elif self.word == GETSTATSPC:
                    self.command_list.append(command("STATSPC"))
                    if len(self.command_list) == 1:
                        break
                elif self.word == DATETIME:
                    self.command_list.append(command("DATIME"))
                    if len(self.command_list) == 1:
                        break
                elif self.word == HELP:
                    self.command_list.append(command("HELP"))
                    if len(self.command_list) == 1:
                        break

                else:
                    error = CommandNotIdentified(self.word)
                    break

            self.advance()

        return self.command_list, error
                

    def make_word(self):
        not_in = ""
        word_text = ""
        if self.word in [GOTO, WRITESCREEN, CREATEFOLDER, CREATEFILE, DELETEFILE, DELETEFOLDER, OPEN]: not_in = "\t"
        else: not_in = " \t"
        len_text = len(self.text)
        
        while self.pos <= len(self.text) and not self.current_char in not_in:
            word_text += self.current_char
            self.advance()
            if self.current_char == None:
                break
        
        return word_text

def int_cmd(cmds_list):
    global current_dir
    if cmds_list:
        _cmd = cmds_list[0]
        type_cmd = _cmd.type.lower()
        #print(type_cmd)
        if _cmd.value:
            value_cmd = _cmd.value
        if type_cmd == SHUTDOWN:
            shutdown_cm()
        elif type_cmd == GOTO:
            #print("Current Directory:", current_dir, "\nValue_cmd:", value_cmd)
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
        elif type_cmd == FILESINFOLDER:
            filfol_cm(current_dir)
        elif type_cmd == WRITESCREEN:
            writescreen_cm(value_cmd)
        elif type_cmd == GETSTATSPC:
            getstatspc_cm()
        elif type_cmd == DATETIME:
            datetime_cm()
        elif type_cmd == HELP:
            help_cm()
        else:
            return CommandNotYetImplemented(type_cmd).str_return()
    else:
        pass
        
            
def run(command):
    commands_list, _error = get_commands(command).make_list_commands()
    
    if _error:
        return _error.str_return()
    
    else:
        return int_cmd(commands_list)
        

def main_app_sys():
    equal_sign = "<" + "="*30 + ">"
    print(f"\n\n{equal_sign}\n{SYSTEM_NAME} {SYSTEM_VER}\nMade in {YEAR_MADE} by {AUTHOR}.\n{equal_sign}\n")

    while True:
        global current_dir
        current_dir = str(SYSTEM_DISK_FOLDER + os.getcwd().split(REAL_SYSTEM_DISK_FOLDER)[1])

        user_input = input(current_dir + ">")

        
        print(run(user_input) if run(user_input) else "")

