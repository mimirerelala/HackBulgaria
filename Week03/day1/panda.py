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

#Magic methods:
#double underscore

    def __str__(self):
        """
        Overrides "to string" or what comes after print
        """
        return "I am {} and I am great!" % self._name

    def __repr__(self):
        return selt.__str__()

    def __eq__(self, other):
        return self._name == other._name

    def __hash__(self):
        return hash(self._name + str(self._age))




ivo = Panda("Ivo", 22, 90)
ivo.sleep()
ivo.eat(2)
print(ivo._age, ivo._weight)


ivo = Panda("Ivo", 22, 90)
rado = Panda("Ivo", 22, 88)
print(ivo == rado)
print(hash(ivo))
# if you redefince __eq__, you must redefine hash, hash breaks


"""

Convention
single underscore "_" - shouldnt change it private/protected?

double underscore "__" - changes the method/atribute name -> no one else can use it
e.g __get_age()  is _Panda__get_age()


"""
