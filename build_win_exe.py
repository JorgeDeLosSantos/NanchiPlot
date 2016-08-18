# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe, sys, os
import matplotlib
import numpy
import glob

sys.argv.append('py2exe')

STYLES = [("styles", [k]) for k in glob.glob("nanchi\\styles\\*")]
IMAGES = [("img", [k]) for k in glob.glob("nanchi\\img\\*")]
HELP = [("help", [k]) for k in glob.glob("nanchi\\help\\*")]
DATA = [("data", [k]) for k in glob.glob("nanchi\\data\\*")]

setup( 
    options = {         
    'py2exe' : {
        'compressed': 1, 
        'optimize': 2,
        'bundle_files': 3, #Options 1 & 2 do not work on a 64bit system
        'dist_dir': 'dist',  # Put .exe in dist/
        'xref': False,
        'skip_archive': False,
        'ascii': False,
        'includes' :  ['matplotlib','numpy','nanchi'],
        'dll_excludes': ['MSVCP90.dll', 'w9xpopen.exe', 'Qwt.pyd', 'tcl85.dll', 'tk85.dll', 'MSVCR90.DLL',
                     'libgdk-win32-2.0-0.dll',
                     'libgobject-2.0-0.dll',
                     'libgdk_pixbuf-2.0-0.dll',
                     'libgtk-win32-2.0-0.dll',
                     'libglib-2.0-0.dll',
                     'libcairo-2.dll',
                     'libpango-1.0-0.dll',
                     'libpangowin32-1.0-0.dll',
                     'libpangocairo-1.0-0.dll',
                     'libglade-2.0-0.dll',
                     'libgmodule-2.0-0.dll',
                     'libgthread-2.0-0.dll',
                     'QtGui4.dll', 'QtCore.dll',
                     'QtCore4.dll'
                        ],
        }
        },                   
    zipfile=None, 
    windows = [{
        "script": "nanchi/app.py",
        "dest_base": "NanchiPlot", #"icon_resources": [(1, "icons/icon.ico")], #"other_resources": [(24, 1, MANIFEST)],
        "icon_resources": [(1, "nanchi.ico")],
        }],
    data_files=matplotlib.get_py2exe_datafiles()+STYLES+IMAGES+HELP+DATA,
)