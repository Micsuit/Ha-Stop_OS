from boot import *
from SYS_INF import *
import sys
from main_app import *

def main():
    print("Starting " + SYSTEM_NAME + "...")
    boot_values, error = boot_sys()
    if error:
        print(boot_values + "\nReason: " + str(error))
        sys.exit()
    else:
        print(boot_values)

    main_app_sys()

if __name__ == "__main__":
    main()
