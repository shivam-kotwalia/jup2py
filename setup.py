from setuptools import setup, find_packages

setup(name='jup2py',
      version='0.1',
      description='Convert jupyter notebook to .py file',
      long_description=
      'Simplest way to convert jupyter notebook to production ready .py file',
      url='https://github.com/shivam-kotwalia/jup2py',
      classifiers=[
          'Development Status :: 1 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Jupyter Notebook :: Python Files',
      ],
      keywords='Convert jupyter notebook to .py',
      author='Shivam Kotwalia',
      author_email='shivamkotwalia@gmail.com',
      license='MIT',
      install_requires=["nbconvert==5.5.0"],
      python_requires=">3.6,!=3.3.*",
      # packages=['jup2py'],
      packages=find_packages(exclude=("tests", "docs", "static")),
      zip_safe=False,
      entry_points={
          'console_scripts': ['jup2py = jup2py:run_main'],
      },
      include_package_data=True,
      )
