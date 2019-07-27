from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='PolyRename',
    version='1.0.1',
    license='GPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    author='Andrew Simmons, Ethan Smith',
    author_email='agsimmons0@gmail.com',
    description='A cross-platform, bulk-file rename tool',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/agsimmons/PolyRename',
    project_urls={
        'Documentation': 'https://polyrename.readthedocs.io/',
        'Bug Tracker': 'https://github.com/agsimmons/PolyRename/issues/',
    },

    packages=find_packages(),
    include_package_data=True,
    package_data={
        'gui': ['images/*.png']
    },
    zip_safe=False,

    entry_points={
        'console_scripts': ['polyrename=polyrename.__main__:main']
    },

    install_requires=[
        'PySide2>=5.11.0',
        'mediafile>=0.2.0',
    ]
)
