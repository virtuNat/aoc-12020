from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("van_eck.pyx", annotate=True),
)
