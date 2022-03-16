
cars = ["Hyundai Kona", "Kia Soul", "Mazda CX-30", "Volkswagen Taos", "BMW X1", "BMW X2"]
old_prices = [22545, 20505, 23425, 24490, 36395, 37595]
jan_increase = [540, 120, 600, 199, 1000, 3050]
feb_increase = [153, 200, 123, 385, 450, 600]

total_number = [x + y+ z for (x, y, z) in zip(jan_increase, feb_increase,old_prices)] 
ziped_lists = zip(cars,total_number)
print(dict(ziped_lists))