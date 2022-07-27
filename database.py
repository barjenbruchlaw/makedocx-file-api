from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Barton1993!@localhost:5432/templates'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sessionmaker()
Session.configure(bind=engine,autocommit=False,autoflush=False)
session = Session()
Base = declarative_base()

class Template(Base):
    __tablename__ = "template"
    template_id = Column(Integer,primary_key=True)
    template_path = Column(String)
    template_name = Column(String)
    output_filename = Column(String)
    update_paragraph_runs=Column(JSONB)
    update_table_runs=Column(JSONB)

Base.metadata.create_all(engine)

def add_new_template_function(new_template_submission):
    new_template = Template(
        template_path=new_template_submission['template_path_field'],
        template_name=new_template_submission['template_name_field'],
        output_filename=new_template_submission['output_filename_field'],
        # update_runs should NOT be formatted as a string in the final format for PostGreSQL -- this is for SQLite testing only
        update_paragraph_runs=new_template_submission['update_paragraph_runs_field'],
        update_table_runs=new_template_submission['update_table_runs_field']
    )
    session.add(new_template)
    session.commit()

def get_templates_function():
    result = session.query(Template).all()
    for row in result:
        print(f'Template #:{row.template_id}, name:{row.template_name}')
