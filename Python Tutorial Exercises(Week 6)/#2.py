'''
This script helps Andrew to find out the car data about the cars he bought. 
Which include: make, model, year, max speed, purchase price, mileage.

According to the needs of the exercise, Have to create an andrews_cars list 
to store purchase_prices, mileages, and years lists. 

The length and the data place and order of each list are the same 
so we can use the cars_i_bought list and 'for item in range(len(cars_i_bought))' 
to match the data of the car.

we can use 'for item in range(len(cars_i_bought))' to easily match data 
that is stored in a list, but not in dictionaries. 

For the mark list, we can retrieve the car model from the makes dictionary to get the car mark/brand. 
Use 'for car_name in cars_i_bought' to get all the car names.
Create 2 variables 'makes_model and makes_brand' and .items() to get the keys and values in 'makes' dictionary. 
Use 'if car_name == makes_model' to do name comparison. 
If the name is the same, return the make of the car.

for spend_list we can combine the 'year' and the 'cars_i_bought' list together, 
to retrieve the speeds dictionary. The process is the same as the one above.

To print the data out just have to place those variables in the same order as in class Car.

'''

class Car:
   
    def __init__(self, make, model, year, max_speed, purchase_price, mileage):
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


makes = {"Veyron Super Sport": "Bugatti",
         "Venom GT": "Hennessey",
         "A8": "Audi",
         "ES": "Lexus",
         "Senna": "McLaren",
         "720S": "McLaren",
         "Corvette Stingray": "Chevrolet",
         "Aventador SVJ": "Lamborghini",
         "MX-5 Miata": "Mazda",
         "918 Spyder": "Porsche",
         "Enzo": "Ferrari",
         "Ioniq Hybrid": "Hyundai",
         "LaFerrari": "Ferrari"}

speeds = {"Countach LP500 S 1990": 182,
          "Ioniq Hybrid 2014": 110,
          "Corvette Stingray 2020": 194,
          "Senna 2019": 211,
          "Agera RS 2017": 278,
          "Ultimate Aero 2007": 256,
          "MX-5 Miata 2017": 141,
          "ES 2021": 131,
          "Venom GT 2014": 270,
          "ES 2022": 135,
          "Veyron EB 16.4 2018": 256,
          "Ioniq Hybrid 2016": 115,
          "918 Spyder 2014": 211}

purchase_prices = [24645, 1200000, 28315, 1560000, 845000, 78100, 60900]
mileages = [31244, 50123, 102945, 24642, 30012, 89450, 120324]
years = [2014, 2014, 2017, 2019, 2014, 2021, 2020]

cars_i_bought = ["Ioniq Hybrid", "Venom GT",
                 "MX-5 Miata", "Senna", "918 Spyder", "ES", "Corvette Stingray"]

####Make#####
car_mark = [makes_brand for car_name in cars_i_bought for makes_model,makes_brand in makes.items() if car_name == makes_model]

####Speeds#####
spends_car_names = [str(l1) + ' ' + str(l2) for l1, l2 in zip(cars_i_bought, years)]
spend_list = [speeds_value for item in spends_car_names for speeds_key,speeds_value in speeds.items() if speeds_key == item]


andrews_cars = [ car_mark, cars_i_bought, years, spend_list, purchase_prices, mileages ]

for item in range(len(cars_i_bought)):
    car_check = Car(car_mark[item], cars_i_bought[item], years[item], spend_list[item], purchase_prices[item], mileages[item])
    car_check.print_info()