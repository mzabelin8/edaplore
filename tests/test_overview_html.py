import seaborn as sns
from separator.data_separator import Separator
from overview.overview_class import Overview
from jinja2 import Environment, Template


data = sns.load_dataset('titanic')

Sep = Separator(data)
Sep.separate()

Ov = Overview(Sep.data_classes)

tmp_string = ''
with open('/Users/maximzabelin/Programming/hse2/html_templates/overview_1.html', 'r') as f:
    tmp_string = f.read()

tmp = Template(tmp_string)

tmp_render = tmp.render(overview=Ov)

with open("/Users/maximzabelin/desktop/a.html", "w") as f:
    f.write(tmp_render)

