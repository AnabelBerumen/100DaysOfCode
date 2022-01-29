class Restaurant:

    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}, Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The Restaurant {self.restaurant_name} is open.")


restaurantA =Restaurant("Morenas", "Indian")
restaurantB = Restaurant("Oishi", "Japanese")
restaurantC = Restaurant("kikiripio", "Urban")



restaurantA.describe_restaurant()
restaurantA.open_restaurant()

restaurantB.describe_restaurant()

restaurantC.describe_restaurant()

restaurant = Restaurant("Allegro", "Coffe shop")
print(restaurant.number_served)
restaurant.number_served = 12
print(restaurant.number_served)