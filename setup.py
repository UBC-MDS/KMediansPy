from setuptools import setup

setup(
    name='KMediansPy',
    version='0.1',
    author='S. Guha, A. Pearson, F. Nie, T. Pan',
    packages=['kmedians'],
    url='https://github.com/UBC-MDS/KMediansPy',
    license='LICENSE.txt',
    description='K Medians Clustering Algorithm and table summary',
    long_description=open('README.md').read(),
    install_requires=[
        'numpy>=1.15.1',
        'pandas>=0.23.4']
)
