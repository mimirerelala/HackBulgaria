class Panda:

    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight

    def eat(self, amount):
        self._weight += amount

    def sleep(self):
        self._age += 1

    def get_age(self):
        return self._age

    def get_weight(self):
        return self._weight


ivo = Panda("Ivo", 22, 90)
ivo.sleep()
ivo.eat(2)
print(ivo._age, ivo._weight)


"""
Convention
single underscore "_" - shouldnt change it private/protected?

double underscore "__" - changes the method/atribute name -> no one else can use it
e.g __get_age()  is _Panda__get_age()


"""
