import os, sys

def add_folderToSysPath(folder: str):
    absolute_path = os.path.abspath(folder)
    if absolute_path not in sys.path:
        sys.path.insert(0, absolute_path)
        print(f"Папка {absolute_path} добавлена в sys.path")
    else:
        print(f"Папка {absolute_path} уже присутствует в sys.path")

def create_folderIfNotExists(folder_path: str):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Папка '{folder_path}' создана.")
    else:
        print(f"Папка '{folder_path}' уже существует.")