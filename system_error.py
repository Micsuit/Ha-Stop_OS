from SYS_INF import SYSTEM_NAME


class ErrorInOS:
    def __init__(self, base_error, details):
        self.error = base_error
        self.details = details

    def str_return(self):
        return self.error + ": " + self.details


class DiskNotFoundInOS(ErrorInOS):
    def __init__(self):
        super().__init__("Disk Not Found Error", "The system disk wasn't found! Aborting boot...")
        
class PCCantRunSys(ErrorInOS):
    def __init__(self):
        super().__init__("PC Can't Run System Error", "Your PC doesn't meet the system requirements to run " + SYSTEM_NAME)

class CommandNotIdentified(ErrorInOS):
    def __init__(self, command):
        super().__init__("Command Not Indentified Error", f"The command \"{command}\" doesn't exist.")

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