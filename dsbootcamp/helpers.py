import inspect
import os
import types

def get_all_functions(modul_path):
    """
    get_all_functions("/Users/mvahit/anaconda3/envs/dsbootcamp/lib/python3.8/tkinter")

    """
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