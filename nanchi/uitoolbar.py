# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import wx
import wx.html as html
import wx.grid as wxgrid
import  wx.lib.floatbar as wxfb
import webbrowser
import uibase as ui
import iodata as io
from _const_ import *
from util import isempty


class MainToolbar(wx.ToolBar):
    def __init__(self,parent,**kwargs):
        wx.ToolBar.__init__(self,parent=parent,**kwargs)
        tbsize = (32,32)
        self.SetToolBitmapSize(tbsize)
        self.SetBackgroundColour("#ffffff")
        
        # Bitmaps
        import_bmp = wx.Bitmap(PATH_IMPORT_ICON)
        function_bmp = wx.Bitmap(PATH_FUNCTION_ICON)
        bivariable_function_bmp = wx.Bitmap(PATH_BIVARIABLE_FUNCTION_ICON)
        load_image_bmp = wx.Bitmap(PATH_LOAD_IMAGE_ICON)
        
        plot_bmp = wx.Bitmap(PATH_PLOT_ICON)
        #~ polar_bmp = wx.Bitmap(PATH_POLAR_ICON)
        bar_bmp = wx.Bitmap(PATH_BAR_ICON)
        scatter_bmp = wx.Bitmap(PATH_SCATTER_ICON)
        pie_bmp = wx.Bitmap(PATH_PIE_ICON)
        image_bmp = wx.Bitmap(PATH_IMAGE_ICON)
        contour_bmp = wx.Bitmap(PATH_CONTOUR_ICON)
        contourf_bmp = wx.Bitmap(PATH_CONTOURF_ICON)
        
        #~ zoom_box_bmp = wx.Bitmap(PATH_ZOOM_BOX_ICON)
        #~ reset_view_bmp = wx.Bitmap(PATH_RESET_VIEW_ICON)
        
        # Toolbar components
        self.import_tool = self.AddLabelTool(-1, "Import data...", 
        import_bmp, shortHelp="Import data...")
        
        self.load_image_tool = self.AddLabelTool(-1, "Import image...", 
        load_image_bmp, shortHelp="Import image...")
        
        self.function_tool = self.AddLabelTool(-1, "Generate data...", 
        function_bmp, shortHelp=u"Generate data from f(x)...")
        
        self.bivariable_function_tool = self.AddLabelTool(-1, "Generate data...", 
        bivariable_function_bmp, shortHelp=u"Generate data from f(x,y)...")
        
        self.AddSeparator()
        self.AddSeparator()
        self.AddSeparator()
        self.AddSeparator()
        
        self.plot_tool = self.AddLabelTool(-1, u"Lines", 
        plot_bmp, shortHelp=u"Lines")
        
        #~ self.polar_tool = self.AddLabelTool(-1, u"Polar", 
        #~ polar_bmp, shortHelp=u"Polar")
        
        self.bar_tool = self.AddLabelTool(-1, "Bars", 
        bar_bmp, shortHelp=u"Bars")
        
        self.scatter_tool = self.AddLabelTool(-1, "Scatter", 
        scatter_bmp, shortHelp=u"Scatter")
        
        self.pie_tool = self.AddLabelTool(-1, "Pie", 
        pie_bmp, shortHelp=u"Pie")
        
        self.image_tool = self.AddLabelTool(-1, "Image", 
        image_bmp, shortHelp=u"Image")
        
        self.contour_tool = self.AddLabelTool(-1, "Contour", 
        contour_bmp, shortHelp=u"Contour")
        
        self.contourf_tool = self.AddLabelTool(-1, "Filled contour", 
        contourf_bmp, shortHelp=u"Filled contour")
        

class AxesToolbar(wx.ToolBar):
    def __init__(self,parent,**kwargs):
        wx.ToolBar.__init__(self,parent=parent,style=wx.TB_VERTICAL,**kwargs)
        tbsize = (24,24)
        self.SetToolBitmapSize(tbsize)
        self.SetBackgroundColour("#ffffff")
        
        # Bitmaps
        zoom_box_bmp = wx.Bitmap(PATH_ZOOM_BOX_ICON)
        reset_view_bmp = wx.Bitmap(PATH_RESET_VIEW_ICON)
        axes_color_bmp = wx.Bitmap(PATH_AXES_COLOR_ICON)
        grid_color_bmp = wx.Bitmap(PATH_GRID_COLOR_ICON)
        grid_style_bmp = wx.Bitmap(PATH_GRID_STYLE_ICON)
        line_color_bmp = wx.Bitmap(PATH_LINE_COLOR_ICON)
        line_style_bmp = wx.Bitmap(PATH_LINE_STYLE_ICON)
        line_width_bmp = wx.Bitmap(PATH_LINE_WIDTH_ICON)
        line_label_bmp = wx.Bitmap(PATH_LINE_LABEL_ICON)
        show_legend_bmp = wx.Bitmap(PATH_SHOW_LEGEND_ICON)
        
        xlabel_bmp = wx.Bitmap(PATH_XLABEL_ICON)
        ylabel_bmp = wx.Bitmap(PATH_YLABEL_ICON)
        xticks_bmp = wx.Bitmap(PATH_XTICKS_ICON)
        yticks_bmp = wx.Bitmap(PATH_YTICKS_ICON)
        pie_labels_bmp = wx.Bitmap(PATH_PIE_LABELS_ICON)
        
        text_bmp = wx.Bitmap(PATH_TEXT_ICON)
        move_text_bmp = wx.Bitmap(PATH_MOVE_TEXT_ICON)
        move_line_bmp = wx.Bitmap(PATH_MOVE_LINE_ICON)
        
        
        
        self.zoom_box_tool = self.AddLabelTool(-1, "Zoom Box", 
        zoom_box_bmp, shortHelp=u"Zoom Box")
        
        self.reset_view_tool = self.AddLabelTool(-1, "Reset view", 
        reset_view_bmp, shortHelp=u"Reset view")
        
        self.AddSeparator()
        
        self.axes_color_tool = self.AddLabelTool(-1, "Axes color", 
        axes_color_bmp, shortHelp=u"Axes color")
        
        self.grid_color_tool = self.AddLabelTool(-1, "Grid color", 
        grid_color_bmp, shortHelp=u"Grid color")
        
        self.grid_style_tool = self.AddLabelTool(-1, "Grid style", 
        grid_style_bmp, shortHelp=u"Grid style")
        
        self.AddSeparator()
        
        self.xlabel_tool = self.AddLabelTool(-1, u"X-Label", 
        xlabel_bmp, shortHelp=u"X-Label")
        
        self.ylabel_tool = self.AddLabelTool(-1, u"Y-Label", 
        ylabel_bmp, shortHelp=u"Y-Label")
        
        self.xticks_tool = self.AddLabelTool(-1, u"X-Ticks", 
        xticks_bmp, shortHelp=u"X-Ticks")
        
        self.yticks_tool = self.AddLabelTool(-1, u"Y-Ticks", 
        yticks_bmp, shortHelp=u"Y-Ticks")


class LineToolbar(wx.ToolBar):
    def __init__(self,parent,**kwargs):
        wx.ToolBar.__init__(self,parent=parent,style=wx.TB_VERTICAL,**kwargs)
        tbsize = (24,24)
        self.SetToolBitmapSize(tbsize)
        self.SetBackgroundColour("#ffffff") # White
        
        # Bitmaps
        line_color_bmp = wx.Bitmap(PATH_LINE_COLOR_ICON)
        line_style_bmp = wx.Bitmap(PATH_LINE_STYLE_ICON)
        line_width_bmp = wx.Bitmap(PATH_LINE_WIDTH_ICON)
        line_label_bmp = wx.Bitmap(PATH_LINE_LABEL_ICON)
        show_legend_bmp = wx.Bitmap(PATH_SHOW_LEGEND_ICON)
        move_line_bmp = wx.Bitmap(PATH_MOVE_LINE_ICON)
        pie_labels_bmp = wx.Bitmap(PATH_PIE_LABELS_ICON)
        text_bmp = wx.Bitmap(PATH_TEXT_ICON)
        move_text_bmp = wx.Bitmap(PATH_MOVE_TEXT_ICON)

        self.line_color_tool = self.AddLabelTool(-1, u"Line color", 
        line_color_bmp, shortHelp=u"Line color")
        
        self.line_style_tool = self.AddLabelTool(-1, u"Line style", 
        line_style_bmp, shortHelp=u"Line style")
        
        self.line_width_tool = self.AddLabelTool(-1, u"Line width", 
        line_width_bmp, shortHelp=u"Line width")
        
        self.line_label_tool = self.AddLabelTool(-1, u"Line label", 
        line_label_bmp, shortHelp=u"Line label")
        
        self.show_legend_tool = self.AddLabelTool(-1, u"Show legends", 
        show_legend_bmp, shortHelp=u"Show legends")
        
        self.AddSeparator()
        
        self.text_tool = self.AddLabelTool(-1, u"Text", 
        text_bmp, shortHelp=u"Insert text/annotation")
        
        self.AddSeparator()
        
        self.pie_labels_tool = self.AddLabelTool(-1, u"Pie Labels", 
        pie_labels_bmp, shortHelp=u"Pie Labels")
        
        self.AddSeparator()
        
        self.move_line_tool = self.AddLabelTool(-1, u"Move line", 
        move_line_bmp, shortHelp=u"Move line")
        
        self.move_text_tool = self.AddLabelTool(-1, u"Move text", 
        move_text_bmp, shortHelp=u"Move text")


if __name__=='__main__':
    test_axestoolbar()
