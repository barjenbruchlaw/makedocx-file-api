from find_replacement_terms import find_terms

def rebuild_run(old_run,term_dictionary):
    old_text = old_run["text"]
    replaced_terms = find_terms(old_text)
    new_text_array = [old_text]
    for each_term in replaced_terms:
        replacing_term = term_dictionary[each_term]
        new_text_entry = new_text_array[-1].replace(each_term, replacing_term)
        new_text_array.append(new_text_entry)
    new_text = new_text_array[-1]
    new_run = old_run
    new_run["text"] = new_text



