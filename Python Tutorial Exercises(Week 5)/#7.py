'''
The total number of each car is obtained by adding the values of x, y, and z. (x[0]+y[0]+z[0]... and so on)
Zip cars list and total_number list together
convert list to a dictionary by using .dict()
print the final dictionary at the end
'''
cars = ["Hyundai Kona", "Kia Soul", "Mazda CX-30", "Volkswagen Taos", "BMW X1", "BMW X2"]
old_prices = [22545, 20505, 23425, 24490, 36395, 37595]
jan_increase = [540, 120, 600, 199, 1000, 3050]
feb_increase = [153, 200, 123, 385, 450, 600]

print({i : x for i, x in zip(cars,[x + y + z for x, y, z in zip(jan_increase, feb_increase, old_prices)])})

