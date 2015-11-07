__author__ = 'mimirerelala'

import numpy as n

char_array = n.genfromtxt('input_array.txt', delimiter=' ', dtype='str')
name_to_look_for = 'bib'


def if_string_symmetric(some_string):
    """ Function to check if the input word is palindrome
    :param some_string: input string
    :return: boolean value
    """
    is_symmetric = True
    some_string_len = len(some_string)
    for m in range(some_string_len):
        if some_string[m] == some_string[some_string_len - m-1]:
            continue
        else:
            is_symmetric = False
    return is_symmetric


def get_the_string(in_data, x, y, delta_x, delta_y, length):
    """
    This function returns a word in a specific direction given input charr array data, initial position (x, y),
    give the direction in which to look via delta_x/delta_y and the length of the word we are looking for!
    :param in_data: numpy array of dtype string, containing input chars
    :param x: position of the start letter (row)
    :param y: position of the start letter (col)
    :param delta_x: direction in which to look for the word (on x)
    :param delta_y: direction in which to look for the word (on y)
    :param length: length of input word
    :return:numpy array of the letters of the current word being checked
    """
    string_array = n.empty(length, dtype='string')
    for k in range(length):
        string_array[k] = in_data[x, y]
        x += delta_x
        y += delta_y
    return string_array


def calculate_string_occurance(data, row, col, search_array_string, word_len):
    """
    This function is called if the letter at position data[row,col] is the first letter of the searched word.
    Now, we will check if the word can be found in each direction!
    :param data: numpy array of dtype string, containing input chars
    :param row: current letter coordinates in data
    :param col: current letter coordinates in data
    :param search_array_string: the text string we are looking for
    :param word_len: length of the searched word
    :return: int of occurances of the searched word, starting from the current position [row, col] in each direction
    """
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
    """
    Test the whole input array, for the starting letter of the searched word;
    If the two letters coincide, check with the function calculate_string_occurance() how many times the word
    could be read in the different directions of the array. Iterate over the whole array and sum results.
    If the word is palindrome (symmetric) divide results by two!
    :return:word counter
    """
    substring_len = len(name_to_look_for)
    search_array = n.array(list(name_to_look_for))
    word_counter = 0
    for i in range(len(char_array)):
        for j in range(len(char_array[i])):
            if char_array[i,j] == search_array[0]:
                word_counter += calculate_string_occurance(char_array, i, j, search_array, substring_len)
    if (if_string_symmetric(name_to_look_for)):
        word_counter /= 2
    return word_counter


print iterate_over_whole_table()
