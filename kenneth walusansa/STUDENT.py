class Student:
    def __init__(self, name, programme="BSIT"):
        self.name = name  
        self.programme = programme 

    def get_info(self):
        return f"Name: {self.name}, Programme: {self.programme}"

    def change_programme(self, new_programme):
        self.programme = new_programme
        print(f"Programme changed to {self.programme}")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am enrolled in {self.programme}.")

# Example Usage
student1 = Student("KENJACQ")
print(student1.get_info())
student1.greet()

student2 = Student("WALU", "BSIT")
print(student2.get_info())
student2.change_programme("DATA Science")
student2.greet()