import argparse
from pathlib import Path
import subprocess

def createArchive(directory):
    print(directory)
    print(type(directory))
    print("function to create an archive")

def moveArchive():
    print("function to move the archive")

def checkIfIsADirectory(path):
    print("function to check if the argument is a directory")
    
    if isinstance(path, Path) and path.is_dir():
        print("It's a directory")
        # createArchive(path)
        is_empty(path)
        if is_empty(path) == True:
            print("Directory is empty, provide a directory with some folders or files.")
        else:
            createArchive(path)
    else:
        print("It's not a directory. Provide a directory to use the CLI tool.")

def is_empty(path):        
    # result = subprocess.run(["ls", "-l", path], capture_output=True, text=True)
        
    # if result.returncode == 0:
    #     print(result.stdout)
    #     print("result =", result)
    #     print("len(result.stdout) =", len(result.stdout) )
    #     print("type(result.stdout)", type(result.stdout))
    #     if result.stdout == "total 0\n":
    #         print("empty directory")
    #     else:
    #         print("not empty")
    # else:
    #     print(f"Error when using the command : {result.stderr}")
    if not any(path.iterdir()):
        return True
    else:
        return False

def main():
    parser = argparse.ArgumentParser(
        description="CLI Tool for log archiving."
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to the directory to use with the CLI tool."
    )

    args = parser.parse_args()

    directory_path = Path(args.path)

    print('=========================')
    print(f"Provided path: {directory_path}")

    checkIfIsADirectory(directory_path)

if __name__ == "__main__":
    main()
