# -*- coding: utf-8 -*-
import site
import os.path
import glob
from setuptools import setup, find_packages

MODULE_NAME = "nanchi"

#IMAGES_DIR = 'img'
#HELP_DIR = 'help'

GET_IMAGES = glob.glob(os.path.join(MODULE_NAME,"img/*.png"))
GET_IMAGES = [k.replace("nanchi\\","") for k in GET_IMAGES]
GET_DATA_SAMPLES = glob.glob(os.path.join(MODULE_NAME,"data/*.*"))
GET_DATA_SAMPLES = [k.replace("nanchi\\","") for k in GET_DATA_SAMPLES]

PACK_DATA = GET_IMAGES + ['help/about.html', 'help/nanchi_logo.png'] + GET_DATA_SAMPLES

setup(
    name= MODULE_NAME,
    version='0.1.0',
    description='Plotting with wxPython, NumPy and Matplotlib',
    author='Pedro Jorge De Los Santos',
    author_email='delossantosmfq@gmail.com',
    license = "MIT",
    keywords=["Plotting"],
    install_requires=["matplotlib","numpy"], # Also required wxPython
    url='https://github.com/JorgeDeLosSantos/NanchiPlot',
    packages=find_packages(),
    scripts = ['nanchi_script.py','nanchi.bat'],
    package_data={"nanchi": PACK_DATA}
)
