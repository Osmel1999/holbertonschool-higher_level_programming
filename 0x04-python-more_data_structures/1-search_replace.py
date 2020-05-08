#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list.pop(i)
            my_list.insert(replace, i)
            new_list = my_list
    return new_list
