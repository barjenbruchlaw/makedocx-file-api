from dataclasses import replace
from docx import Document

document = Document("message-template.docx")

paragraphs = document.paragraphs

replacement_field_map_rough = list()

for a in paragraphs:
    replace_index = [0]
    next_line = a.text
    next_index = next_line.find("{{", replace_index[-1])
    replace_index.append(next_index)
    if replace_index[-1] != -1:
        close_replace_index = [0]
        close_index = next_line.find("}}", close_replace_index[-1])
        close_replace_index.append(close_index+2)
        replace_index.extend(close_replace_index)
    replacement_field_map_rough.append(replace_index)

replacement_field_map = list()

for b in replacement_field_map_rough:
    if b[1] == -1:
        replacement_field_map.append(False)
    else:
        replacement_field_map_entry = [True]
        cleaned_b = [b[1], b[3]]
        replacement_field_map_entry.append(cleaned_b)
        replacement_field_map.append(replacement_field_map_entry)

def get_coords(list):
    coords_list = list[1]
    starting_point = coords_list[0]
    end_point = coords_list[1]
    return [starting_point, end_point]

search_item_list = list()

for c in range(len(replacement_field_map)):
    if replacement_field_map[c] != False:
        scanned_line = paragraphs[c].text
        search_item_coords = get_coords(replacement_field_map[c])
        search_item = scanned_line[search_item_coords[0]:search_item_coords[1]]
        search_item_index = [c, search_item_coords, search_item]
        search_item_list.append(search_item_index)

print(search_item_list)