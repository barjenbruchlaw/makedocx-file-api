from dataclasses import replace
from datetime import datetime
from docx import Document

document = Document("message-template.docx")

paragraphs = document.paragraphs

paragraph_count = len(paragraphs)

table_count = len(document.tables)

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

static_term_dict = {
    "{{ name }}": "Fred Jones",
    "{{ datetime }}": dt_string,
    "{{ message }}": "Hello world!  This is a generated Word document.",
}

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
            i += 2
        replacement_dict.update(
            {a: [all_braces_index, search_term_index, next_line]})

print(replacement_dict)

j = 0

while j < paragraph_count:
    if j in replacement_dict:
        replaced_term = replacement_dict[j][1][0]
        replacing_term = static_term_dict[replaced_term]
        new_paragraph = replacement_dict[j][2].replace(
            replaced_term, replacing_term)
        paragraphs[j].clear()
        paragraphs[j].add_run(text=new_paragraph)
    j += 1

key_list = list()

for f in replacement_dict:
    key_list.append(f)

key_list.sort()

last_key = key_list[-1]

if table_count > 0:
    table = document.tables[0]
    table_matrix = []

    for row in table.rows:
        table_row = []
        for cell in row.cells:
            table_row.append(cell.text)
        table_matrix.append(table_row)

    print(table_matrix)

print("paragraph count = "+str(paragraph_count))
print("table count = "+str(table_count))

document.save('new-message.docx')
