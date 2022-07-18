from docx import Document
from datetime import datetime

#Creates new dictionary to which to add template parameters
template_dict = dict()

#Create timedate string for default parameter on output file name
time_now = datetime.now()
time_stamp = time_now.strftime('%Y-%m-%d_%H%M%S')

#Main function start
def template_generator(docx_template_file,docx_output_filename='New File '+time_stamp):

#   Adds the provided template path and output file name to the template parameter dict
    template_dict.update({'template path': './'+docx_template_file,'output file name': docx_output_filename})

#   Starts a new list to hold runs to be replaced
    replacement_field_list = list()

#   Loads document from first parameter
    document = Document(docx_template_file)

#   Breaks document into paragraphs
    paragraphs = document.paragraphs

    for paragraph_count,paragraph in enumerate(paragraphs):

#       Breaks paragraphs into runs
        runs = paragraph.runs
        for run_count, run in enumerate(runs):

#       If replacement string marker is found, adds new dict entry to replacement field list with all of the run elements
            if "{{" in run.text:
                run_dict = dict()
                run_dict.update({'paragraph':paragraph_count,'run': run_count,'text': run.text})

#       Uses a list of run elements and a loop function for ease of adding or removing searched elements
                run_element_list = ['bold', 'italic', 'underline', 'font.subscript', 'font.superscript',
                                    'font.highlight_color', 'font.strike', 'font.double_strike', 'font.emboss',
                                    'font.imprint','font.outline', 'font.shadow', 'font.name', 'font.size']
                for run_element in run_element_list:
                    run_element_search = f'run.{run_element}'
                    if eval(run_element_search, {}, {'run': run}) != None:
                        run_dict.update({run_element: eval(run_element_search, {}, {'run': run})})
                replacement_field_list.append(run_dict)

#   Adds runs to be replaced to main dictionary
    template_dict.update({'update runs': replacement_field_list})
    return template_dict
