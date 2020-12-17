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

cat_summary(df)

import dsbootcamp.prep.outlier
dir(dsbootcamp.prep.outlier)


import os
import inspect
import typing
import types


def get_all_functions(modul_path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(modul_path):
        for filename in filenames:
            if filename.endswith('.py'):
                files.append(os.sep.join([dirpath, filename]))

    for f in files:
        # turn the files into code objects and find declared constants
        functions = []
        code_obj = compile(open(f).read(), f, 'exec')
        members = dict(inspect.getmembers(code_obj))
        for idx in range(len(members['co_consts']) // 2):
            val = members['co_consts'][idx * 2]
            name = members['co_consts'][idx * 2 + 1]
            # suboptimal: this check also allows lambdas and classes
            if isinstance(val, types.CodeType):
                functions.append(name)
        print(f'{f}: {functions}')


get_all_functions("/Users/mvahit/anaconda3/envs/dsbootcamp/lib/python3.8/tkinter")


