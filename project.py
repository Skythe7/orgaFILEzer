from pathlib import Path
import shutil
import datetime
import zipfile
import argparse
import sys


parser = argparse.ArgumentParser(description="Organize, inspect, and analyze your filesystem!")

parser.add_argument("options", choices=["organize", "inspect", "analyze"], nargs='?')
parser.add_argument("path", nargs='?')

args = parser.parse_args()


def main():
    if len(sys.argv) == 1:
        menu()
    else:
        try:
            path = convert_to_path(args.path)

            match args.options:
                case "organize":
                    folder_organizer(path)
                case "inspect":
                    archive_inspector(path)
                case "analyze":
                    project_analyzer(path)
        except FileNotFoundError:
            sys.exit("File or folder does not exist!")


def menu():
    try:
        print("1. Folder Organizer")
        print("2. Project Analyzer")
        print("3. Archive Inspector")
        user_choice = int(input("Options (1-3): "))

        path = convert_to_path(input("Folder/file path: "))
        
        match user_choice:
            case 1:
                folder_organizer(path)
            case 2:
                project_analyzer(path)
            case 3:
                archive_inspector(path)
            case _:
                sys.exit("Invalid options!")
        
    except ValueError:
        sys.exit("Please insert a number!")
    except FileNotFoundError:
        sys.exit("File or folder does not exist!")
  

def folder_organizer(path: Path):
    for file in path.iterdir():
        if file.is_file():
            target_dir = path / f"{file.suffix.removeprefix(".")} files"
            print(target_dir)
            target_dir.mkdir(exist_ok=True)
            shutil.move(file, target_dir)

def project_analyzer(path: Path):
    ...


def archive_inspector(path: Path):
    ...


def convert_to_path(path_string):
    try:
        path = Path(path_string).expanduser()
        if not path.is_absolute():
            path = Path.home() / path
        
        return path
    except TypeError:
        sys.exit("Please enter path!")



if __name__ == "__main__":
    main()