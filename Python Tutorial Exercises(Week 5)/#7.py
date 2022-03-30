'''
This script uses dictionary comprehension to help Andrew to track the car prices.
Use a for loop :for i in range(len(cars)) to get the order of the cars. 

The length of every list is the same so we can use 'i' to help us match car names with 3 price lists 
and use the "+"/add symbol to help us get the current price for each car from the 3 price lists. 

{cars[i]: old_prices[i]+jan_increase[i]+feb_increase[i]} 
The key(car[i]) is the car names and the value(old_prices[i]+jan_increase[i]+feb_increase[i]) is the current price for each car. 
You get the current price for each car by printing out the dictionary comprehension.
'''

cars = ["Hyundai Kona", "Kia Soul", "Mazda CX-30", "Volkswagen Taos", "BMW X1", "BMW X2"]
old_prices = [22545, 20505, 23425, 24490, 36395, 37595]
jan_increase = [540, 120, 600, 199, 1000, 3050]
feb_increase = [153, 200, 123, 385, 450, 600]

print({cars[i]: old_prices[i]+jan_increase[i]+feb_increase[i] for i in range(len(cars))})
