from docx import Document
import sys
from pprint import pprint

docx_template_file = sys.argv[1]
docx_output_filename = sys.argv[2]

template_dict = dict()

template_dict.update({'template path': './'+docx_template_file,'output file name': docx_output_filename})

replacement_field_list = list()

document = Document(docx_template_file)

paragraphs = document.paragraphs

for paragraph_count,paragraph in enumerate(paragraphs):
    runs = paragraph.runs
    for run_count, run in enumerate(runs):
        if "{{" in run.text:
            run_dict = dict()
            run_dict.update({'paragraph':paragraph_count,'run': run_count,'text': run.text})
            run_element_list = ['bold', 'italic', 'underline', 'font.subscript', 'font.superscript',
                                'font.highlight_color', 'font.strike', 'font.double_strike', 'font.emboss',
                                'font.imprint','font.outline', 'font.shadow', 'font.name', 'font.size']
            for run_element in run_element_list:
                run_element_search = f'run.{run_element}'
                if eval(run_element_search, {}, {'run': run}) != None:
                    run_dict.update({run_element: eval(run_element_search, {}, {'run': run})})
            replacement_field_list.append(run_dict)

template_dict.update({'update runs': replacement_field_list})

pprint(template_dict)