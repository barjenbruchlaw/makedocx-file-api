from docx import Document

document = Document('22XX-000000 - John Smith.docx')

paragraphs = document.paragraphs

for paragraph_count,paragraph in enumerate(paragraphs):
    runs = paragraph.runs
    for run_count,run in enumerate(runs):
        if run.text == '\n':
            print(f'paragraph: {paragraph_count}, run: {run_count}')

tables = document.tables
for table_count,table in enumerate(tables):
    rows = table.rows
    for row_count,row in enumerate(rows):
        cells = row.cells
        for cell_count,cell in enumerate(cells):
            paragraphs = cell.paragraphs
            for paragraph_count, paragraph in enumerate(paragraphs):
                runs = paragraph.runs
                for run_count, run in enumerate(runs):
                    if run.text == '\n':
                        print(f'table: {table_count}, row: {row_count}, cell: {cell_count}, paragraph: {paragraph_count}, run: {run_count}')
