import logging
import csv
import re
#Логгер

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# first file logger
logger = setup_logger('first_logger', 'info.log') #Информационный логгер
# logger.info('This is just info message')

# second file logger
super_logger = setup_logger('second_logger', 'error.log') # логгер для ошибок
# super_logger.error('This is an error message')


class RevealAccess(object):
    """Дескриптор данных, который устанавливает и возвращает значения,
       и печатает сообщение о том, что к атрибуту был доступ.
    """

    def _check_date(self, val): #Проверка даты
        if len(val) == 10:  # количество символов включая цифры и знаки препинания в верном формате равно 10
            if not re.match('(\w{4})-(\w{2})-(\w{2})', val):  # проверка на НЕсоответсвие паттерну 1994-10-12
                new_date = re.split('\.|/|-', val)  # сформируем список из чисел
                if len(new_date[2]) == 4:  # если год стоит на последнем месте,
                    new_date = new_date[::-1]  # исправим это
                new_string = '-'.join(new_date)  # соберем все вместе в правильно формате 1994-10-12
                val = new_string
        else:
            super_logger.error('Неверный формат даты')
            raise ValueError('Неверный формат даты')
        return val

    def _check_document_type(self, val): #Проверка типа документа
        _valid_document_types = {
            'Паспорт': ['Паспорт', 'паспорт'],
            'Водительские права': ['Водительские права', 'водительские права', 'права'],
            'Заграничный паспорт': ['Заграничный паспорт', 'заграничный паспорт', 'загран'],
        }
        found = False # флаг найденного значения
        for key, valid_list in _valid_document_types.items():
            if val in valid_list: # Проверка нахождения подаваемого значения в списке допустимых значений
                val = key # В случае успеха приведем значение к человеческому виду
                found = True # соответственно флаг теперь тру
        if not found:
            super_logger.error('Неверный тип документа')
            raise ValueError('Неверный тип документа')
        return val

    def _check_phone(self, val):
        # Проверим и преобразуем номер телефона
        val = re.sub(r'[^0-9]+', r'', val)  # для начала удалим все лишнее(все то, что не цифра)
        if len(val) != 11:
            super_logger.error('Неверное количество цифр в номере телефона')
            raise ValueError('Неверное количество цифр в номере телефона')
        return val

    def _check_doc_id(self, val, doc_type): # в doc_type будем передавать значение из dict объекта по ключу document_type
        _valid_len = {
            'Паспорт': 10,
            'Водительские права': 10,
            'Заграничный паспорт': 9,
        }
        v_len = _valid_len[doc_type]
        val = re.sub(r'[^0-9]+', r'', val)  # удалим все лишнее и непонятное

        if len(val) != v_len:
            super_logger.error('Неверное количество цифр в номере документа')
            raise ValueError('Неверное количество цифр в номере документа ')
        return val

    def __init__(self, name='атрибут'):
        self.name = name
        self.inited = False

    def __get__(self, obj, objtype):
        # print('Получаю', self.name)
        return obj.__dict__[self.name]

    def __set__(self, obj, val):
        if self.name == 'birth_date':
            val = self._check_date(val)
        if self.name == 'phone':
            val = self._check_phone(val)
        if self.name == 'document_type':
            val = self._check_document_type(val)
        if self.name == 'document_id':
            val = self._check_doc_id(val, obj.__dict__.get('document_type'))

        if self.name == 'first_name':
            if self.name in obj.__dict__:
                super_logger.error('Попытка изменить имя')
                raise ValueError('Попытка изменить имя')
        elif self.name == 'last_name':
            if self.name in obj.__dict__:
                super_logger.error('Попытка изменить фамилию')
                raise ValueError('Попытка изменить фамилию')
        else:
            logger.info(
                f"изменяю {self.name} у пациента {obj.first_name} {obj.last_name} c {obj.__dict__.get(self.name, None)} на {val}")
        obj.__dict__[self.name] = val


class Patient:
    header = ['Имя', 'Фамилия', 'Дата рождения', 'Телефон', 'Вид документа', 'Номер документа']
    is_header_written = False

    first_name = RevealAccess('first_name')
    last_name = RevealAccess('last_name')
    birth_date = RevealAccess('birth_date')
    phone = RevealAccess('phone')
    document_type = RevealAccess('document_type')
    document_id = RevealAccess('document_id')
    curent_row_idx = 1 #Указатель на текущую строку

    def __init__(self, first_name, last_name, birth_date, phone, document_type, document_id):
        if not (first_name and last_name and birth_date
                and phone and document_type and document_id):
            super_logger.error('Заполнены не все поля')
            raise ValueError('Заполнены не все поля')

        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.birth_date = birth_date
        self.phone = phone
        self.document_type = document_type
        self.document_id = document_id

        self._saved = False # Флаг, позволящюий узнать сохранен ли объект, по умолчанию False,
                            #  начале объектов у нас нет
        self._row_idx = None # индекс объекта
        logger.info(f'создан объект {self.first_name} {self.last_name} '
                    f'{self.birth_date} {self.phone} {self.document_type} {self.document_id}')

    #         self.validation()

    @classmethod
    def create(cls, first_name, last_name, birth_date, phone, document_type, document_id):
        return cls(first_name, last_name, birth_date, phone, document_type, document_id)

    def save(self):  # сохраняем пациента в csv таблицу
        data = [self.first_name,
                self.last_name,
                self.birth_date,
                self.phone,
                self.document_type,
                self.document_id]

        if self._saved:
            with open('patient.csv', 'r', newline='') as f:
                reader = csv.reader(f, delimiter=';')
                rows = [row for row in reader] # список с объектами
                rows[self._row_idx] = data # элементу списка со всеми пациентами присваются данные конкретного пациенту
            with open('patient.csv', 'w', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerows(rows) # записываем данные в файл с измененными данными одного пациента
        else:
            self._saved = True
            self._row_idx = Patient.curent_row_idx # конкретном объекту присвается номер строки в файле
            Patient.curent_row_idx += 1 #после этого для следующего объекта счетчик +1

            with open('patient.csv', "a", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=';')
                if not Patient.is_header_written:  # Пишем заголовок в файл, он должен быть записан всего один раз, поэтому вот так
                    writer.writerow(Patient.header)
                    Patient.is_header_written = True
                writer.writerow(data)

    def __str__(self):
        return (f'{self.first_name} {self.last_name} {self.birth_date} '
                f'{self.phone} {self.document_type} {self.document_id}')

class PatientCollection:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.patient_list = []
        with open(self.path_to_file) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for ind, row in enumerate (reader,1):
                p = Patient(row[0], row[1], row[2], row[3], row[4], row[5])
                p._saved = True
                p._row_idx = ind
                self.patient_list.append(p)
            Patient.curent_row_idx = len(self.patient_list)
            Patient.is_header_written = True

    def __iter__(self):
            with open('patient.csv', 'rb', buffering=0) as fp:
                next(fp)
                for line in fp:
                    row = line.decode().split(';')
                    p = Patient(*row)
                    yield p

    # def limit(self,num):
    #     with open('patient.csv', 'rb', buffering=0) as fp:
    #         next(fp)
    #         for i, line in enumerate(fp):
    #             if i == num:
    #                 break
    #             row = line.decode().split(';')
    #             p = Patient(*row)
    #             yield p

    def limit(self,num):
        with open('patient.csv', 'rb', buffering=0) as fp:
            next(fp)
            for i in range(num):
                row = next(fp).decode().split(';')
                p = Patient(*row)
                yield p

collection = PatientCollection('patient.csv')
for patient in collection.limit(4):
    print(patient)
#
# a = Patient('vasya', 'pupkin', '12.10.1994', '+7-(915)-690-53-53', 'паспорт', '0123 456789')
# a.save()
# b = Patient('petya', 'petrov', '1994-10-12', '7(915)6905353', 'права', '1234 567891')
# b.save()
# c = Patient.create('Vova', 'Putin', '12-10-1994', '79156905353', 'загран', '1234-56789')
# c.save()
# d = Patient('vasya', 'pupkin', '12.10.1994', '+7-(915)-789-97-87', 'паспорт', '0123 456789')
# d.save()


