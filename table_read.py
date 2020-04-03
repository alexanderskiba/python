import os
import csv
class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    def get_photo_file_ext(self): # получение расширения фотофайла (os.path.splittext)
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = int(passenger_seats_count) # вероятно этот атрибут надо сделать атрибутом класса
    # def passenger_seats_count(self):
    #     return self.passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        self.body_whl = body_whl
        try:
            new_whl_list = self.body_whl.split('x',2)
            self.body_width = float(new_whl_list[1])
            self.body_height = float(new_whl_list[2])
            self.body_length = float(new_whl_list[0])
        except:
            self.body_width = 0.0
            self.body_height = 0.0
            self.body_length = 0.0
    def get_body_volume(self):
        result = self.body_width * self.body_height * self.body_length
        return result


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra

def create_object(klasse):
    if klasse.get_photo_file_ext() not in ['.jpg', '.jpeg', '.png', '.gif',]:
        return ''
    else:
        x = klasse

        return x

def get_car_list(csv_filename):
    try:
        car_list = []
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                # print(type(row))
                if len(row) < 5:
                    continue
                if row[4] == "":
                    row[4] = '0.0x0.0x0.0'
                if row[0] == 'car': #таким образом проверяем класс автомобиля, далее else проверка на truck итд
                    #вложенным условием будет проверка на валидность : по индексу будем проверять валидность каждой строки
                     if row[1] and row[2] and row[3] and row[5]:
                        car_list.append(create_object(Car(row[1], row[3], row[5], row[2] ))) #создан экземпляр класса с атрибутами
                if row[0] == 'truck':
                    if row[1] and row[3] and row[4] and row[5]: #Порядок аргументов проверить
                        car_list.append(create_object(Truck(row[1],row[3],row[5],row[4])))
                        # print(create_object(Truck))
                if row[0] == 'spec_machine':
                    if row[1] and row[3] and row[5] and row[6]:
                        car_list.append(create_object(SpecMachine(row[1], row[3], row[5], row[6])))
                        # print(create_object(SpecMachine))
    except IndexError:
        pass
    if car_list == ['']:
        return []
    else:
        return car_list
# print (get_car_list('cars_week3.csv'))
