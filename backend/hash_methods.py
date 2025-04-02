#-------------------------------------------------------------#
import hashlib
import os
#-------------------------------------------------------------#

def hash_password(password: str, salt_length: int = 16) -> (str, str):
    """
    Генерирует хэш пароля с использованием SHA-256 и соли.
    :param password: Пароль, который нужно захэшировать.
    :param salt_length: Длина соли (по умолчанию 16 символов).
    :return: Хэшированный пароль в формате "salt:hash".
    """
    # Генерируем случайную соль
    salt = os.urandom(salt_length).hex()
    # Вычисляем хэш пароля с солью
    hash_object = hashlib.sha256((salt + password).encode())
    password_hash = hash_object.hexdigest()
    # Возвращаем соль и хэш в формате "salt:hash"
    return (password_hash, salt)

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Проверяет, соответствует ли введённый пароль хэшу.
    :param password: Введённый пароль.
    :param hashed_password: Хэшированный пароль в формате "salt:hash".
    :return: True, если пароль верный, иначе False.
    """
    try:
        # Разделяем соль и хэш
        salt, stored_hash = hashed_password.split(":")
        # Вычисляем хэш введённого пароля с той же солью
        hash_object = hashlib.sha256((salt + password).encode())
        password_hash = hash_object.hexdigest()
        # Сравниваем хэши
        return password_hash == stored_hash
    except ValueError:
        print("Неверный формат хэша.")
        return False
    
def get_fileHash(file_path : str) -> str:
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as file:
            # Читаем файл блоками для обработки больших файлов
            for chunk in iter(lambda: file.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
    except Exception as e:
        print(f"Ошибка при вычислении хэша: {e}")