import logging
import csv
import re
#
# class Logger: #дескриптор
#     def __init__(self):
#         self.value = None
#
#
#     def __get__(self, obj, obj_type):
#         return self.value
#
#     def __set__(self, obj, value):
#         # self.value = self.prepare_value (value, obj.comission)
#         self.value = value - value * obj.commission


class Patient:
    header = ['Имя', 'Фамилия', 'Дата рождения', 'Телефон', 'Вид документа', 'Номер документа']
    is_header_written = False


    def __init__(self, first_name, last_name, birth_date, phone, document_type, document_id):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.phone = phone
        self.document_type = document_type
        self.document_id = document_id
        self.validation()

    @classmethod
    def create(cls,first_name, last_name, birth_date, phone, document_type, document_id):
        return cls(first_name, last_name, birth_date, phone, document_type, document_id)

    def validation(self):
        if (self.first_name and self.last_name and self.birth_date #Проверка имени, фамилии и типа документа сводится
            and self.phone and self.document_type and self.document_id):# к проверке их наличия

            #проверим дату и приведем ее к требуемому виду
            if len(self.birth_date) == 10: # количество символов включая цифры и знаки препинания в верном формате равно 10
                if not re.match('(\w{4})-(\w{2})-(\w{2})', self.birth_date): # проверка на НЕсоответсвие паттерну 1994-10-12
                    self.new_date = re.split('\.|/|-', self.birth_date) #сформируем список из чисел
                    if len(self.new_date[2]) == 4: #если год стоит на последнем месте,
                        self.new_date = self.new_date[::-1] # исправим это
                        self.new_string = '-'.join(self.new_date) #соберем все вместе в правильно формате 1994-10-12
                        self.birth_date = self.new_string
            else:
                raise ValueError('Неверный формат даты')

            #Проверим и преобразуем номер телефона
            self.phone = re.sub(r'[^0-9]+', r'', self.phone) # для начала удалим все лишнее(все то, что не цифра)
            if len(self.phone) != 11:
                raise ValueError('Неверное количество цифр в номере телефона')

            #Проверим паспорт
            if self.document_type == 'Паспорт' or self.document_type == 'паспорт':
                self.document_type = self.document_type.capitalize() #первую букву сделаем заглавной для красоты
                # Проверим номер паспорта, он должен иметь в себе 10 цифр
                self.document_id = re.sub(r'[^0-9]+', r'', self.document_id) #удалим все лишнее и непонятное
                if len(self.document_id) != 10:
                    raise ValueError('Не хватает цифр в номере российского паспорта')

            #Проверим водительские права
            elif (self.document_type == 'права' or self.document_type == 'водительские права' or
                  self.document_type == 'Водительские права'):
                self.document_type = 'Водительские права'
                self.document_id = re.sub(r'[^0-9]+', r'', self.document_id) #удалим все лишнее и непонятное
                if len(self.document_id) != 10:
                    raise ValueError('Неверное количество цифр в номере водительских права')

            #Проверим заграничный паспорт
            elif (self.document_type =='загран' or self.document_type =='загранпаспорт' or
            self.document_type == 'Заграничный паспорт' or self.document_type == 'заграничный паспорт'):
                self.document_type = 'Заграничный паспорт'
                self.document_id = re.sub(r'[^0-9]+', r'', self.document_id)  # удалим все лишнее и непонятное
                if len(self.document_id) !=9:
                    raise ValueError('Неверное количество цифр в заграничном паспорте')
            else:
                raise ValueError('Неверный тип документа')

        else:
            raise ValueError('Заполнены не все поля')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} {self.phone} {self.document_type} {self.document_id} '


    def save(self):# сохраняем пациента в csv таблицу
        data = [self.first_name,
                self.last_name,
                self.birth_date,
                self.phone,
                self.document_type,
                self.document_id]

        with open('patient.csv', "a", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            if not type(self).is_header_written: #Пишем заголовок в файл, он должен быть записан всего один раз, поэтому вот так
                writer.writerow(Patient.header)
                type(self).is_header_written = True
            writer.writerow(data)



class PatientCollection:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.patient_list = []
        with open(self.path_to_file) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                self.patient_list.append(self.create_patient(Patient(row[0], row[1], row[2], row[3], row[4], row[5])))

    def create_patient(self,klasse):
        self.x = klasse
        return self.x

    def __iter__(self):
        for i in self.patient_list:
            yield i

    def __str__(self):
        return f"{str(self.x.first_name)} {str(self.x.last_name)} {str(self.x.birth_date)} {str(self.x.phone)} {str(self.x.document_type)} {str(self.x.document_id)}"


    def limit(self,num):
        for i in range(num):
            yield self.patient_list[i]




a = Patient('vasya', 'pupkin', '12.10.1994', '+7-(915)-690-53-53', 'паспорт', '0123 456789')
a.save()
b = Patient('petya', 'petrov', '1994-10-12', '7(915)6905353', 'права', '1234 567891')
b.save()
c = Patient.create('Vova', 'Putin', '12-10-1994', '79156905353', 'загран', '1234-56789')
c.save()
d = Patient('vasya', 'pupkin', '12.10.1994', '+7-(915)-789-97-87', 'паспорт', '0123 456789')
d.save()



collection = PatientCollection('patient.csv')
for patient in collection:
    print(patient)

# collection = PatientCollection('patient.csv')
# for patient in collection.limit(2):
# 	print(patient)




