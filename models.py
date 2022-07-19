from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Template(Base):
    __tablename__ = "template"
    template_id = Column(Integer,primary_key=True)
    template_path = Column(String)
    template_name = Column(String)
    output_filename = Column(String)
    update_runs=Column(String)

