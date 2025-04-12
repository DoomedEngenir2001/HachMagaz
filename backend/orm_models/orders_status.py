class Order_status:
    STATUS_CREATED             = "created"             # Корзина создана, но пуста  
    STATUS_ITEMS_ADDED         = "items_added"         # В корзину добавлены товары  
    STATUS_AWAITING_CHECKOUT   = "awaiting_checkout"   # Пользователь начал оформление заказа  
    STATUS_ORDERED             = "ordered"             # Заказ оформлен, но не оплачен  
    STATUS_AWAITING_PAYMENT    = "awaiting_payment"    # Ожидание оплаты  
    STATUS_PAID                = "paid"                # Оплата получена  
    STATUS_PROCESSING          = "processing"          # Заказ собирается  
    STATUS_SHIPPED             = "shipped"             # Заказ передан в доставку  
    STATUS_IN_TRANSIT          = "in_transit"          # Заказ в пути  
    STATUS_READY_FOR_PICKUP    = "ready_for_pickup"    # Доступен в пункте выдачи  
    STATUS_DELIVERED           = "delivered"           # Доставлен клиенту  
    STATUS_COMPLETED           = "completed"           # Заказ завершён  
    STATUS_CANCELED            = "canceled"            # Заказ отменён  
    STATUS_RETURN_REQUESTED    = "return_requested"    # Клиент запросил возврат  
    STATUS_RETURNED            = "returned"            # Возврат завершён, деньги возвращены  

    @staticmethod
    def get_all_statuses() -> list[str]:
        """
        Возвращает все статусы заказа.
        """
        return [
            Order_status.STATUS_CREATED,
            Order_status.STATUS_ITEMS_ADDED,
            Order_status.STATUS_AWAITING_CHECKOUT,
            Order_status.STATUS_ORDERED,
            Order_status.STATUS_AWAITING_PAYMENT,
            Order_status.STATUS_PAID,
            Order_status.STATUS_PROCESSING,
            Order_status.STATUS_SHIPPED,
            Order_status.STATUS_IN_TRANSIT,
            Order_status.STATUS_READY_FOR_PICKUP,
            Order_status.STATUS_DELIVERED,
            Order_status.STATUS_COMPLETED,
            Order_status.STATUS_CANCELED,
            Order_status.STATUS_RETURN_REQUESTED,
            Order_status.STATUS_RETURNED
        ]