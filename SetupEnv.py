import os
import sys
import pip
import subprocess

from sys import platform

yesList = ["YES", "Y", ""]
noList = ["NO", "N"]
osList = ["LINUX", "LINUX2", "WIN32", "DARWIN"]
pythonBinWin = os.path.join(os.getcwd(), "Python_101\\Scripts\\python")
pythonBinLin = os.path.join(os.getcwd(), "Python_101/bin/python")

def install(package):
    print("Installing {}...".format(package))
    pip.main(["install", package])

def setup_linux():
    print("Beginning install")
    install("virtualenv")
    print("Setting up virtual environment: Python_101")
    subprocess.call(["virtualenv", "Python_101"])
    print("Installing necessary imports in virtual environment")
    subprocess.call([pythonBinLin, "pipInstall.py"])
    print("Switching to new environment")
    os.system('/bin/bash --rcfile setActive.sh')
    print("Environment Setup")
    
def setup_windows():
    install("virtualenv")
    print("Setting up virtual environment: Python_101")
    subprocess.call(["virtualenv", "Python_101"])
    print("Installing necessary imports in virtual environment")
    subprocess.call([pythonBinWin, "pipInstall.py"])
    print("Environment Setup")
    print("To switch to your new environment, please enter the following: '" + str(os.getcwd()) +
          "\\Python_101\\Scripts\\activate")

def setup_osx():
    print("Beginning install")
    install("virtualenv")
    print("Setting up virtual environment: Python_101")
    subprocess.call(["virtualenv", "Python_101"])
    print("Installing necessary imports in virtual environment")
    subprocess.call([pythonBinLin, "pipInstall.py"])
    print("Switching to new environment")
    os.system('/bin/bash --rcfile setActive.sh')
    print("Environment Setup")
    
def setup3():
    version = [sys.version_info.major, sys.version_info.minor, sys.version_info.micro]
    print("Python {}.{}.{} detected".format(*version))
    prompt = True
    while(prompt):
        if platform == "linux" or platform == "linux2":
            answer = input("Linux OS detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_linux()
            elif answer in noList:
                os = input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid input.")
        elif platform == "win32":
            answer = input("Windows OS detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_windows()
            elif answer in noList:
                os = input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid input.")
        elif platform == "darwin":
            answer = input("Mac OSX detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_osx()
            elif answer in noList:
                os = input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid input.")
        else:
            print("This OS is not supported. Exiting script...")

def setup2():
    version = [sys.version_info.major, sys.version_info.minor, sys.version_info.micro]
    print("Python {}.{}.{} detected".format(*version))
    prompt = True
    while (prompt):
        if platform == "linux" or platform == "linux2":
            answer = raw_input("Linux OS detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_linux()
            elif answer in noList:
                os = raw_input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid raw_input.")
        elif platform == "win32":
            answer = raw_input("Windows OS detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_windows()
            elif answer in noList:
                os = raw_input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid raw_input.")
        elif platform == "darwin":
            answer = raw_input("Mac OSX detected. Is this correct? (Y/N) [Default: Y] ")
            answer = answer.upper()
            if answer in yesList:
                prompt = False
                setup_osx()
            elif answer in noList:
                os = raw_input("Please enter your OS - use linux or linux2, win32, or darwin (OSX)")
                os = os.upper()
                if os in osList:
                    if os == "LINUX" or os == "LINUX2":
                        prompt = False
                        setup_linux()
                    if os == "WIN32":
                        prompt = False
                        setup_windows()
                    if os == "DARWIN":
                        prompt = False
                        setup_osx()
                else:
                    print("That is not a valid OS")
            else:
                print("That is not a valid raw_input.")
        else:
            print("This OS is not supported. Exiting script...")

def main():
    version = sys.version_info.major
    if version == 2:
        setup2()
    else:
        setup3()

if __name__ == "__main__":
    main()