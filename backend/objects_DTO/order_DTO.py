from orm_models.orm_orders import Orders

class Order_DTO:
    def __init__(self, orders:Orders):
        self.id = orders.id
        self.createTime = orders.createTime
        self.address = orders.address   