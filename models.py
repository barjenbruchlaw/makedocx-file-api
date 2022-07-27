from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Template(Base):
    __tablename__ = "template"
    template_id = Column(Integer,primary_key=True)
    template_path = Column(String)
    template_name = Column(String)
    output_filename = Column(String)
    update_paragraph_runs=Column(JSON)
    update_table_runs=Column(JSON)


