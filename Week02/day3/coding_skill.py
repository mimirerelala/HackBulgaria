import sys
import json


def main():
    if len(sys.argv) > 1:
        data_input = sys.argv[1]
    else:
        data_input = 'data.json'
    result = {}
    with open(data_input, 'r') as f:
        data = json.load(f)
    for people in data['people']:
        for skill in people['skills']:
            new_skill = skill['name']
            if new_skill in result:
                if skill['level'] > result[new_skill][0]:
                    result[new_skill] = [skill['level'],people['first_name'] + ' ' + people['last_name']]
            else:
                result[new_skill] = [skill['level'],people['first_name'] + ' ' + people['last_name']]
    print(result)
    for key in result:
        print(key, result[key][1])


if __name__ == '__main__':
    main()

