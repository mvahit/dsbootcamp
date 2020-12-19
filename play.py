# Modul .py uzantılı dosyalardır.
# Package modullerin organize edildiği klasördür.

import dsbootcamp
help(dsbootcamp)

from dsbootcamp.hi import *

hello1()
hello2()
hello3()

help(dsbootcamp)


import dsbootcamp.prep
help(dsbootcamp.prep)


from dsbootcamp.prep.outlier import outlier_thresholds
help(outlier_thresholds)

import seaborn as sns
df = sns.load_dataset("titanic")
low, up = outlier_thresholds(df, "age")
print(low, up)


help(dsbootcamp.prep.outlier)

help(dsbootcamp)

import dsbootcamp.eda
help(dsbootcamp.eda)

import dsbootcamp.eda.eda
help(dsbootcamp.eda.eda)



from dsbootcamp.eda.eda import cat_summary

cat_summary(df, cat_cols)

import dsbootcamp.prep.outlier
dir(dsbootcamp.prep.outlier)



import seaborn as sns
import pandas as pd
from dsbootcamp.eda.eda import cat_summary

df = pd.read_csv("/Users/mvahit/Documents/GitHub/dsbootcamp/dsbootcamp/datasets/titanic.csv")
cat_cols = [col for col in df.columns if df[col].dtypes == 'O']
cat_summary_adv(df, cat_cols)