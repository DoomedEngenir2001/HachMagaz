import os

def check_file_exists(file_path: str) -> bool:
    """
    Проверяет, существует ли файл по указанному пути.
    :param file_path: Путь к файлу.
    :return: True, если файл существует, иначе False.
    """
    return os.path.isfile(file_path)

print( check_file_exists("backend/images/Пиццуля.PNG") )