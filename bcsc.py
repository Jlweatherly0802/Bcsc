import subprocess
import os
from pathlib import Path
import sys



def FindCsFiles(dir):
    csFiles = []
    files = os.listdir(dir)
    for file in files:
        path = os.path.join(dir, file)
        if file.endswith(".cs"):
            csFiles.append(path)

        if os.path.isdir(path):
            csFiles.extend(FindCsFiles(path))


    return csFiles



def Main():
    if len(sys.argv) < 3:
        print("""
              argument 1 is name of the outputed exe file
              argument 2 is the directory in witch all your files exist

              ex.
              bcsc MyProgram Path/to/your/project
              """)
        exit()
        
    NAME = str(sys.argv[1])
    MAIN_DIR = str(sys.argv[2])

    CS_FILES = FindCsFiles(MAIN_DIR) # returns a list of cs files

    if not os.path.exists(os.path.join(MAIN_DIR, "build")):
        os.mkdir(os.path.join(MAIN_DIR, "build"))


    cscCommand = ["csc", f"/out:{MAIN_DIR}\\build\\{NAME}.exe"] + CS_FILES

    processResult = subprocess.run(cscCommand, capture_output=True, text=True)
    print(processResult.stdout)
    print(processResult.stderr)


Main()
