import sys
import argparse
import os
from pathlib import Path

from .orchestrator import topy, bach_conversion


# *********GLOBAL CONFIG **************
name = "jup2py"
__description__ = "Jup2Py :- Simple way to convert your Jupyter Notebook to .py"
__version__ = "0.1.dev1"
__all__ = [topy, __description__, bach_conversion]
# *************************************


print(__description__)
# print("Please make sure that you have saved the Notebook before running Jup2Py")


def main(argv):
    # handling argparse
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("-v",
                        "--version",
                        help="Jup2Py Version",
                        action="store_true")
    parser.add_argument("-i",
                        "--input",
                        help="""
                        Input Jupyter Notebook to be converted to .py file
                        Can also take folder name, for bulk transfer but should be used with -r option
                        """,
                        type=str)
    parser.add_argument("-o",
                        "--output",
                        help="[Optional]: Output python file name and location",
                        type=str)
    parser.add_argument("-r",
                        "--recursive",
                        help="Used with ",
                        action="store_true")
    args = parser.parse_args(argv[1:])
    if args.version:
        print(f"Jup2Py {__version__}")
        return 0

    if args.input:
        topy(ipynb_file=args.input, py_filename=args.output)
    elif args.recursive and os.path.isdir(args.input):
        bach_conversion(ipynb_folder=args.input, py_folder=args.output)
    else:
        print(
            """
            Please enter input jupyter notebook path with -i/--input flag
            or 
            pass folder name in -i/--input flag with -r/--recursive flag
            """
        )
        return 0


def run_main():
    try:
        sys.exit(main(sys.argv))
    except Exception as e:
        print("Something went wrong - ", end=" ")
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    run_main()
