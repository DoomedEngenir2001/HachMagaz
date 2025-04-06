import os, sys
import random, string
from datetime import datetime

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

def generate_random_UID(length: int = 4):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def add_parent_folder_to_sys_path():
    """
    Добавляет родительскую папку текущего файла в sys.path.
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))  # Текущая директория файла
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))  # Родительская директория
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
        print(f"Родительская папка {parent_dir} добавлена в sys.path")
    else:
        print(f"Родительская папка {parent_dir} уже присутствует в sys.path")

def get_current_datetime(pattern: str = "%Y-%m-%d %H:%M:%S") -> str:
    """
    Возвращает текущую дату и время в строковом формате по заданному паттерну.

    :param pattern: Паттерн для форматирования даты и времени (по умолчанию "%Y-%m-%d %H:%M:%S").
    :return: Строка с текущей датой и временем.
    """
    return datetime.now().strftime(pattern)

def check_file_exists(file_path: str) -> bool:
    """
    Проверяет, существует ли файл по указанному пути.
    :param file_path: Путь к файлу.
    :return: True, если файл существует, иначе False.
    """
    return os.path.isfile(file_path)
