class Product:
    discount = 0.0   
    
    def __init__(self, pid=0, pname="Unknown", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Constructor Called. Product Created.")

    def __del__(self):
        print("Destructor Called. Product Destroyed.")

    # method to display product details
    def show_product(self):
        print(f"\nProduct ID: {self.pid}")
        print(f"Product Name: {self.pname}")
        print(f"Price (before discount): {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Discount: {Product.discount}%")
        print(f"Price (after discount): {self.get_discounted_price()}")

    # static method to set discount for all products
    @staticmethod
    def set_discount(discount_percent):
        Product.discount = discount_percent
        print(f"Discount set to {Product.discount}% for all products.")

    # method to get discounted price
    def get_discounted_price(self):
        return self.price - (self.price * Product.discount / 100)


# Example usage
if __name__ == "__main__":
   
    p1 = Product()
    p1.show_product()

    p2 = Product(101, "Laptop", 60000, 5)
    p2.show_product()

    Product.set_discount(10)  # 10% discount for all products
    p2.show_product()

    p3 = Product(102, "Mobile", 20000, 10)
    p3.show_product()

    del p3
