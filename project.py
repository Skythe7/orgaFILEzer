from pathlib import Path
import shutil
import datetime
from zipfile import ZipFile
import argparse
import sys
import humanize
import rich


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
                    folder_analyzer(path)
                
        except FileNotFoundError:
            sys.exit("File or folder does not exist!")


def menu():
    try:
        print("1. Folder Organizer")
        print("2. Folder Analyzer")
        print("3. Archive Inspector")
        user_choice = int(input("Options (1-3): "))

        path = convert_to_path(input("Folder/file path: "))
        
        match user_choice:
            case 1:
                folder_organizer(path)
            case 2:
                folder_analyzer(path)
            case 3:
                archive_inspector(path)
            case _:
                sys.exit("Invalid options!")
        
    except ValueError:
        sys.exit("Please insert a type according to the prompt!")
    except FileNotFoundError:
        sys.exit("File or folder does not exist!")
  

def folder_organizer(path: Path):
    for file in path.iterdir():
        if file.is_file():
            target_dir = path / f"{file.suffix.upper().removeprefix(".")} files"
            print(target_dir)
            target_dir.mkdir(exist_ok=True)
            shutil.move(file, target_dir)


def folder_analyzer(path: Path):
    statistic = {
        "total_files": 0,
        "total_folders": 0,
        "oldest_file": "",
        "newest_file": "",
        "total_size": 0,
        "largest_file": "",
        "smallest_file": ""
    }
    file_time = {}
    file_size = {}

    for file in path.rglob("*"):
        if file.is_file():
            statistic["total_files"] += 1
            statistic["total_size"] += file.stat().st_size
            file_time[file.relative_to(path)] = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            file_size[file.relative_to(path)] = file.stat().st_size
    
    for folder in path.rglob("*"):
        if folder.is_dir():
            statistic["total_folders"] += 1

    statistic["oldest_file"] = min(file_time, key=file_time.get)
    statistic["newest_file"] = max(file_time, key=file_time.get)
    statistic["largest_file"] = max(file_size, key=file_time.get)
    statistic["smallest_file"] = min(file_size, key=file_time.get)

    print()
    print("=======================================================================")
    print(f"Total files: {humanize.intcomma(statistic["total_files"])}")
    print(f"Total folders: {humanize.intcomma(statistic["total_folders"])}")
    print(f"Oldest file: {statistic["oldest_file"]}")
    print(f"Newest file: {statistic["newest_file"]}")
    print(f"Total size: {humanize.naturalsize(statistic["total_size"])}")
    print(f"Largest file: {statistic["largest_file"]}")
    print(f"Smallest file: {statistic["smallest_file"]}")
    print("=======================================================================")


def archive_inspector(path: Path):
    try:
        with ZipFile(path) as file:
            print()
            print("==================================")
            print(f"Name: {file.filename}")
            print(f"File in archive:")
            for f in file.infolist():
                print(f"{f.filename}: {humanize.naturalsize(f.file_size)}")
            print("==================================")

    except IsADirectoryError:
        sys.exit("Please enter zip file")


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