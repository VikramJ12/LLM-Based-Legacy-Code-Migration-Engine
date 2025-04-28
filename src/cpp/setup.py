from setuptools import setup, Extension
import pybind11

cpp_module = Extension(
    'cparser',
    sources=['parser.cpp'],
    include_dirs=[pybind11.get_include()],
    language='c++',
    extra_compile_args=['-std=c++11'],
)

setup(
    name='cparser',
    version='0.1',
    description='C Parser Module',
    ext_modules=[cpp_module],
)
