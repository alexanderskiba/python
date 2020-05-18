#Для добавления нового экспортера просто добавляем новый класс(класс-наследний от пет экспорта)


import json
class PetExport: #Класс только для наследования
    def export(self,dog):
        raise NotImplementedError


class ExportJSON(PetExport):
    def export(self,dog):
        return json.dumps({
            "name" : dog.name,
            "breed" : dog.breed,
        })


class ExportXML:
    def export(self,dog):
        return """<?xml version = 1.0 encoding = "utf-8"?>
        <dog>
            <name>{0}</name>
            <breed>{1}</breed>
        </dog>""".format(dog.name,dog.breed)


class Pet:
    def __init__(self,name):
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed
#Не будем использвать наследование, а будем расширять существующий класс Dog
class ExDog(Dog):
    def __init__(self, name, breed=None, exporter = None):
        super().__init__(name,breed=None)
        self._exporter = exporter or ExportJSON()
        if not isinstance(self._exporter, PetExport):
            raise ValueError ("bad exporter", exporter)
    def export(self):
        return self._exporter.export(self)
#
# dog = ExDog("шарик", "Дворняга", exporter=ExportXML())
# print(dog.export())

dog = ExDog("Тузик", "Мопс")
print(dog.export())
