
# Assignment 1: Design Your Own Class! 🏗️
#    1. Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#    2.Add attributes and methods to bring the class to life!
#    3. Use constructors to initialize each object with unique values.
#    4.Add an inheritance layer to explore polymorphism or encapsulation.

# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


# Child class (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # Call parent constructor
        self.storage = storage           # in GB
        self.__battery = battery         # private attribute (encapsulation)

    def make_call(self, number):
        return f"📞 Calling {number} from {self.device_info()}..."

    def get_battery(self):
        return f"🔋 Battery level: {self.__battery}%"

    def use_app(self, app, hours):
        self.__battery -= hours * 5
        if self.__battery < 0:
            self.__battery = 0
        return f"📱 Used {app} for {hours}h. {self.get_battery()}"


# Another subclass (polymorphism example)
class Tablet(Device):
    def __init__(self, brand, model, stylus_support):
        super().__init__(brand, model)
        self.stylus_support = stylus_support

    def device_info(self):
        info = super().device_info()
        return info + (" with stylus ✍️" if self.stylus_support else "")


# --- Testing our classes ---
phone = Smartphone("Samsung", "Galaxy S22", 128, 80)
tablet = Tablet("Apple", "iPad Pro", True)

print(phone.make_call("0712345678"))
print(phone.use_app("Instagram", 3))
print(tablet.device_info())





# Activity 2: Polymorphism Challenge! 🎭

#     Create a program that includes animals or vehicles with the same action (like move()).
#     However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, 
#     while Plane.move() prints "Flying" ✈️).


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"


class Bike(Vehicle):
    def move(self):
        return "🚴 Pedaling along the path"


# --- Polymorphism in action ---
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    print(v.move())
