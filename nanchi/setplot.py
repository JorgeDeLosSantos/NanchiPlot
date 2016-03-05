# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from _const_ import *
# WX Backend ?

def set_default_params(axes,figure):
    # Figure properties
    axes.cla()
    mpl.rc('figure',autolayout=True)
    figure.set_facecolor(FIGURE_BG_COLOR)
    
    # Tick properties
    mpl.rc('xtick', color=XTICK_COLOR, labelsize=TICK_LABEL_SIZE)
    mpl.rc('ytick', color=YTICK_COLOR, labelsize=TICK_LABEL_SIZE)
    
    # Axes properties
    mpl.rc('axes', grid=True, facecolor=AXES_BG_COLOR, hold=False)
    
    # Grid properties
    mpl.rc('grid', color=GRID_COLOR)
    
    set_default_axes_props(axes)
    

def set_default_axes_props(axes):
    axes.cla()
    axes.set_aspect("auto")
    if is_reversed_yaxis(axes):
        axes.invert_yaxis()
    if not axes.get_frame_on():
        axes.set_frame_on(True)
    axes.set_axis_bgcolor(AXES_BG_COLOR)



def is_reversed_yaxis(axes):
    a,b = axes.get_ylim()
    if a > b: return True
    return False
    

    
    
