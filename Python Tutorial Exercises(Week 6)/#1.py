'''
Organising data by using class and methods.
Created an __init__ method to store all the elements we need later
new_car = input values
Created 3 different methods to slove this Exercise' problem as asked
print_name prints the make and model. Use self.make &v self.model will be easier to manage for later on. The value will be changed automatically
print_info stores all the information about the car
estimate_value returns the estimate value by using the equation for calculating in the exercise.
Use return to send a value back to the main program
'''

class Car:
    #Instance variables 
    def __init__ (self, make, model, year, max_speed, purchase_price, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.purchase_price = purchase_price
        self.mileage = mileage

    def print_name(self):
        print(self.make,self.model)

    def print_info(self):
        print(f'Mark: {self.make}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Max speed: {self.max_speed}mph')
        print(f'Purchase price: ${self.purchase_price}')
        print(f'Mileage: {self.mileage}km')

    def estimate_value(self):
        return (round(self.purchase_price * (1 - self.mileage / 300000)**2))


new_car = Car("SSC", "Tuatara", 2020, 283, 2000000, 50677)
#              Mark     Model   Year   MS   price   Mileage
new_car.print_name()
new_car.print_info()
new_value = new_car.estimate_value()
print(new_value)
