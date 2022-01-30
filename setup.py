from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as file:
    long_description = file.read()

setup(name='end2end',
      version='1.0.2',
      description='Python end two end encryption designed for socket',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Julian Wandhoven',
      author_email='jwandhoven@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(include=['end2end']),
      license="MIT",
      install_requires = [
          "rsa"
      ]
     )