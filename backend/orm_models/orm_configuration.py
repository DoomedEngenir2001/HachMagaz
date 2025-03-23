class ORM_Configuration:
    t_products      : str = 'products'
    t_productsCards : str = 'productsCards'
    t_images        : str = 'images'
    t_users         : str = 'users'
    t_orders        : str = 'orders'
    t_detailes      : str = 'detailes'
    t_basket        : str = 'basket'


    c_Products     : str = "Products"
    c_ProductCards : str = "ProductCards"
    c_Images       : str = "Images"
    rel_product_to_productsCards  : str = 'product'
    rel_productsCards_to_product  : str = 'productCards'
    rel_image_to_productsCard     : str = 'image'
    rel_productsCard_to_image     : str = 'productCards'
    

    str_None        : str = 'None'
    str_Error       : str = 'Error'
    int_None        : int = -200
    int_Error       : int = -404

