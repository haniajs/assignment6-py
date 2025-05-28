class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        """Get the price."""
        return self._price

    @price.setter
    def price(self, value):
        """Set the price, ensure it's a positive number."""
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        """Delete the price."""
        print("Deleting price...")
        del self._price

p = Product(100)
print(p.price) 

p.price = 150
print(p.price) 

del p.price
