# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('WXAgg') # wxPython backend
import matplotlib.pyplot as plt
import matplotlib.cm as cm # Colormap
from _const_ import *

# Default style for graphs
DEFAULT_STYLE = WHITE_STYLE

if True:
    """
    Only this...
    """
    try:
        plt.style.use(DEFAULT_STYLE)
    except:
        pass # Default style
else:
    try:
        plt.style.use(DARK_STYLE)
    except:
        pass #Default style

