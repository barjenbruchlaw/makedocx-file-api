from database import add_new_template_function
from template_generator import template_generator

print("Enter template file name:")
template_path = input()
print("Enter template name:")
template_name = input()
print("Enter template output name:")
output_filename = input()

new_template = template_generator(template_path,template_name,output_filename)

# print(new_template)

add_new_template_function(new_template)

