from docx import Document

document = Document("Judgment - Jackson County.docx")

paragraphs = document.paragraphs

document_diagram = list()

for paragraph_count, paragraph in enumerate(paragraphs):
    document_diagram.append([paragraph_count, list()])
    document_diagram_paragraph_entry = document_diagram[paragraph_count][1]
    runs = paragraph.runs
    for run_count, run in enumerate(runs):
        document_diagram_paragraph_entry.append([run_count, dict()])
        document_diagram_run_entry = document_diagram_paragraph_entry[run_count][1]
        document_diagram_run_entry.update({'text': run.text})
print(document_diagram[2])