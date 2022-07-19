import sys
from template_generator import template_generator

template_path = sys.argv[1]
template_name = sys.argv[2]
output_file = sys.argv[3]

new_template = template_generator(template_path,template_name,output_file)

# print(new_template['template_path_field'])