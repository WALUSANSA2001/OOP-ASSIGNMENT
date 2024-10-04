class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock
# method to display product info to the user
    def display_product_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")
#here the shoppingis initialised to 0 basing on the fact that the cart has no item when the user logs in
class ShoppingCart:
    total_carts = 0

    def __init__(self):
        self.items = []
        #here the enables adding items to the cart
        ShoppingCart.total_carts += 1
# method to add items on the list for shopping by the user
    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"{quantity} {product.product_name} added to cart.")
        else:
            print("Insufficient stock.")
# the method here removes an item from the list if not wanted 
    def remove_from_cart(self, product):
        for i, (item, qty) in enumerate(self.items):
            if item == product:
                self.items.pop(i)
                product.quantity_in_stock += qty
                print(f"{product.product_name} removed from cart.")
                break
        else:
            print("Product not found in cart.")
#the method to display items chosen by the user
    def display_cart(self):
        print("Your Cart:")
        for product, quantity in self.items:
            product.display_product_info()
            print(f"Quantity: {quantity}")
            print()
# the method here calculates the total sum odf all items chosen
    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

# Create products
product1 = Product("Laptop", 1000, 5)
product2 = Product("Smartphone", 500, 10)
product3 = Product("Headphones", 100, 20)

# Create shopping carts
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Add items to carts
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 3)
cart2.add_to_cart(product2, 1)
cart2.add_to_cart(product3, 5)