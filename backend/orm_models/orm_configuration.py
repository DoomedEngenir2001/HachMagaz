class ORM_Configuration:
    # Таблицы ORM
    t_products      : str = 'products'
    t_productsCards : str = 'productsCards'
    t_images        : str = 'images'
    t_users         : str = 'users'
    t_orders        : str = 'orders'
    t_transactions  : str = 'transactions'

    # Классы ORM
    c_Products     : str = "Products"
    c_ProductCards : str = "ProductCards"
    c_Images       : str = "Images"
    c_Users        : str = "Users"
    c_Orders       : str = "Orders"
    c_Transactions : str = "Transactions"

    # Связи
    # Products <-> ProductCards
    rel_product_to_productsCards  : str = 'product'
    rel_productsCards_to_product  : str = 'productCards'
    # ProductCards <-> Images
    rel_image_to_productsCard     : str = 'image'
    rel_productsCard_to_image     : str = 'productCards'
    # Users <-> Orders
    rel_user_to_orders            : str = 'user'
    rel_orders_to_user            : str = 'orders'
    # Orders <-> Transactions
    rel_orders_to_transactions    : str = 'order'
    rel_transactions_to_orders    : str = 'transactions'
    # ProductCards <-> Transactions
    rel_productsCards_to_transactions : str = 'productCard'
    rel_transactions_to_productsCards : str = 'transactions'
    
    # Константы для ORM
    str_None        : str = 'None'
    str_Error       : str = 'Error'
    int_None        : int = -200
    int_Error       : int = -404

