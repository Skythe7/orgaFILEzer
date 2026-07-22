from pathlib import Path
import shutil
import datetime
import zipfile
import argparse
import sys


parser = argparse.ArgumentParser(description="Organize, inspect, and analyze your filesystem!")

parser.add_argument("path")
parser.add_argument("options", choices=["organize", "inspect", "analyze"])

args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        menu()
    else:
        path = convert_to_path(args.path)

        match args.options:
            case "organize":
                folder_download_organizer(path)
            case "inspect":
                archive_inspector(path)
            case "analyze":
                project_analyzer(path)


def menu():
    try:
        print("1. Folder Download Organizer")
        print("2. Project Analyzer")
        print("3. Archive Inspector")
        user_choice = int(input("Options (1-3): "))

        path = convert_to_path(input("Folder/file path: "))
        
        match user_choice:
            case 1:
                folder_download_organizer(path)
            case 2:
                project_analyzer(path)
            case 3:
                archive_inspector(path)
            case _:
                sys.exit("Invalid options!")
        
    except ValueError:
        sys.exit("Please insert a number!")
  

def folder_download_organizer(path):
    ...


def project_analyzer(path):
    ...


def archive_inspector(path):
    ...


def convert_to_path(path_string):
    path = Path(path_string).expanduser()
    if not path.is_absolute():
        path = Path.home() / path
    
    return path


if __name__ == "__main__":
    main()