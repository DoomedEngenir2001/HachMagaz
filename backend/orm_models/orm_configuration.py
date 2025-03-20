class ORM_Configuration:
    t_products      : str = 'products'
    t_productsCards : str = 'productsCards'
    t_images        : str = 'images'
    t_users         : str = 'users'
    t_orders        : str = 'orders'
    t_detailes      : str = 'detailes'
    t_basket        : str = 'basket'

    rel_products_to_productsCards : str = 'productCards'
    rel_productsCards_to_products : str = 'products'
    rel_images_to_productsCards   : str = 'productCards'
    rel_productsCards_to_images   : str = 'images'
    

    str_None        : str = 'None'
    str_Error       : str = 'Error'
    int_None        : int = -200
    int_Error       : int = -404

