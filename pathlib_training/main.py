from pathlib import Path
import sys
import datetime


def main():
    try:
        print("WHY R U HERE- Oh u want to inspect ur dirty filesystem?")
        print("1. Folder summary")
        print("2. Total Files")
        print("3. Largest Files")
        print("4. Extensions Counts")
        print("5. Newest File")
        print("6. Oldest File")

        option = int(input("Option (Input number plssss): "))

        user_input = input("Folder: ").strip()
        path = Path(user_input).expanduser()
        if not path.is_absolute():
            path = Path.home() / path
        
        check_path_exist(path)

        print("======================================================================================")
        match option:
            case 1:
                print("*breath* AAAAAAA-")
                for folder in folder_summary(path):
                    print(folder)

            case 2:
                print(f"Ew ur file(s) stinks, there are like {total_files(path)} of them")

            case 3:
                print(f"Oh gosh, cuz wth is this file contains: {largest_files(path)}")

            case 4:
                extensions = extensions_counts(path)

                print("Here's ur stupid file extensions count")
                for key, value in extensions.items():
                    print(f"{key}: {value} file(s)")

            case 5:
                print(f"Yo, my xbox 360 is older than this: {newest_files(path)}")

            case 6:
                print(f"Nah, bro is unc: {oldest_files(path)}")

            case _:
                sys.exit("WHAT THE HELLLLL IS THIS NUMBER GRRRRRRR, USE 1-6 DUMMY")
            
        print("======================================================================================")

    except ValueError:
        sys.exit("r u an idiot? I SAID INPUT A NUMBER GRRRR")
    except FileNotFoundError:
        sys.exit("Im crine, this path does not exist lil bro")


def check_path_exist(p):
    if not p.exists():
        raise FileNotFoundError


def folder_summary(p):
    for directory in p.iterdir():
        if directory.is_dir():
            yield directory


def total_files(p):
    file_count = 0

    for file in p.rglob("*"):
        if file.is_file():
            file_count += 1
    
    return file_count


def largest_files(p):
    file_size = {}

    for file in p.rglob("*"):
        if file.is_file():
            file_size[file.resolve()] = file.stat().st_size
    
    return max(file_size, key=file_size.get)


def extensions_counts(p):
    extensions = {}

    for file in p.rglob("*"):
        if file.is_file():
            if file.suffix in extensions.keys():
                extensions[file.suffix] += 1
            else:
                extensions[file.suffix] = 1
    
    return extensions


def newest_files(p):
    file_time = {}

    for file in p.rglob("*"):
        if file.is_file():
            file_time[file.resolve()] = datetime.datetime.fromtimestamp(file.stat().st_mtime)
    
    return max(file_time, key=file_time.get)


def oldest_files(p):
    file_time = {}

    for file in p.rglob("*"):
        if file.is_file():
            file_time[file.resolve()] = datetime.datetime.fromtimestamp(file.stat().st_mtime)
    
    return min(file_time, key=file_time.get)


if __name__ == "__main__":
    main()