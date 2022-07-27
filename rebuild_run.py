from find_replacement_terms import find_terms

def rebuild_run(old_run,term_dictionary):
    old_text = old_run.text
    replaced_terms = find_terms(old_text)
    new_text_array = [old_text]
    term_dictionary_final = add_caps_to_dict(term_dictionary)
    for each_term in replaced_terms:
        replacing_term = term_dictionary_final[each_term]
        new_text_entry = new_text_array[-1].replace(each_term, replacing_term)
        new_text_array.append(new_text_entry)
    new_text = new_text_array[-1]
    new_run = old_run
    new_run.text = new_text
    return new_run

def add_caps_to_dict(term_dictionary):
    caps_dict_list = list()
    for each_key in term_dictionary:
        each_value = term_dictionary[each_key]
        if type(each_value) == str:
            key_no_braces = each_key[2:-2]
            key_make_caps = key_no_braces.upper()
            key_final = '{{'+key_make_caps+'}}'
            value_make_caps = each_value.upper()
            caps_dict_list.append({key_final: value_make_caps})
    for caps_dict_entry in caps_dict_list:
        term_dictionary.update(caps_dict_entry)
    return term_dictionary




