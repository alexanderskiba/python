from table_read import *
cars = get_car_list('cars_week3.csv')
print (len(cars))

for car in cars:
    print(type(car))

# <class 'solution.Car'>
# <class 'solution.Truck'>
# <class 'solution.Truck'>
# <class 'solution.Car'>
print(cars[0].passenger_seats_count)

print(cars[1].get_body_volume())
# 60.0

#2
cars1 = get_car_list('cars_week3.csv')
print(len(cars1))

for car in cars1:
    print(type(car))
# <class 'solution.Car'>
# <class 'solution.Truck'>
# <class 'solution.Truck'>
# <class 'solution.Car'>
print (cars[0].passenger_seats_count)
# 4
print(cars[1].get_body_volume())
# 60.0
