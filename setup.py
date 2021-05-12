from setuptools import setup

setup(
    name='python-image-search',
    version="1.0",
    url='https://github.com/RandomPythonProgrammer/python-image-search',
    author='RandomPythonProgramer',
    author_email="jhc3628@gmail.com",
    description='Simple image search',
    install_requires=['selenium', 'bs4', 'requests'],
    keywords="Image Search",
    scripts=["Image_Search.py"]
)
