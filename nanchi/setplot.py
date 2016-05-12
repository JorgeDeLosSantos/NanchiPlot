# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from _const_ import *
# WX Backend ?

def set_default_params(axes,figure):
    # Figure properties
    #~ axes.cla()
    #~ mpl.rc('figure',autolayout=True)
    set_default_axes_props(axes)
    

def set_default_axes_props(axes):
    axes.cla()
    axes.set_aspect("auto")
    if is_reversed_yaxis(axes):
        axes.invert_yaxis()
    if not axes.get_frame_on():
        axes.set_frame_on(True)


def is_reversed_yaxis(axes):
    """
    """
    a,b = axes.get_ylim()
    if a > b: return True
    return False
    

    
    
