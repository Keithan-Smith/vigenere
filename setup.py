from setuptools import setup, find_packages

setup(
    name='vigenere',
    version='0.0.3',
    author='Keithan Smith',
    author_email='kjs20@ic.ac.uk',
    description='A Python implementation of the Vigenère cipher.',  # Short description
    long_description=open('README.md').read(),  # Long description read from the README file
    long_description_content_type='text/markdown',  # Type of the long description
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=[],
    python_requires='>=3.6'
)

