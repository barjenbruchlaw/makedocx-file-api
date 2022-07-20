import re
import ast

def string2dict(string_source):
    no_brackets = string_source[1:-1:]

    raw_list = re.split('\}, \{', no_brackets)

    first_element = raw_list[0]
    fixed_first_element = first_element[1::]
    raw_list[0] = fixed_first_element

    last_element = raw_list[-1]
    fixed_last_element = last_element[:-1:]
    raw_list[-1] = fixed_last_element

    final_list = list()

    for raw_list_item in raw_list:
        str_dict_item = '{'+raw_list_item+'}'
        dict_item = ast.literal_eval(str_dict_item)
        final_list.append(dict_item)

    return final_list

