# Count Words


def count_words(arr):
    histogram = {}
    for i in range(len(arr)):
        if arr[i] in histogram:
            histogram[arr[i]] += 1
        else:
            histogram[arr[i]] = 1

    return histogram

print(count_words(["apple", "banana", "apple", "pie"]))
print(count_words(["python", "python", "python", "ruby"]))


def nan_expand(n):
    if n == 0:
        return ""
    else:
        return n * "Not a " + "NaN"

print(nan_expand(0))
print(nan_expand(1))
print(nan_expand(2))
print(nan_expand(3))


def iterations_of_nan_expand(expanded):
    if expanded.count("NaN")==1:
        return expanded.count("Not a")
    else:
        return 0

print(iterations_of_nan_expand(""))
print(iterations_of_nan_expand("Not a NaN"))
print(iterations_of_nan_expand('Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print(iterations_of_nan_expand("Show these people!"))


def group(input_list):
    result = []
    last_list = [input_list[0]]
    for i in range(1, len(input_list)):
        if input_list[i] == input_list[i-1]:
            last_list.append(input_list[i])
        else:
            result.append(last_list)
            last_list = [input_list[i]]
    result.append(last_list)
    return result

print(group([1, 1, 1, 2, 3, 1, 1]))
print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    sequences = group(items)
    max_len = 0
    for seq in sequences:
        if len(seq) > max_len:
            max_len = len(seq)
    return max_len

print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def gas_stations(distance, tank_size, stations):
    to_fuel_at = []
    for i in range(len(stations)-1):
        gas_left = tank_size*(len(to_fuel_at)+1) - stations[i]
        distance_to_end = distance - stations[i]
        distance_to_next_station = stations[i+1] - stations[i]
        if gas_left <= distance_to_next_station and gas_left < distance_to_end:
            to_fuel_at.append(stations[i])

    gas_left = tank_size*(len(to_fuel_at)+1) - stations[-1]
    distance_to_end = distance - stations[-2]
    distance_to_next_station = stations[-1] - stations[-2]
    if gas_left <= distance_to_next_station and gas_left <= distance_to_end:
            to_fuel_at.append(stations[-1])
    return to_fuel_at


print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))



def sum_of_numbers(str):
    list_num = []
    current_digit_str = ""
    for i in range(len(str)):
        if str[i].isdigit():
            current_digit_str += str[i] 
        else:
            if len(current_digit_str) > 0:
                list_num.append(int(current_digit_str))
            current_digit_str = ""
    if len(current_digit_str) > 0:
        list_num.append(int(current_digit_str))
    return sum(list_num)


print(sum_of_numbers("1111"))
print(sum_of_numbers("1abc33xyz22"))
print(sum_of_numbers("abcd"))



dict_sms = {
    " ":[0],
    "a": [2],
    "b": [2,2],
    "c": [2,2,2],
    "d": [3],
    "e": [3,3],
    "f": [3,3,3],
    "g": [4],
    "h": [4,4],
    "i": [4,4,4],
    "j": [5],
    "k": [5,5],
    "l": [5,5,5],
    "m": [6],
    "n": [6,6],
    "o": [6,6,6],
    "p": [7],
    "q": [7,7],
    "r": [7,7,7,7],
    "s": [7,7,7,7],
    "t": [8],
    "u": [8,8],
    "v": [8,8,8],
    "w": [9],
    "x": [9,9],
    "y": [9,9,9],
    "z": [9,9,9,9]
    }

NUMBERS = {
    2:"abc",
    3:"def",
    4:"ghi", 
    5:"jkl", 
    6:"mno",
    7:"pqrs", 
    8:"tuv",
    9:"wxyz",
    0:" ",
    -1:""
}


def numbers_to_message(pressedSequence):
    result = ""
    next_letter_capital = False
    list_commands = group(pressedSequence)
    print list_commands
    for i in range(len(list_commands)):
        if list_commands[i][0]==0:
            result += len(list_commands[i])*" "
        elif list_commands[i][0]==1:
            if len(list_commands[i])%2==1:
                next_letter_capital=True
        else:
            for key in dict_sms:
                if dict_sms[key] == list_commands[i]:
                    if next_letter_capital:
                        print key
                        result += key.upper()
                        next_letter_capital = False
                    else:
                        result += key    
    return result

print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))



def messageToNumbers(messsage):
    
    return
