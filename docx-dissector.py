from docx import Document

document = Document("Judgment - Jackson County.docx")

paragraphs = document.paragraphs

document_diagram = list()

for paragraph_count, paragraph in enumerate(paragraphs):
    document_diagram.append([paragraph_count, list()])
    document_diagram_paragraph_entry = document_diagram[paragraph_count][1]
    document_diagram_paragraph_entry.append(dict())
    document_diagram_paragraph_format_elements = document_diagram_paragraph_entry[0]
    paragraph_elements_list = ['alignment', 'first_line_indent', 'left_indent', 'line_spacing', 'page_break_before', 'right_indent', 'space_before', 'space_after']

    for paragraph_element in paragraph_elements_list:
        paragraph_element_search = f'paragraph.paragraph_format.{paragraph_element}'
        document_diagram_paragraph_format_elements.update({paragraph_element: eval(paragraph_element_search, {}, {'paragraph': paragraph})})

    runs = paragraph.runs
    for run_count, run in enumerate(runs):
        run_element_list = ['bold', 'italic', 'underline', 'font.subscript', 'font.superscript',
                            'font.highlight_color', 'font.strike', 'font.double_strike', 'font.emboss', 'font.imprint',
                            'font.outline', 'font.shadow', 'font.name', 'font.size']
        document_diagram_paragraph_entry.append([run_count, dict()])
        document_diagram_run_entry = document_diagram_paragraph_entry[run_count+1][1]
        document_diagram_run_entry.update({'text': run.text})
        for run_element in run_element_list:
            run_element_search = f'run.{run_element}'
            if eval(run_element_search, {}, {'run': run}) != None:
                document_diagram_run_entry.update({run_element: eval(run_element_search, {}, {'run': run})})

print(document_diagram[2])
