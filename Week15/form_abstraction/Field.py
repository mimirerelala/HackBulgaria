from abc import ABCMeta, abstractmethod


class BaseField(metaclass=ABCMeta):
    @abstractmethod
    def is_valid(self):
        return True

    @abstractmethod
    def __str__(self):
        pass

class Form(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        pass
#--------------------------------


class TextField(BaseField):
    def is_valid(self):
        return True

    def __str__(self):
        return "<input />"

class PasswordField(BaseField):
    def is_valid(self):
        return True

    def __str__(self):
        return "<input />"

#--------------------------------

class LoginForm(Form):
    name = TextField()
    password = PasswordField()