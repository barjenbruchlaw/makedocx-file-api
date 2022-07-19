from pydantic import BaseModel
from pydantic.typing import List, Dict

class Template(BaseModel):
    template_id = int
    template_path = str
    template_name = str
    output_filename = str
    update_runs = list[dict]
