import sys
from template_generator import template_generator

template_path = sys.argv[1]
output_file = sys.argv[2]

new_template = template_generator(template_path,output_file)
