import images.make_plot as plot
from html_templates.template_loader import find_template

class GenMap:
    def render(self):
        template = find_template('genmap_template.html').render(gm=self)
        return template

    def mis_vals(self):
        df = self.data.isna()

        self.miss_heatmap = plot.heat_map_general(df.transpose())

        self.miss_barplot = plot.barplot_general(x=df.sum().index,
                                                 y=df.sum().values)

    def corr_matrix(self):
        df = self.data.corr(numeric_only=True)

        self.corr_heatmap = plot.heat_map_general(df, annot=True)

    def __init__(self, data):
        self.data = data

        self.miss_heatmap = None
        self.miss_barplot = None
        self.mis_vals()

        self.corr_heatmap = None
        self.corr_matrix()

        self.rendered = self.render()


