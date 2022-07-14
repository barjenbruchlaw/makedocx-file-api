from docx import Document

document = Document("Test document.docx")

paragraphs = document.paragraphs

document_diagram = list()
document_diagram.append(list())
document_diagram_style = document_diagram[0]
document_styles = document.styles
document_styles_list = list()

for style_item in document_styles:
    document_styles_list.append(style_item)

document_diagram_style.append(document_styles_list)

for paragraph_count, paragraph in enumerate(paragraphs):
    document_diagram.append([paragraph_count, list()])
    document_diagram_paragraph_entry = document_diagram[paragraph_count+1][1]
    document_diagram_paragraph_entry.append(dict())
    document_diagram_paragraph_format_elements = document_diagram_paragraph_entry[0]
    paragraph_elements_list = ['alignment', 'first_line_indent', 'left_indent', 'line_spacing', 'page_break_before', 'right_indent', 'space_before', 'space_after']

    for paragraph_element in paragraph_elements_list:
        paragraph_element_search = f'paragraph.paragraph_format.{paragraph_element}'
        document_diagram_paragraph_format_elements.update({paragraph_element: exec(paragraph_element_search)})

    runs = paragraph.runs
    for run_count, run in enumerate(runs):
        document_diagram_paragraph_entry.append([run_count, dict()])
        document_diagram_run_entry = document_diagram_paragraph_entry[run_count+1][1]
        document_diagram_run_entry.update({'text': run.text})
        document_diagram_run_entry.update({'bold': run.bold})
        document_diagram_run_entry.update({'italic': run.italic})
        document_diagram_run_entry.update({'underline': run.underline})
        document_diagram_run_entry.update({'subscript': run.font.subscript})
        document_diagram_run_entry.update({'superscript': run.font.superscript})
        document_diagram_run_entry.update({'highlight color': run.font.highlight_color})
        document_diagram_run_entry.update({'strike through': run.font.strike})
        document_diagram_run_entry.update({'double strike through': run.font.double_strike})
        document_diagram_run_entry.update({'emboss': run.font.emboss})
        document_diagram_run_entry.update({'imprint': run.font.imprint})
        document_diagram_run_entry.update({'outline': run.font.outline})
        document_diagram_run_entry.update({'shadow': run.font.shadow})
        document_diagram_run_entry.update({'font name': run.font.name})
        document_diagram_run_entry.update({'font size': run.font.size})


print(document_diagram)
