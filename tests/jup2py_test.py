#!/usr/bin/env python# coding: utf-8import osimport nbconvert#get_ipython().run_line_magic('load_ext', 'autoreload')#get_ipython().run_line_magic('autoreload', '2')    if jup_filename is None or not jup_filename.endswith(".ipynb"):        print("Please supply jupter filename with .ipynb extension")    if py_filename is None:        py_org_filename = os.path.splitext(jup_filename)[0] + "_original.py"        py_filename = os.path.splitext(jup_filename)[0] + ".py"    # Converting jupyter to py through nbconvertor    py_code = nbconvert.export(nbconvert.PythonExporter(), jup_filename)    mycode = py_code[0].split("\n")    clean_code = []    for index, line in enumerate(mycode):        # Removing which are either "\n" or denotes the "Input" Tag for jupyter notebook        if line == "\n" or (line.startswith("# In[")) or line is None or line=="":            pass        # Commenting the magic functions or the command line#        elif "get_ipython()" in line:            line = "#" + line            clean_code.append(line)            pass        else:            clean_code.append(line)    return clean_code    # Saving back the .py file#     with open(py_filename, "w") as myfile:#         myfile.writelines(mycode2)#     print(f".py file {py_filename} saved!")#     if keep_org is False:#         os.remove(py_org_filename)aa.split("\n")bprint(c)