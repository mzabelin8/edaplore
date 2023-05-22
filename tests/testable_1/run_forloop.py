import seaborn as sns
from types_clases import type_numeric, type_boolean, type_categorical
from separator.combine import Combiner
import images.make_plot as plot
from jinja2 import Environment, Template, FileSystemLoader

df = sns.load_dataset('titanic')

plots = []

N1 = type_numeric.Numeric(df.age, 'age')
N2 = type_numeric.Numeric(df.fare, 'fare')

C = type_categorical.Categorical(df['class'], 'class')
E = type_categorical.Categorical(df['embarked'], 'em')
S = type_boolean.Boolean(df['survived'], 'survivded')

# comb = Combiner(x=N1, y=N2)

# scatter hue
comb = Combiner(x=N1, y=N2, hue=C)
image = plot.scatter_plot(comb)
plots.append(image)

# scatter
comb = Combiner(x=N1, y=N2)
image = plot.scatter_plot(comb)
plots.append(image)

# line
comb = Combiner(x=N1, y=N2)
image = plot.line_plot(comb)
plots.append(image)

# line hue
comb = Combiner(x=N1, y=N2, hue=C)
image = plot.line_plot(comb)
plots.append(image)

# pair
comb = Combiner(x=N1, y=N2)
image = plot.pair_plot(comb)
plots.append(image)

# pair hue
comb = Combiner(x=N1, y=N2, hue=C)
image = plot.pair_plot(comb)
plots.append(image)

# joint
comb = Combiner(x=N1, y=N2)
image = plot.joint_plot(comb)
plots.append(image)

# joint hue
comb = Combiner(x=N1, y=N2, hue=C)
image = plot.joint_plot(comb)
plots.append(image)

# kde
comb = Combiner(x=N1, y=N2)
image = plot.kde_plot(comb)
plots.append(image)

# kde hue
comb = Combiner(x=N1, y=N2, hue=C)
image = plot.kde_plot(comb)
plots.append(image)

# box
comb = Combiner(x=C, y=N2)
image = plot.box_plot(comb)
plots.append(image)

# box hue
comb = Combiner(x=C, y=N2, hue=S)
image = plot.box_plot(comb)
plots.append(image)

# violin
comb = Combiner(x=C, y=N2)
image = plot.violin_plot(comb)
plots.append(image)

# violin hue
comb = Combiner(x=C, y=N2, hue=S)
image = plot.violin_plot(comb)
plots.append(image)

# bar
comb = Combiner(x=C, y=N2)
image = plot.bar_plot(comb)
plots.append(image)

# bar hue
comb = Combiner(x=C, y=N2, hue=S)
image = plot.bar_plot(comb)
plots.append(image)


# heat map
comb = Combiner(x=C, y=N2, hue=S)
image = plot.heat_map(comb)
plots.append(image)

# strip plot
comb = Combiner(x=C, y=N2)
image = plot.strip_plot(comb)
plots.append(image)

# strip plot hue
comb = Combiner(x=C, y=N2, hue=S)
image = plot.strip_plot(comb)
plots.append(image)

# cat plot
comb = Combiner(x=C, y=E, hue=S)
image = plot.cat_plot(comb)
plots.append(image)


# comb = Combiner(x=C, y=N2)
# comb = Combiner(x=C, y=N2, hue=S)
# comb = Combiner(x=C, hue=S)
# comb = Combiner(x=C, y=E, hue=S)

# image = plot.cat_plot(comb)


env = Environment(loader=FileSystemLoader('.'))
t = env.get_template('temp_forloop.html').render(plot_names=plots)

with open('/Users/maximzabelin/desktop/loops_plots.html', 'w') as f:
    f.write(t)
