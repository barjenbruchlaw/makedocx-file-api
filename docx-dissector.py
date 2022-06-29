from docx import Document

document = Document("message-template.docx")

paragraphs = document.paragraphs

new_line = "Name: Fred"

paragraphs[0].clear()
    
paragraphs[0].add_run(text=new_line)

document.save('new-message.docx')