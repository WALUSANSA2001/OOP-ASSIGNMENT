class Torch:
    def __init__(self, brand, battery_life):
        self.brand = brand  
        self.battery_life = battery_life 
        self.is_on = False  

    def switch_on(self):
        if not self.is_on:
            self.is_on = True
            print(f"The {self.brand} torch is now ON.")
        else:
            print(f"The {self.brand} torch is already ON.")

# Example Usage
my_torch = Torch("Maglite", 10)
my_torch.switch_on()