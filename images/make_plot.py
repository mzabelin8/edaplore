import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from jinja2 import Environment, Template, FileSystemLoader
from copy import copy


def plt_formatter(figure_size=(10, 6),
                  x_label='x_label',
                  y_label='y_label'):
    plt.figure(figsize=figure_size)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


def save_plot(plot_format='png'):
    img = BytesIO()
    plt.savefig(img, format=plot_format)
    img.seek(0)
    result = base64.b64encode(img.read()).decode('utf-8')
    return result


# def image_render(image):
#     path_to_template = './html_templates'
#     env = Environment(loader=FileSystemLoader(path_to_template))
#     rendered = env.get_template('template_for_image_.html').render(plot=image)
#     return rendered


def dis_plot(data,
             figure_size=(10, 6),
             plot_format='png',
             x_label='x_label',
             y_label='y_label'):
    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)

    sns.displot(data)

    return save_plot()


def count_plot(data,
               figure_size=(10, 6),
               plot_format='png',
               x_label='x_label',
               y_label='y_label'):
    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)

    sns.displot(data)

    return save_plot()


def count_plot_combiner(combiner,
                        figure_size=(10, 6),
                        plot_format='png',
                        x_label='x_label',
                        y_label='y_label'):
    # only for x and hue
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)

    args = combiner.args.copy()

    sns.countplot(**args)

    return save_plot()


def cat_plot(combiner,
             figure_size=(10, 6),
             plot_format='png',
             x_label='x_label',
             y_label='y_label'):
    # only for 3 categorical
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)

    args = {}
    args['data'] = combiner.data_frame
    args['x'] = combiner.x
    args['hue'] = combiner.hue
    args['col'] = combiner.y
    args['kind'] = 'count'

    sns.catplot(**args)

    return save_plot()


def scatter_plot(combiner,
                 figure_size=(10, 6),
                 plot_format='png',
                 x_label='x_label',
                 y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)
    args = combiner.args.copy()
    sns.scatterplot(**args)

    return save_plot()


def line_plot(combiner,
              figure_size=(10, 6),
              plot_format='png',
              x_label='x_label',
              y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)
    args = combiner.args.copy()
    sns.lineplot(**args)

    return save_plot()


def pair_plot(combiner,
              figure_size=(16, 9),
              plot_format='png',
              x_label='x_label',
              y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)

    if combiner.hue:
        sns.pairplot(data=combiner.data_frame,
                     vars=[combiner.x, combiner.y], hue=combiner.hue)
    else:
        sns.pairplot(data=combiner.data_frame,
                     vars=[combiner.x, combiner.y])

    return save_plot()


def joint_plot(combiner,
               figure_size=(10, 6),
               plot_format='png',
               x_label='x_label',
               y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)
    args = combiner.args.copy()

    if combiner.hue:
        args['kind'] = 'scatter'
    else:
        args['kind'] = 'hex'

    sns.jointplot(**args)

    return save_plot()


def kde_plot(combiner,
             figure_size=(10, 6),
             plot_format='png',
             x_label='x_label',
             y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)
    args = combiner.args.copy()
    if combiner.hue:
        args['fill'] = False
    else:
        args['fill'] = True

    sns.kdeplot(**args)

    return save_plot()


def box_plot(combiner,
             figure_size=(10, 6),
             plot_format='png',
             x_label='x_label',
             y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)
    args = combiner.args.copy()
    sns.boxplot(**args)

    return save_plot()


def bar_plot(combiner,
             figure_size=(10, 6),
             plot_format='png',
             x_label='x_label',
             y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)
    args = combiner.args.copy()
    sns.barplot(**args)

    return save_plot()


def violin_plot(combiner,
                figure_size=(10, 6),
                plot_format='png',
                x_label='x_label',
                y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)
    args = combiner.args.copy()
    sns.violinplot(**args)

    return save_plot()


def strip_plot(combiner,
               figure_size=(10, 6),
               plot_format='png',
               x_label='x_label',
               y_label='y_label'):
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)
    args = combiner.args.copy()
    sns.stripplot(**args)

    return save_plot()


def heat_map_general(data, colormap="YlGnBu",
                     annot=False,
                     figure_size=(10, 6),
                     plot_format='png',
                     x_label='x_label',
                     y_label='y_label'):
    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)

    sns.heatmap(data, cmap=colormap, annot=annot)

    return save_plot()


def barplot_general(x, y,
                    figure_size=(10, 6),
                    plot_format='png',
                    x_label='x_label',
                    y_label='y_label',
                    palette="YlGnBu"):
    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)

    sns.barplot(x=x, y=y, palette=palette)

    return save_plot()


def heat_map(combiner,
             figure_size=(10, 6),
             plot_format='png',
             x_label='x_label',
             y_label='y_label'):
    # only with hue option
    if x_label == 'x_label' and combiner.x:
        x_label = combiner.x

    if y_label == 'y_label' and combiner.y:
        y_label = combiner.y

    plt_formatter(figure_size=figure_size,
                  x_label=x_label,
                  y_label=y_label)

    args = {}
    args['index'] = combiner.x
    args['columns'] = combiner.hue
    args['values'] = combiner.y
    args['aggfunc'] = 'count'

    pivot_table = combiner.data_frame.pivot_table(**args)
    sns.heatmap(pivot_table, annot=True, cmap='Blues', fmt='g')

    return save_plot()
