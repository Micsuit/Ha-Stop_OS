class type_stor:
    B = 1
    KB = B * 1024
    MB = KB * 1024
    GB = MB * 1024
    TB = GB * 1024
    
    
    def convert_byte(bytes, tpstor):
        return bytes / tpstor
    
    def convert_show(bytes):
        lev_stor_str = {1: "B", 2: "KB", 3: "MB", 4: "GB", 5: "TB"}
        converted_bytes = bytes
        i = 1
        
        while converted_bytes > 750:
            i += 1
            
            converted_bytes /= 1024
            
        return f"{(round(converted_bytes, 2))} {lev_stor_str[i]}"


class RAM:
    def __init__(self, num, type_storage):
        self.num = num
        self.type_storage = type_storage
        self.size = self.num * self.type_storage

    def __repr__(self):
        return f"{self.num} {self.type_storage}"

class CPU:
    def __init__(self, name, bits, power):
        self.name = name
        self.bits = bits
        self.power = power

    def __repr__(self):
        return [self.name, str(self.bits) + "-BITS", str(self.power) + " POWER"]

class storage:
    def __init__(self, num, type_storage):
        self.num = num
        self.type_storage = type_storage
        self.size = self.num * self.type_storage

    def __repr__(self):
        return f"{self.num} {self.type_storage}"

# [System Param]
SYSTEM_NAME = "Ha-Stop OS"
SYSTEM_VER = 1.0
YEAR_MADE = 2022
AUTHOR = "Daniel Munteanu"
REAL_SYSTEM_DISK_FOLDER = "system_disk"
SYSTEM_DISK_FOLDER = "H:"

# [Configs]


# [Computer Components]
PC_RAM = RAM(48, type_stor.MB)
PC_CPU = CPU("default CPU", 16, 5)
SYS_STORAGE = storage(512, type_stor.MB)


# [Min Requirements]
MIN_RAM = RAM(16, type_stor.MB)
MIN_CPU = CPU("default CPU", 16, 2)
MIN_SYS_STORAGE = storage(128, type_stor.MB)
