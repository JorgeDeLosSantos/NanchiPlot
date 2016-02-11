# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from _const_ import *
# WX Backend ?

def set_default_params(axes,figure):
	# Figure properties
	mpl.rc('figure',autolayout=True)
	figure.set_facecolor(FIGURE_BG_COLOR)
	
	# Axes properties
	mpl.rc('axes', grid=True, facecolor=AXES_BG_COLOR, hold=False)
	set_default_axes_props(axes)
	
	# Grid properties
	mpl.rc('grid', color=GRID_COLOR)
	
	# Tick properties
	mpl.rc('xtick', color=XTICK_COLOR)
	mpl.rc('ytick', color=YTICK_COLOR)
	

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
	

	
	
