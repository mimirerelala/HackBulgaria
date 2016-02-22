import datetime
from time import sleep
from functools import wraps


def encrypt(char_difference):
    def encrypter(func):
        @wraps(func)
        def decorated(input_string):
            input_string_arr = list(input_string)
            for ch_index in range(len(input_string_arr)):
                if input_string_arr[ch_index] is not " ":
                    input_string_arr[ch_index] = chr(ord(input_string_arr[ch_index])+char_difference)
            return func("".join(input_string_arr))
        return decorated
    return encrypter


def log(filename):
    def logger(func):
        def save_to_file():
            with open(filename, 'a') as fn:
                fn.write("{} was called at {}\n".format(func.__name__, datetime.datetime.now()))
            return func()
        return save_to_file
    return logger


def performance(filename):
    def logger(func):
        def eval_time():
            print("eval_started", datetime.datetime.now())
            function_result = func()
        
            print("evel ended", datetime.datetime.now())
            with open(filename, 'a') as fn:
                fn.write("{} was called at {}\n".format(func.__name__, datetime.datetime.now()))
            return function_result
        return eval_time
    return logger

@performance('log.txt')
@encrypt(2)
def get_low(input_string):
    sleep(2)
    print("function is actually called",datetime.datetime.now())
    return input_string

print(get_low("Get get get low"))


