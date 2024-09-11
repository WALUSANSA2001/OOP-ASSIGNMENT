class Laptop:
    def __init__(self, brand, model, battery_capacity):
        self.brand = brand  # The brand of the laptop (e.g., Dell)
        self.model = model  # The model of the laptop (e.g., XPS 13)
        self.battery = Battery(battery_capacity)  # Battery object with a specific capacity

    def type_on_keyboard(self, text):
        print(f"Typing '{text}' on the {self.model}'s keyboard...")

    def display_on_screen(self, content):
        print(f"Displaying '{content}' on the {self.model}'s screen...")

    def check_battery(self):
        print(f"Battery level: {self.battery.charge_level}%")

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity  # The battery capacity in mAh
        self.charge_level = 100  # The current charge level (starts at 100%)

    def charge(self):
        self.charge_level = 100  # Fully charge the battery
        print("Battery fully charged.")

    def use(self, amount):
        if self.charge_level - amount >= 0:
            self.charge_level -= amount  # Reduce the charge level by the amount used
            print(f"Used {amount}% of battery. Remaining: {self.charge_level}%")
        else:
            print("Not enough battery. Please charge.")
            # Creating a Laptop object
my_laptop = Laptop("Dell", "XPS 13", 5000)
print(f"Brand: {my_laptop.brand}, Model: {my_laptop.model}")

# Using the keyboard and screen methods
my_laptop.type_on_keyboard("Hello, world!")
my_laptop.display_on_screen("Welcome to your new laptop!")

# Checking the battery level
my_laptop.check_battery()

# Using the Battery object within the Laptop
my_laptop.battery.use(30)
my_laptop.battery.charge()