import seaborn as sns
from types_clases import type_numeric, type_boolean, type_categorical
from separator.combine import Combiner
import images.make_plot as plot
from jinja2 import Environment, Template, FileSystemLoader

df = sns.load_dataset('titanic')

N1 = type_numeric.Numeric(df.age, 'age')
N2 = type_numeric.Numeric(df.fare, 'fare')

C = type_categorical.Categorical(df['class'], 'class')
E = type_categorical.Categorical(df['embarked'], 'em')
S = type_boolean.Boolean(df['survived'], 'survivded')

# comb = Combiner(x=N1, y=N2)
# comb = Combiner(x=N1, y=N2, hue=C)

# comb = Combiner(x=C, y=N2)
comb = Combiner(x=C, y=N2)
# comb = Combiner(x=C, hue=S)
# comb = Combiner(x=C, y=E, hue=S)

image = plot.strip_plot(comb)



env = Environment(loader=FileSystemLoader('.'))
t = env.get_template('temp.html').render(plot=image)

with open('/Users/maximzabelin/desktop/interactions.html', 'w') as f:
    f.write(t)
