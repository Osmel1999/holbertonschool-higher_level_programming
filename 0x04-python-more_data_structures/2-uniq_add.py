#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = []
    for uno in range(len(my_list)):
        for dos in range(len(my_list)):
            if my_list[uno] == my_list[dos] and uno != dos:
                result.append(my_list[uno])
        return result


