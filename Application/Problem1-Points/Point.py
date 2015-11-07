__author__ = 'mimirerelala'

starting_point = (0,0)
given_path = ">>><<<~>>>~^^^"

def calculate_new_position(initial_position, path):
    (x,y) = initial_position
    direction_coefficient = 1
    for i in range(len(path)):
        if (path[i]=='>'):
            x += direction_coefficient
        elif (path[i]=='<'):
            x -= direction_coefficient
        elif (path[i]=='^'):
            y += direction_coefficient
        elif (path[i]=='v'):
            y -= direction_coefficient
        elif (path[i]=='~'):
            direction_coefficient = - direction_coefficient
    return (x, y)

final_position = calculate_new_position(starting_point, given_path)
print final_position