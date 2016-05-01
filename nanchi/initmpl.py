# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('WXAgg') # wxPython backend
import matplotlib.pyplot as plt
import matplotlib.cm as cm # Colormap
from _const_ import *


DEFAULT_STYLE = DARK_STYLE

if True:
    """
    Only this...
    """
    plt.style.use(DEFAULT_STYLE)
else:
    plt.style.use(DARK_STYLE)

