from interactions.num_num import NumNum
from interactions.num_cat import NumCat
from interactions.cat_cat import CatCat
from interactions.num_num_cat import Num2Cat
from interactions.num_cat_cat import NumCat2


class Comparator:
    def __init__(self, separ):

        self.nn = []
        for el1 in separ.numeric_list:
            for el2 in separ.numeric_list:
                if not el1 is el2:
                    inter = NumNum(el1, el2)
                    self.nn.append(inter)

        self.nc = []
        for el1 in separ.numeric_list:
            for el2 in separ.categorical_list:
                inter = NumCat(el1, el2)
                self.nc.append(inter)

        self.cc = []
        for el1 in separ.categorical_list:
            for el2 in separ.categorical_list:
                if not el1 is el2:
                    inter = CatCat(el1, el2)
                    self.cc.append(inter)

        self.n2c = []
        for el1 in separ.numeric_list:
            for el2 in separ.numeric_list:
                for el3 in separ.categorical_list:
                    if not el1 is el2:
                        inter = Num2Cat(el1, el2, el3)
                        self.n2c.append(inter)

        self.nc2 = []
        for el1 in separ.numeric_list:
            for el2 in separ.categorical_list:
                for el3 in separ.categorical_list:
                    if not el2 is el3:
                        inter = NumCat2(el1, el2, el3)
                        self.nc2.append(inter)
