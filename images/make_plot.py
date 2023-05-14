import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO


class MakePlot:
    def __init__(self):
        self.figure_size = (10, 6)
        self.png_format = 'png'

    def sns_dis_plot(self, data):
        plt.figure(figsize=self.figure_size)

        sns.displot(data)
        img = BytesIO()
        plt.savefig(img, format=self.png_format)
        img.seek(0)
        result = base64.b64encode(img.read()).decode('utf-8')
        return result

    def sns_count_plot(self, data):
        plt.figure(figsize=(5, 3))

        sns.countplot(x=data)
        img = BytesIO()
        plt.savefig(img, format=self.png_format)
        img.seek(0)
        result = base64.b64encode(img.read()).decode('utf-8')
        return result
