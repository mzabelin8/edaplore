import seaborn as sns
from separator.data_separator import Separator
from overview.overview_class import Overview
from jinja2 import Environment, Template
from jinja2 import Environment, FileSystemLoader

data = sns.load_dataset('titanic')

Sep = Separator(data)
Sep.separate()

print(Sep.data_classes[3].column_name)



env = Environment(loader=FileSystemLoader('/Users/maximzabelin/Programming/hse2/html_templates/test_templates'))

# Get the template from the environment
template = env.get_template('table_and_plot.html')

# Render the template with the numeric object as a variable
output = template.render(numeric=Sep.data_classes[3])


with open("/Users/maximzabelin/desktop/c.html", "w") as f:
    f.write(output)


#
# tmp_string = ''
# with open('/table_and_plot.html', 'r') as f:
#     tmp_string = f.read()
#
# tmp = Template(tmp_string)
#
# tmp_render = tmp.render(numeric=Sep.data_classes[3])
#
# with open("/Users/maximzabelin/desktop/c.html", "w") as f:
#     f.write(tmp_render)