import pandas as pd


class Combiner:
    def __init__(self, x=None, y=None, hue=None):
        if x:
            self.x = x.column_name
        else:
            self.x = None

        if y:
            self.y = y.column_name
        else:
            self.y = None

        if hue:
            self.hue = hue.column_name
        else:
            self.hue = None

        container = {}
        for el in [x, y, hue]:
            if el:
                container[el.column_name] = el.data
        self.data_frame = pd.DataFrame(container)

        self.args = {'data': self.data_frame}
        if self.x:
            self.args['x'] = self.x
        if self.y:
            self.args['y'] = self.y
        if self.hue:
            self.args['hue'] = self.hue

