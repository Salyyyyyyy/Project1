# Base Product Class
class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_product_info(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity} "

# DigitalProduct Class (Derived from Product)
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, quantity, file_size, download_link):
        super().__init__(product_id, name, price, quantity)
        self.file_size = file_size
        self.download_link = download_link

    def get_product_info(self):
        product_info = super().get_product_info()  # Calling the base class method
        return f"{product_info}, File size: {self.file_size} MB, Download link: {self.download_link}"

# PhysicalProduct Class (Derived from Product)
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, quantity, weight, dimensions, shipping_cost):
        super().__init__(product_id, name, price, quantity)
        self.weight = weight
        self.dimensions = dimensions
        self.shipping_cost = shipping_cost

    def get_product_info(self):
        product_info = super().get_product_info()  # Calling the base class method
        return f"{product_info}, Weight: {self.weight} kg, Dimensions: {self.dimensions}, Shipping cost: ${self.shipping_cost}"

# Cart Class
class Cart:
    def __init__(self):
        self.__cart_items = []

    def add_product(self, product):
        self.__cart_items.append(product)

    def remove_product(self, product_id):
        for product in self.__cart_items:
            if product.product_id == product_id:
                self.__cart_items.remove(product)
                print(f"Product {product_id} removed.")
                return
        print("Product not found.")

    def view_cart(self):
        if not self.__cart_items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            for product in self.__cart_items:
                print(product.get_product_info())

    def calculate_total(self):
        total = 0
        for product in self.__cart_items:
            total += product.price * product.quantity
        return total

    def apply_discount(self, discount):
        total = self.calculate_total()
        return discount.apply_discount(total)

# User Class
class User:
    def __init__(self, user_id, name, cart):
        self.user_id = user_id
        self.name = name
        self.cart = cart

    def add_to_cart(self, product):
        self.cart.add_product(product)

    def remove_from_cart(self, product_id):
        self.cart.remove_product(product_id)

    def checkout(self, discount=None):
        total = self.cart.calculate_total()
        print(f"Total before discount: ${total:.2f}")
        if discount:
            total_after_discount = self.cart.apply_discount(discount)
            print(f"Total after discount: ${total_after_discount:.2f}")
        else:
            print(f"Total: ${total:.2f}")
        self.cart = Cart()  # Clear the cart after checkout

# Abstract Discount Class
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, total_amount):
        pass

# Percentage Discount Class
class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_amount):
        return total_amount * (1 - self.percentage / 100)

# Fixed Amount Discount Class
class FixedAmountDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, total_amount):
        return total_amount - self.amount

# Example usage
# Create products
product1 = DigitalProduct(1, "Ebook", 15.00, 1, 5, "www.ebookdownloadlink.com")
product2 = PhysicalProduct(2, "Smartphone", 500.00, 1, 0.2, "10x5x2 cm", 10.00)

# Create cart and user
cart = Cart()
user = User(1, "Alice", cart)

# Add products to the cart
user.add_to_cart(product1)
user.add_to_cart(product2)

# View cart
user.cart.view_cart()

# Apply discount (Percentage discount of 10%)
discount = PercentageDiscount(10)

# Checkout with discount
user.checkout(discount)
