from pathlib import Path


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = Path(self.__file_name)
        if not file.exists():
            return ""

        with open(self.__file_name, "r") as f:
            shop_store = f.read()
        return shop_store

    def add(self, *products):
        shop_store = self.get_products()

        for product in products:
            if not isinstance(product, Product):
                continue
            if product.name in shop_store:
                print(f"Продукт {product.name} уже есть в магазине")
                continue
            shop_store += f"{product}\n"

        with open(self.__file_name, "w") as f:
            f.write(shop_store)


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product("Potato", 50.5, "Vegetables")
    p2 = Product("Spaghetti", 3.4, "Groceries")
    p3 = Product("Tomato", 5.5, "Vegetables")
    print(p2)  # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())
