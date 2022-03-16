car_and_price = {"Ford Mustang": 6590,
                 "Suzuki Swift": 2400,
                 "Jeep Wrangler": 30099,
                 "Honda Civic": 4500,
                 "Toyota Corolla": 4999,
                 "Audi A4": 20000}
u = [key for key, val in car_and_price.items() if val <= 5000]
print(u)

z = []
for i,n in car_and_price.items():
    if n <=5000:
        z.append(i)
print(z)