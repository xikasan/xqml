# coding: utf-8

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='xqml',
    version='0.0.0',
    description="Quantum machine learning utils",
    long_description=readme,
    author='xikasan',
    # author_email='',
    url='https://github.com/xikasan/xqml',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=reqs
)
