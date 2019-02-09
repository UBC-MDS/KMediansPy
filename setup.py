from setuptools import setup

setup(
    name='KMediansPy',
    version='1.0',
    author='S. Guha, A. Pearson, F. Nie, T. Pan',
    author_email='NA',
    packages=['KMediansPy'],
    url='https://github.com/UBC-MDS/KMediansPy',
    license='LICENSE.txt',
    description='K Medians Clustering Algorithm',
    long_description=open('README.txt').read(),
    install_requires=[
        "numpy = 1.15.1",
        "pytest =3.8.0",
    ],
)
