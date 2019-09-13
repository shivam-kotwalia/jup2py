def save_pyfile(code, py_filename):
    with open(py_filename, "w") as myfile:
        myfile.writelines(code)
    print(f".py file {py_filename} saved!")


def data_cleaning():
    pass