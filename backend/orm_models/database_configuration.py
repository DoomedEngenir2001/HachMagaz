class DatabaseConfiguration():
    USER         = "root"
    PASSWORD     = "918808722"
    HOST         = "127.0.0.1"
    PORT         = 3306  
    DB_NAME      = "foodshop"
    DATABASE_URL = f"mysql+aiomysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"