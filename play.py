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