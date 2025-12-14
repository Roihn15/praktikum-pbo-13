from models import Product

class ProductRepository:
    def __init__(self):
        self.products = {
            1: Product(1, "Keyboard", 150000),
            2: Product(2, "Mouse", 80000),
            3: Product(3, "Monitor", 2000000),
        }

    def get_product_by_id(self, product_id):
        return self.products.get(product_id)
