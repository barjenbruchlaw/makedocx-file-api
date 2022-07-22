from docx import Document
from datetime import datetime
from string_to_array_dict import string2dict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Template
from database import get_templates_function
from sample_values import sample_values
from rebuild_run import rebuild_run
from find_replacement_terms import find_terms

SQLALCHEMY_DATABASE_URL = 'sqlite:///./templates.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker()
Session.configure(bind=engine,autocommit=False,autoflush=False)
session = Session()

print(get_templates_function())
print("Choose template ID number")
template_id_choice = input()

template_entry = session.query(Template).filter_by(template_id=template_id_choice).first()

raw_update_paragraph_runs = template_entry.update_paragraph_runs

update_paragraph_runs_final = string2dict(raw_update_paragraph_runs)

term_dictionary = sample_values
time_now = datetime.now()
time_stamp = time_now.strftime('%Y-%m-%d_%H%M%S')
term_dictionary.update({"{{datetimestamp}}": time_stamp})

template_doc=template_entry.template_path

template_document = Document(template_doc)

template_paragraphs = template_document.paragraphs

for template_paragraph_count,template_paragraph in enumerate(template_paragraphs):
    template_runs = template_paragraph.runs
    for template_run_count,template_run in enumerate(template_runs):
        for update_paragraph_run in update_paragraph_runs_final:
            if update_paragraph_run["paragraph"] == template_paragraph_count and update_paragraph_run["run"] == template_run_count:
                new_run = rebuild_run(update_paragraph_run,term_dictionary)
                print(type(new_run))
#                 template_run.clear()
#                 template_paragraph.add_run(new_run)
#
# output_filename_template=template_entry.output_filename
# output_filename_entry = [output_filename_template]
# output_filename_dynamic_terms = find_terms(output_filename_template)
# for output_term in output_filename_dynamic_terms:
#     new_dynamic_term = term_dictionary[output_term]
#     new_output_filename_entry=output_filename_entry[-1].replace(output_term,new_dynamic_term)
#     output_filename_entry.append(new_output_filename_entry)
#
# save_filename=output_filename_entry[-1]
#
# template_document.save(save_filename)
