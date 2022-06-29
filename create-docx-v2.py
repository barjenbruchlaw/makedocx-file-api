from dataclasses import replace
from docx import Document

document = Document("Judgment - Jackson County.docx")

paragraphs = document.paragraphs

replacement_dict = dict()

for a in range(len(paragraphs)):
    next_line = paragraphs[a].text
    if "{{" in next_line:
        braces_count = next_line.count("{{")
        all_braces_index = list()
        search_term_index = list()
        for b in range(len(next_line)):
            c = b+2
            if next_line[b:c] == "{{":
                all_braces_index.append(b)
        for d in range(len(next_line)):
            e = d+2
            if next_line[d:e] == "}}":
                all_braces_index.append((d+2))
        all_braces_index.sort()
        i = 0
        while i < len(all_braces_index):
            next_search_term = next_line[all_braces_index[i]:all_braces_index[i+1]]
            search_term_index.append(next_search_term)
            i+=2
        replacement_dict.update({a: [all_braces_index, search_term_index, next_line]})

print(replacement_dict)

key_list = list()

for f in replacement_dict:
    key_list.append(f)

key_list.sort()

last_key = key_list[-1]

g = 0

while g <= last_key:
    if g in replacement_dict.keys():
        print(replacement_dict[g])
    else:
        print(g)
    g+=1

