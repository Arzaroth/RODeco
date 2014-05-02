#!/usr/bin/env python
import setuptools


setuptools.setup(
    name='RODeco',
    version='1.0',
    license='GPLv3',
    url='https://github.com/Arzaroth/RODeco',
    download_url='https://github.com/Arzaroth/RODeco/tarball/1.0',
    author='Lucas Philippe, Marc-Etienne Barrut',
    author_email='lu.k.philippe@gmail.com, me.barrut@gmail.com',
    description='RODeco a read only function decorator',
    packages=['RODeco'],
    long_description=open('README').read(),
)
