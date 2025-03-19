class DatabaseConfiguration():
    USER         = "root"
    PASSWORD     = "918808722"
    HOST         = "localhost"
    PORT         = 3306  
    DB_NAME      = "FoodShop"
    DATABASE_URL = f"mysql+aiomysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"