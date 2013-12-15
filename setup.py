from distutils.core import setup
import os
import sys
from . import VERSION
sys.path.insert(0, os.path.abspath('.'))

setup(
    name='kaboom',
    version=VERSION,
    packages=[''],
    url='http://github.com/vinu76jsr/kaboom',
    license='',
    author='vaibhav',
    author_email='vinu76jsr@gmail.com',
    license='bsd3',
    description='Command line key-value store',
    install_requires=['rethinkdb'],
    entry_points={'console_scripts': [
        'kaboom = kaboom:run']}
)
