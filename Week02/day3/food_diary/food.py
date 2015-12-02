import sys
import json


#Implement Levenstain Min Distance Algo :))))


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def write_json(filename, new_dic):
    data = read_json(filename)
    data.update(new_dic)
    with open(filename, 'w') as f:
        json.dump(data, f)


def main():

    while True:
        print("Hello and Welcome!Choose an option.")
        print("1. meal - to write what are you eating now.")
        print("2. list <dd.mm.yyyy> - lists all the meals that you ate that day")
        user_input = input('Input>')
        user_input_list = user_input.split(" ")
        data = read_json()
        print(user_input_list)
        if user_input_list[0] == 'meal':

            print(user_input_list[1])
        
        elif user_input_list[0] == 'list':
            date =  user_input_list[1]
            print(date)

        else:
            print("Wronginput")

if __name__ == '__main__':
    main()
