from docx import Document

document = Document("Judgment - Jackson County.docx")

paragraphs = document.paragraphs

document_diagram = list()

for paragraph_count, paragraph in enumerate(paragraphs):
    document_diagram.append([paragraph_count, list()])
    document_diagram_paragraph_entry = document_diagram[paragraph_count][1]
    document_diagram_paragraph_entry.append(dict())
    document_diagram_paragraph_format_elements = document_diagram_paragraph_entry[0]
    document_diagram_paragraph_format_elements.update({'alignment': paragraph.paragraph_format.alignment})
    document_diagram_paragraph_format_elements.update({'first line indent': paragraph.paragraph_format.first_line_indent})
    document_diagram_paragraph_format_elements.update({'left indent': paragraph.paragraph_format.left_indent})
    document_diagram_paragraph_format_elements.update({'line spacing': paragraph.paragraph_format.line_spacing})
    document_diagram_paragraph_format_elements.update({'line spacing rule': paragraph.paragraph_format.line_spacing_rule})
    document_diagram_paragraph_format_elements.update({'page break before': paragraph.paragraph_format.page_break_before})
    document_diagram_paragraph_format_elements.update({'right indent': paragraph.paragraph_format.right_indent})
    document_diagram_paragraph_format_elements.update({'space before': paragraph.paragraph_format.space_before})
    document_diagram_paragraph_format_elements.update({'space after': paragraph.paragraph_format.space_after})
    runs = paragraph.runs
    for run_count, run in enumerate(runs):
        document_diagram_paragraph_entry.append([run_count, dict()])
        document_diagram_run_entry = document_diagram_paragraph_entry[run_count+1][1]
        document_diagram_run_entry.update({'text': run.text})
        document_diagram_run_entry.update({'bold': run.bold})
        document_diagram_run_entry.update({'italic': run.italic})
        document_diagram_run_entry.update({'underline': run.underline})
        document_diagram_run_entry.update({'font name': run.font.name})
        document_diagram_run_entry.update({'font size': run.font.size})

print(document_diagram[2])