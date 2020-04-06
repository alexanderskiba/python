import os
import tempfile

# class Iterator:


class File:

    def __init__(self, storage_path):
        self.storage_path = storage_path
        if not os.path.exists(storage_path):
            open(storage_path,'w').close()

    def __str__(self):
        return self.storage_path

    def read(self):
        with open(self.storage_path, 'r') as f:
            return f.read()

    def write(self, string):
        with open(self.storage_path, 'w') as f:
            return f.write(string)

    def __add__(self,adding):
        # with open(self.storage_path,'w') as f:
        cls = type(self) #класс File
        obj = cls (os.path.join(tempfile.gettempdir(), 'tmp.txt')) #создаем экземпляр класса, в который передаем путь + название нового файла
        obj.write(self.read() + adding.read()) #записываем в новый файл внутренности экземпляра + второго экземпляра
        return obj

    # запись(чтение экземпляра + чтение объекта)

    def __iter__(self):
        self.cursor = 0
        with open(self.storage_path, 'r') as f:
            self.lines = f.readlines()
        return self

    def __next__(self):
        try:
            line = self.lines[self.cursor]
            self.cursor += 1
            return line
        except IndexError: #когда кончаются индексы вызываем StopIteration
            raise StopIteration