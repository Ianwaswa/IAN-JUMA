car_name = "Volvo"
other_car = "Toyota"
car_mileage = "1000"
response = f"I have a {car_name} car that has {car_mileage} miles on it."
for car in [car_name, other_car, car_mileage]:
    if car == car_name:
        response = response.replace(car, "Volvo")
    elif car == other_car:
        response = response.replace(car, "Toyota")
    elif car == car_mileage:
        response = response.replace(car, "1000")
print(response)