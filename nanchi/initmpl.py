# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('WXAgg') # wxPython backend
import matplotlib.pyplot as plt
import matplotlib.cm as cm # Colormap

if True:
    """
    Only this...
    """
    plt.style.use(r'styles/white.mplstyle')
else:
    plt.style.use(r'styles/dark.mplstyle')

