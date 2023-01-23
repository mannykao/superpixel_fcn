from distutils.core import setup
import os

requirements = ["Cython","numpy"]
for requirement in requirements:
  os.system(f"pip install {requirement}")

from Cython.Build import cythonize
import numpy

setup(
  name = 'Connectivity',
  install_requires = requirements,
  ext_modules = cythonize("connectivity.pyx"),
  include_dirs=[numpy.get_include()],
)

