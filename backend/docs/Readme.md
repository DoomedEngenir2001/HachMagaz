# Это шпаргалка для Backend

Активация вертуального окружения:

```
.venv\Scripts\activate
```

Запуск сервера в режиме реального времени:

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
* Открытие Swagger:

```
 http://127.0.0.1:8000/docs
```

* Открытие ReDoc:

```
 http://127.0.0.1:8000/redoc
```
