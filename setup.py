from distutils.core import setup
from Cython.Build import cythonize
import numpy
from setuptools import find_packages
from distutils.extension import Extension


extensions = [Extension("*", ["discretization/*.pyx"], language='c++')]
setup(name='discretization',
      packages=find_packages(),
      version='0.1',
      ext_modules=cythonize(extensions),
      include_dirs=[numpy.get_include()]
      )
