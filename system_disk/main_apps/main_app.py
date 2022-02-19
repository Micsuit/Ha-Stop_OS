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
                            self.command_list.append(command("CREATEFILE", value))
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
                        self.command_list.append(command("CREATEFOLDER", value))
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
                        self.command_list.append(command("DELETEFILE", value))
                        if len(self.command_list) == 1:
                            break
                elif self.word == DELETEFOLDER:
                    if self.blank_file(): error = FolderNotDefined()
                    else:
                        while self.current_char in " \t" and self.pos < len(self.text):
                            self.advance()
                        value = self.make_word()
                        self.command_list.append(command("DELETEFOLDER", value))
                        if len(self.command_list) == 1:
                            break
                elif self.word == FILESINFOLDER:
                    self.command_list.append(command("FILESINFOLDER"))
                    if len(self.command_list) == 1:
                        break
                elif self.word == WRITESCREEN:
                    self.advance()
                    value = self.make_word()
                    self.command_list.append(command("WRITESCREEN", value))
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
                    self.command_list.append(command("GETSTATSPC"))
                    if len(self.command_list) == 1:
                        break
                else:
                    error = CommandNotIdentified(self.word)
                    break

            self.advance()

        return self.command_list, error
                

    def make_word(self):
        word_text = ""
        if self.word == GOTO or self.word == WRITESCREEN:
            while not self.current_char in "\t" and self.pos <= len(self.text):
                word_text += self.current_char
                self.advance()
                if self.current_char == None:
                    break
        else:
            while not self.current_char in " \t" and self.pos <= len(self.text):
                word_text += self.current_char
                self.advance()
                if self.current_char == None:
                    break
        
        return word_text

def run(command):
    commands_list = get_commands(command).make_list_commands()
    return commands_list

def main_app_sys():
    equal_sign = "<" + "="*30 + ">"
    print(f"\n\n{equal_sign}\n{SYSTEM_NAME} {SYSTEM_VER}\nMade in {YEAR_MADE} by {AUTHOR}.\n{equal_sign}\n")

    while True:
        current_dir = str(os.getcwd().split(REAL_SYSTEM_DISK_FOLDER)[1] + SYSTEM_DISK_FOLDER)

        user_input = input(current_dir + ">")

        command_list, error_pro = run(user_input)

        if error_pro:
            print(error_pro.str_return())
        else:
            print(command_list)

