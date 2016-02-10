# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from _const_ import *
# WX Backend ?

def set_default_params(axes,figure):
	#mpl.rcParams.update(mpl.rcParamsDefault)
	# Figure properties ====================================================
	mpl.rc('figure',autolayout=True, facecolor=FIGURE_BG_COLOR)
	# Axes properties ======================================================
	mpl.rc('axes', grid=True, facecolor=AXES_BG_COLOR, hold=False, axisbelow=True)
	axes.cla()
	axes.set_aspect("auto")
	if is_reversed_yaxis(axes):
		axes.invert_yaxis()
	axes.images = []
	if not axes.get_frame_on():
		axes.set_frame_on(True)
	axes.set_axis_on()
	
	mpl.rc('grid', color=GRID_COLOR)
	mpl.rc('xtick', color=XTICK_COLOR)
	mpl.rc('ytick', color=YTICK_COLOR)
	# Image properties
	#mpl.rc('image',aspect="equal")
	

def is_reversed_yaxis(axes):
	a,b = axes.get_ylim()
	if a > b: return True
	return False
	

	
	
