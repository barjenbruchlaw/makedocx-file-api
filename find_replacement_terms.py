def find_terms(text):
    all_braces_index = list()
    search_term_index = list()
    if "{{" in text:
        for b in range(len(text)):
            c = b+2
            if text[b:c] == "{{":
                all_braces_index.append(b)
        for d in range(len(text)):
            e = d+2
            if text[d:e] == "}}":
                all_braces_index.append((d+2))
        all_braces_index.sort()
        i = 0
        while i < len(all_braces_index):
            if len(all_braces_index)<2:
                i += 2
                continue
            else:
                next_search_term = text[all_braces_index[i]:all_braces_index[i+1]]
                search_term_index.append(next_search_term)
                i += 2
    return search_term_index