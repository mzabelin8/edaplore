import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from jinja2 import Environment, Template, FileSystemLoader
import time

from separator.data_separator import Separator
from overview.overview_class import Overview

from interactions.num_num import NumNum
from interactions.num_cat import NumCat
from interactions.cat_cat import CatCat
from interactions.num_num_cat import Num2Cat
from interactions.num_cat_cat import NumCat2

full_time = time.time()

start_time = time.time()

df = sns.load_dataset('titanic')

separ = Separator(data=df)

nn = []

for el1 in separ.numeric_list:
    for el2 in separ.numeric_list:
        if not el1 is el2:
            inter = NumNum(el1, el2)
            nn.append(inter)

print(f'nn is {time.time() - start_time}')
start_time = time.time()

nc = []
for el1 in separ.numeric_list:
    for el2 in separ.categorical_list:
        inter = NumCat(el1, el2)
        nc.append(inter)
print(f'nc is {time.time() - start_time}')
start_time = time.time()

cc = []
for el1 in separ.categorical_list:
    for el2 in separ.categorical_list:
        if not el1 is el2:
            inter = CatCat(el1, el2)
            cc.append(inter)
print(f'cc is {time.time() - start_time}')
start_time = time.time()

n2c = []
for el1 in separ.numeric_list:
    for el2 in separ.numeric_list:
        for el3 in separ.categorical_list:
            if not el1 is el2:
                inter = Num2Cat(el1, el2, el3)
                n2c.append(inter)

print(f'n2c is {time.time() - start_time}')
start_time = time.time()

nc2 = []
for el1 in separ.numeric_list:
    for el2 in separ.categorical_list:
        for el3 in separ.categorical_list:
            if not el2 is el3:
                inter = NumCat2(el1, el2, el3)
                nc2.append(inter)

print(f'nc2 is {time.time() - start_time}')
start_time = time.time()



env = Environment(loader=FileSystemLoader('/Users/maximzabelin/Programming/hse2/html_templates'))
t = env.get_template('interaction_main.html').render(NN=nn, NC=nc, CC=cc, N2C=n2c, NC2=nc2)

with open('/Users/maximzabelin/desktop/in_ter.html', 'w') as f:
    f.write(t)


print(f'full time is {time.time() - full_time}')
