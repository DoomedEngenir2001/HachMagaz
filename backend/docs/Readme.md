# Это шпаргалка для Backend

Активация вертуального окружения:

```
.venv\Scripts\activate
```

Запуск сервера в режиме реального времени:

```
uvicorn fast_main:app --reload
```

## Как это запустить :

1. Установить **MySQL Workbench**
2. Запустить **MySQL Workbench**
3. Создать **connection** со следующими параметрами:

```
USER         = "root"
PASSWORD     = "918808722"
HOST         = "127.0.0.1"
PORT         = 3306
DB_NAME      = "foodshop"
```

4. Проверить их соответствие в файле **database_configuration.py**
5. Создать новый терминал
6. Перейти в каталог **backend**
7. Выполнить команду
   ```
   uvicorn fast_main:app --reload
   ```

Зависимости:

* Фрэймворк FastAPI

  ```
  pip install fastapi
  ```
* Uvicorn:

  ```
  pip install uvicorn
  ```
* ORM SQLAlchemy

  ```
  pip install SQLAlchemy
  ```
* Ассинхронный драйвер MySQL aiomysql:

  ```
  pip install aiomysql
  ```
* Библиотека обработки JWT

```
pip install PyJWT
```

* Открытие Swagger:

```
 http://127.0.0.1:8000/docs
```

* Открытие ReDoc:

```
 http://127.0.0.1:8000/redoc
```
