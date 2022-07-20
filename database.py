from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Template

SQLALCHEMY_DATABASE_URL = 'sqlite:///./templates.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker()
Session.configure(bind=engine,autocommit=False,autoflush=False)
session = Session()

def add_new_template_function(new_template_submission):
    new_template = Template(
        template_path=new_template_submission['template_path_field'],
        template_name=new_template_submission['template_name_field'],
        output_filename=new_template_submission['output_filename_field'],
        # update_runs should NOT be formatted as a string in the final format for PostGreSQL -- this is for SQLite testing only
        update_paragraph_runs=str(new_template_submission['update_paragraph_runs_field']),
        update_table_runs=str(new_template_submission['update_table_runs_field']),
    )
    session.add(new_template)
    session.commit()

def get_templates_function():
    result = session.query(Template).all()
    for row in result:
        print(f'Template #:{row.template_id}, name:{row.template_name}')
