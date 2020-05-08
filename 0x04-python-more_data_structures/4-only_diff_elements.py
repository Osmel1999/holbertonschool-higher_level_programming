#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = []
    my_list = set_1 - set_2
    my_list.append(set_2 - set_1)
    return my_list
