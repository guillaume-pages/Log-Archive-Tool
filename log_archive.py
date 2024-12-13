import argparse
import datetime
from pathlib import Path
import subprocess
import shutil

def createArchive(directory):
    x = datetime.datetime.now()
    date = x.strftime("%Y") + x.strftime("%m") + x.strftime("%d") + "_" + x.strftime("%H") + x.strftime("%M") + x.strftime("%S")
    archiveName = "logs_archive_" + date

    compressed_file = shutil.make_archive(
        base_name=archiveName,
        format='gztar',
        root_dir=directory
    )

def moveArchive():
    print("function to move the archive")

def checkIfIsADirectory(path):
    if isinstance(path, Path) and path.is_dir():
        is_empty(path)
        if is_empty(path) == True:
            print("Directory is empty, provide a directory with some folders or files.")
        else:
            createArchive(path)
    else:
        print("It's not a directory. Provide a directory to use the CLI tool.")

def is_empty(path):        
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

    checkIfIsADirectory(directory_path)

if __name__ == "__main__":
    main()
