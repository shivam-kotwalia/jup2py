from .core import jup2py
from pathlib import Path
from tqdm.auto import tqdm


def topy(ipynb_file, py_filename):
    # print(
    #     "Please make sure you have saved your jupyter notebook before converting"
    # )
    if ipynb_file is None or not ipynb_file.endswith(".ipynb"):
        print("Please supply jupyter filename with .ipynb extension")
    if py_filename is None:
        py_filename = Path(ipynb_file).stem + ".py"
    elif Path(py_filename).is_dir():
        py_filename = Path(py_filename).joinpath(Path(ipynb_file).stem + ".py")
    elif Path(py_filename).is_file():
        pass
    jup2py(jup_filename=ipynb_file, py_filename=py_filename)


def bach_conversion(ipynb_folder, py_folder):
    if Path(py_folder).is_dir():
        pass
    else:
        py_folder = Path(py_folder).parent
    for ipynb_file in tqdm(Path(ipynb_folder).glob("*.ipynb")):
        topy(ipynb_file, py_folder)
