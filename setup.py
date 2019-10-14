from setuptools import setup, find_packages
from os import path

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='better_uniform',
    version='1.0.4',
    url='https://github.com/j-faria/better_uniform.git',
    author='João Faria',
    author_email='joao.faria@astro.up.pt',
    description='A better scipy.stats.uniform',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['scipy'],
)
