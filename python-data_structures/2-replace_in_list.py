#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    for i in range(len(my_list)):
        new_list = replace_in_list(my_list,idx,new_element)
        if my_list[i] == new_element:
            print(new_list)
        else:
            print(element)
