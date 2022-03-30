"""
Errors used by the system...
"""
from sysINF.SYS_INF import SYSTEM_NAME

class ErrorInOS:
    def __init__(self, base_error, details):
        self.error = base_error
        self.details = details

    def str_return(self):
        return f"{self.error}: {self.details}"
    
class WarningInOS:
    def __init__(self, warning):
        self.warning = warning
        
    def show_warning(self):
        print(f"[WARNING]: {self.warning}")


class DiskNotFoundInOS(ErrorInOS):
    def __init__(self):
        super().__init__("Disk Not Found Error", "The system disk wasn't found! Aborting boot...")
        
class PCCantRunSys(ErrorInOS):
    def __init__(self):
        super().__init__("PC Can't Run System Error", "Your PC doesn't meet the system requirements to run " + SYSTEM_NAME)

class CommandNotIdentified(ErrorInOS):
    def __init__(self, command):
        super().__init__("Command Not Indentified Error", f"The command \"{command}\" doesn't exist. Type \"help\" to get all available commands.")

class FileNotDefined(ErrorInOS):
    def __init__(self):
        super().__init__("File Not Defined Error", "Please specify a file.")

class FolderNotDefined(ErrorInOS):
    def __init__(self):
        super().__init__("Folder Not Defined Error", "Please specify a folder.")

class InvalidFileName(ErrorInOS):
    def __init__(self, filename):
        super().__init__("Invalid File Name Error", f"The filename \"{filename}\" is invalid")

class InvalidFolderName(ErrorInOS):
    def __init__(self, foldername):
        super().__init__("Invalid Folder Name Error", f"The foldername \"{foldername}\" is invalid")

class FileWasNotFound(ErrorInOS):
    def __init__(self, filename):
        super().__init__("File Was Not Found Error", f"The file \"{filename}\" doesn't exist.")
        
class FolderWasNotFound(ErrorInOS):
    def __init__(self, foldername):
        super().__init__("Folder Was Not Found Error", f"The folder \"{foldername}\" doesn't exist.")
        
class FileAlreadyExists(ErrorInOS):
    def __init__(self, filename):
        super().__init__("File Already Exists Error", f"The file \"{filename}\" already exists.")
        
class FolderAlreadyExists(ErrorInOS):
    def __init__(self, foldername):
        super().__init__("Folder Already Exists Error", f"The folder \"{foldername}\" already exists.")
        
class CommandNotYetImplemented(ErrorInOS):
    def __init__(self, command_name):
        super().__init__("Command Not Yet Implemented Error", f"The command \"{command_name}\" exists but has not been implemented yet.")
        
class UnknownError(ErrorInOS):
    def __init__(self, error_mes):
        super().__init__("Unknown Error", error_mes)

class IsFolderError(ErrorInOS):
    def __init__(self, foldername):
        super().__init__("Is Folder Error", f"\"{foldername}\" is a folder.")
        
class IsFileError(ErrorInOS):
    def __init__(self, filename):
        super().__init__("Is File Error", f"\"{filename}\" is a file.")
        
class FolderFileNotFoundMove(ErrorInOS):
    def __init__(self):
        super().__init__("Folder or File Not Found Error", "Please specify a File or Folder to move.")
        
class FolderFileNotFoundToMove(ErrorInOS):
    def __init__(self):
        super().__init__("Folder or File Not Found To Move Error", "Please specify a File or Folder to move to.")
        
class FolderFileNotFound(ErrorInOS):
    def __init__(self, folfil):
        super().__init__("Folder or File Not Found Error", f"The File/Folder \"{folfil}\" doesn't exist.")
        
class MoveToFile(ErrorInOS):
    def __init__(self):
        super().__init__("Move To File Error", "You can only move to directories.")
        
class FileExtensionNotFound(ErrorInOS):
    def __init__(self):
        super().__init__("File Extension Not Found Error", "File extension not found, cannot open file.")

#class FileExtensionNotIdentified(ErrorInOS):
#    def __init__(self, ext):
#        super().__init__("File Extension Not Identified Error", f"File extension \"{ext}\" not identified, cannot open file.\n(Do a Pull Request if file extension is needed)")

class ArgvNotIdentified(WarningInOS):
    def __init__(self, argv):
        super().__init__(f"The argument \"{argv}\" doesn't exist. Reading file...")
        
class ArgvNotFound(WarningInOS):
    def __init__(self):
        super().__init__("Argument not specified. Reading file...")
        
class InvalidCharacters(WarningInOS):
    def __init__(self, normalized):
        super().__init__(f"Detected non-ascii characters, normalizing string to \"{normalized}\".")
        
class FileTooLarge(ErrorInOS):
    def __init__(self):
        super().__init__("File Too Large Error", "File too large to be opened, can only open files with 64 KB or less.")