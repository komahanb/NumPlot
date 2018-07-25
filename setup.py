from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='numplot',
    version='0.0.1',
    description='NumPlot package for easy plotting of numerical data',
    long_description=readme,
    author='Komahan Boopathy',
    author_email='komahan.cool@gmail.com',
    url='https://github.com/komahanb/NumPlot',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

