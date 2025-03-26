from orm_models.orm_productCards import ProductCards
from orm_models.orm_images import Images

class ProductCard_DTO:
    # {{"product": "Самса", "price":  120}, {"product": "Шава", "price":  250}}
    
    def __init__(self, productCards: ProductCards):
        self.product     = productCards.title
        self.price       = productCards.specPrice
        self.description = productCards.description
        self.image       = productCards.image_id

    async def get_image(self):
        image : Images = await Images.get_rowById(cls=Images, id=self.image)
        self.image = image.file_path
        return image
        