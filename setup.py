from setuptools import setup, find_packages

setup(
    # Package Metadata
    name='PolyRename',
    version='0.0.1',
    description='A tool for renaming large sets of files',
    url='https://github.com/agsimmons/PolyRename',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    packages=find_packages(),

    author='Andrew Simmons, Ethan Smith',
    author_email='agsimmons0@gmail.com'
)
