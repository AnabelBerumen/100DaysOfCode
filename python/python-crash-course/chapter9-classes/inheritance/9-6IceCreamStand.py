class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name} \nType: {self.cuisine_type}")


    def open_restaurant(self):
        print(f"The Restaurant {self.restaurant_name} is open.")



class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name,cuisine_type="Ice cream stand"):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []
    

    def stored_flavors(self):
        print("This is the list of ice cream flavors: ")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")


ice_cream = IceCreamStand("El rey helado")
ice_cream.flavors = ["Chocolate", "Vainilla", "Fresa", "kiwi"]

ice_cream.describe_restaurant()
ice_cream.stored_flavors()

    

