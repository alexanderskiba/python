class Pet:
    def __init__(self, name=None):
        pass
        # print("Я инит класса пет")

class Dog(Pet):
    def __init__(self, name=None):
        pass
        # super(Dog,self).__init__()
        # print("Я инит класса дог")
    def mem (self):
        pass

print(isinstance(Dog(),Pet))
print(isinstance(Dog(),Dog))
print(isinstance(Dog,Dog))
print(isinstance(Pet(),Dog))
print(isinstance(Pet(),object))

print(issubclass(Dog, object))
print(issubclass(Pet, Dog))
print(issubclass(Pet, object))
print(issubclass(Dog, Pet))


