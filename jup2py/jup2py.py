import os 
import nbconvert

def jup2py(jup_filename, py_filename=None, keep_org=False):
    print("Please make sure you have saved your jupyter notebook before converting")
    if jup_filename is None:
        print("Please supply jupter filename with .ipynb extension")
    if py_filename is None:
        py_org_filename = os.path.splitext(jup_filename)[0] + "_original.py"
        py_filename = os.path.splitext(jup_filename)[0] + ".py"

    #Converting jupyter to py through nbconvertor
    py_code = nbconvert.export(nbconvert.PythonExporter(), jup_filename)
    with open(py_org_filename, "w") as myfile:
        myfile.write(py_code[0])
    
    with open(py_org_filename, "r") as myfile:
        mycode = myfile.readlines()
    mycode2 = []
    for index, line in enumerate(mycode):
        #Removing which are either "\n" or denotes the "Input" Tag for jupyter notebook
        if line == "\n" or (line.startswith("# In[")):
            pass
        # Commenting the magic functions or the command line 
        elif "get_ipython()" in line:
            line = "#" + line
            mycode2.append(line)
        # Remove the jup2py line itself
        elif "jup2py" in line:
            pass
        else:
            mycode2.append(line)
    # Saving back the .py file
    with open(py_filename, "w") as myfile:
        myfile.writelines(mycode2)
    print(f".py file {py_filename} saved!")
    if keep_org is False:
        os.remove(py_org_filename)