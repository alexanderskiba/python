import csv
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count # вероятно этот атрибут надо сделать атрибутом класса


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.body_whl = body_whl
    def get_body_volume(self,body_width, body_height, body_length):
        result = body_width*body_height*body_length # метод, возвращающий объем кузова
        return result


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def create_object(klasse):
    x = klasse
    return x

def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            # print(row)
            if row[0] == 'car': #таким образом проверяем класс автомобиля, далее else проверка на truck итд
                #вложенным условием будет проверка на валидность : по индексу будем проверять валидность каждой строки

                print(create_object(Car))
    return car_list
get_car_list('test_table.csv')