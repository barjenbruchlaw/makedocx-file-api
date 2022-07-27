from sample_values import sample_values
from rebuild_run import add_caps_to_dict
import pprint

old_dict = sample_values

new_dict = add_caps_to_dict(old_dict)

pprint.pprint(new_dict)
