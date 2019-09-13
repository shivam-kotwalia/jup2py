import os
import nbconvert
from .utils import save_pyfile


def jup2py(jup_filename, py_filename=None, save=True):
    # Converting jupyter to py through nbconvertor
    py_code = nbconvert.export(nbconvert.PythonExporter(), jup_filename)
    mycode = py_code[0].split("\n")
    clean_code = []
    for index, line in enumerate(mycode):
        # Removing which are either "\n" or denotes the "Input" Tag for jupyter notebook
        if line == "\n" or (line.startswith("# In[")) or line is None or line == "":
            pass
        # Commenting the magic functions or the command line
        elif line.startswith("get_ipython()"):
            line = "#" + line
            clean_code.append(line)
        # Remove the jup2py line itself
        elif "jup2py" in line:
            pass
        else:
            clean_code.append(line)
    clean_code = "\n".join(clean_code)
    # Saving back the .py file
    if save:
        save_pyfile(clean_code, py_filename)
    else:
        return clean_code


def jup2html(jup_filename, py_filename=None, save=True):
    # Converting jupyter to html through nbconvertor
    pass
