"""
Calculator in the Ha-Stop OS System!
"""

from errors.system_error import InvalidCalculation
from applications.calc import version_program
INVALID_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$&',:;<=>?@\\[]^_`\\{|}~"

def is_valid(calc_string):
    for letter in calc_string:
        if letter in INVALID_CHARS:
            return False
        
    return True

def calc_main():
    error = None
    print(f"\n============================ Calculator {version_program.version} ============================\n")
    while True:
        calc_str = input("Calc: ")
        if calc_str.lower().strip() == "quit": break
        if is_valid(calc_str): 
            try:
                print(eval(calc_str))
            except:
                error = InvalidCalculation()
        else: error = InvalidCalculation()
        if error: print(error.str_return()); error = None