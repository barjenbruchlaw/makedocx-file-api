from docx import Document

document = Document("Judgment - Missouri.docx")

# document_style_list = document.styles
#
# for style in document_style_list:
#     print(style)

# sections = document.sections
#
# for section in sections:
#     print(section)

# paragraphs = document.paragraphs
#
# for paragraph in paragraphs:
#     print(paragraph)

tables = document.tables

table_map = list()

for table_count, table in enumerate(tables):
    table_map.append(list())
    table_map_table = table_map[table_count]
    rows = table.rows
    for row_count, row in enumerate(rows):
        table_map_table.append(list())
        table_map_row = table_map_table[row_count]
        cells = row.cells
        for cell_count, cell in enumerate(cells):
            table_map_row.append(list())
            table_map_cell = table_map_row[cell_count]
            paragraphs = cell.paragraphs
            for paragraph_count, paragraph in enumerate(paragraphs):
                table_map_cell.append([paragraph_count, paragraph.text])

print(table_map)
