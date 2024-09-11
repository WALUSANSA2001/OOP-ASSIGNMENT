class Vehicle:
    

    def __init__(self, make, model, year):
        
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        """Returns information about the vehicle.
        """
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

# Create instances of the Vehicle class
car = Vehicle("Toyota", "Camry", 2023)
bike = Vehicle("Honda", "CBR1000RR", 2022)

# Access and print information about the vehicles
print(car.get_info())
print(bike.get_info())