#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0:
            return my_list
        if idx > len(my_list):
            return my_list
        newlst = my_list[:]
        newlst[idx] = element
        return my_list