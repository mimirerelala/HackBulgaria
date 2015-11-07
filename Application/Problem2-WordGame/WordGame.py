__author__ = 'mimirerelala'

import numpy as n

char_array = n.genfromtxt('input_array.txt', delimiter=' ', dtype='str')
name_to_look_for = 'bib'


def if_string_symmetric(some_string):
    is_symmetric = True
    some_string_len = len(some_string)
    for m in range(some_string_len):
        if some_string[m] == some_string[some_string_len - m-1]:
            continue
        else:
            is_symmetric = False
    return is_symmetric


def get_the_string(in_data, x, y, delta_x, delta_y, length):
    string_array = n.empty(length, dtype='string')
    for k in range(length):
        string_array[k] = in_data[x, y]
        x += delta_x
        y += delta_y
    return string_array


def return_string_number(data, row, col, search_array_string, word_len):
    current_count = 0

    #look up
    if row + 1 >= word_len:
        if n.array_equal(get_the_string(data, row, col,-1, 0 , word_len), search_array_string):
            current_count += 1

    #look down
    if len(data)-row >= word_len:
        if n.array_equal(get_the_string(data, row, col,1, 0 , word_len), search_array_string):
            current_count += 1

    #look left
    if col + 1 >= word_len:
        if n.array_equal(get_the_string(data, row, col,0, -1 , word_len), search_array_string):
            current_count += 1

    #look right
    if len(data[row]) - col >= word_len:
        if n.array_equal(get_the_string(data, row, col,0, 1 , word_len), search_array_string):
            current_count += 1

    #look upleft
    if row + 1 >= word_len and col + 1 >= word_len:
        if n.array_equal(get_the_string(data, row, col, -1, -1, word_len), search_array_string):
            current_count += 1

    #look upright
    if row + 1 >= word_len and len(data[row]) - col >= word_len:
        if n.array_equal(get_the_string(data, row, col, -1, 1, word_len), search_array_string):
            current_count += 1

    #look downleft
    if len(data)-row >= word_len and col + 1 >= word_len:
        if n.array_equal(get_the_string(data, row, col, 1, -1, word_len), search_array_string):
            current_count += 1

    #look downright
    if len(data)-row >= word_len and len(data[row]) - col >= word_len:
        if n.array_equal(get_the_string(data, row, col, 1, 1, word_len), search_array_string):
            current_count += 1

    return current_count


def iterate_over_whole_table():
    substring_len = len(name_to_look_for)
    search_array = n.array(list(name_to_look_for))
    word_counter = 0
    for i in range(len(char_array)):
        for j in range(len(char_array[i])):
            if char_array[i,j] == search_array[0]:
                word_counter += return_string_number(char_array, i, j, search_array, substring_len)
    if (if_string_symmetric(name_to_look_for)):
        word_counter /= 2
    return word_counter


print iterate_over_whole_table()
