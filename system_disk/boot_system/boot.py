import os
from errors.system_error import *
from sysINF.SYS_INF import *

def test_ram():
   return PC_RAM.size >= MIN_RAM.size

def test_cpu():
    test_all = [PC_CPU.name == MIN_CPU.name, 
                PC_CPU.bits >= MIN_CPU.bits,
                PC_CPU.power >= MIN_CPU.power]

from errors.system_error import *
from sysINF.SYS_INF import *

def test_ram():
   return PC_RAM.size >= MIN_RAM.size

def test_cpu():
    test_all = [PC_CPU.name == MIN_CPU.name, 
                PC_CPU.bits >= MIN_CPU.bits,
                PC_CPU.power >= MIN_CPU.power]

    return all(test_all)

def test_storage():
    return SYS_STORAGE.size >= MIN_SYS_STORAGE.size
    

def test_comp():
    return all([test_ram(), test_cpu(), test_storage()])

def boot_sys():
    error = None

    print("Testing Components...")
    test_comp_boot = test_comp()
    if test_comp_boot: print("Test Sucessful")
    else:
        error = PCCantRunSys()
        print("Test Failed")
        return "Boot Failed", error.details

    return "Boot Sucessful", error

    
