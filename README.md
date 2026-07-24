# orgaFILEzer
#### Video demo: TODO
## What is orgaFILEzer?
OrgaFILEzer is simply a CLI program that can be used to analyze, or even organize your file system!
## Why would I need this?
Some people may have a problem where their file system is AWFULLY disorganized (which includes me too).

That's why I created this program to know better about your file system. This program will helps you discover what might be a problem related to big heavy files, or simple just organize your folders and files better.
## How do I use this?
It's very simple, there's two modes in this program:
1. With menu
2. Non menu (use arguments)

### With menu
```
python project.py
```
It should output a table of menu:
```
┏━━━━━━━━━━━━━━━━━━━━━━┓
┃ Options              ┃
┡━━━━━━━━━━━━━━━━━━━━━━┩
│ 1. Folder Organizer  │
│ 2. Folder Analyzer   │
│ 3. Archive Inspector │
└──────────────────────┘
```
Choose an option with their corresponding number. And input your file/folder path
### With arguments
```
python project.py -h
```
It should output following arguments:
```
usage: project.py [-h] [{organize,inspect,analyze}] [path]

Organize, inspect, and analyze your filesystem!

positional arguments:
  {organize,inspect,analyze}
  path

options:
  -h, --help            show this help message and exit
```
## Features
### Folder Organizer
- Scans the whole folder
- Collect the file extensions.
- Make a folder and move the files into designated folders according to their own file extensions.
### Folder Analyzer
- Ask users where their folder is (or if have arguments)
- Scans the folders
- Find information about all the files in that folder
- Output all the reports
### Archive Inspector
- Get into the archive file.
- Output the informations (folders, files, etc)