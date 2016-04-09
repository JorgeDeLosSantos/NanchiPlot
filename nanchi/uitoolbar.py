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
        self.import_tool = self.AddLabelTool(-1, "Importar datos...", 
        import_bmp, shortHelp="Importar datos...")
        
        self.load_image_tool = self.AddLabelTool(-1, "Importar imagen...", 
        load_image_bmp, shortHelp="Importar imagen...")
        
        self.function_tool = self.AddLabelTool(-1, "Generar datos...", 
        function_bmp, shortHelp=u"Generar datos de función...")
        
        self.bivariable_function_tool = self.AddLabelTool(-1, "Generar datos...", 
        bivariable_function_bmp, shortHelp=u"Generar datos de función bivariable...")
        
        self.AddSeparator()
        self.AddSeparator()
        self.AddSeparator()
        self.AddSeparator()
        
        self.plot_tool = self.AddLabelTool(-1, u"Líneas", 
        plot_bmp, shortHelp=u"Líneas")
        
        #~ self.polar_tool = self.AddLabelTool(-1, u"Polar", 
        #~ polar_bmp, shortHelp=u"Polar")
        
        self.bar_tool = self.AddLabelTool(-1, "Barras", 
        bar_bmp, shortHelp=u"Barras")
        
        self.scatter_tool = self.AddLabelTool(-1, "Scatter", 
        scatter_bmp, shortHelp=u"Scatter")
        
        self.pie_tool = self.AddLabelTool(-1, "Pie", 
        pie_bmp, shortHelp=u"Pastel")
        
        self.image_tool = self.AddLabelTool(-1, "Imagen", 
        image_bmp, shortHelp=u"Imagen")
        
        self.contour_tool = self.AddLabelTool(-1, "Contorno", 
        contour_bmp, shortHelp=u"Contorno")
        
        self.contourf_tool = self.AddLabelTool(-1, "Contorno relleno", 
        contourf_bmp, shortHelp=u"Contorno relleno")
        

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
        reset_view_bmp, shortHelp=u"Vista inicial")
        
        self.AddSeparator()
        
        self.axes_color_tool = self.AddLabelTool(-1, "Axes color", 
        axes_color_bmp, shortHelp=u"Axes color")
        
        self.grid_color_tool = self.AddLabelTool(-1, "Color de rejilla", 
        grid_color_bmp, shortHelp=u"Color de rejilla")
        
        self.grid_style_tool = self.AddLabelTool(-1, "Estilo de rejilla", 
        grid_style_bmp, shortHelp=u"Estilo de rejilla")
        
        self.AddSeparator()
        
        self.xlabel_tool = self.AddLabelTool(-1, u"XLabel", 
        xlabel_bmp, shortHelp=u"Modificar XLabel")
        
        self.ylabel_tool = self.AddLabelTool(-1, u"YLabel", 
        ylabel_bmp, shortHelp=u"Modificar YLabel")
        
        self.xticks_tool = self.AddLabelTool(-1, u"XTicks", 
        xticks_bmp, shortHelp=u"Modificar XTicks")
        
        self.yticks_tool = self.AddLabelTool(-1, u"YTicks", 
        yticks_bmp, shortHelp=u"Modificar YTicks")


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

        self.line_color_tool = self.AddLabelTool(-1, u"Color de línea", 
        line_color_bmp, shortHelp=u"Color de línea")
        
        self.line_style_tool = self.AddLabelTool(-1, u"Estilo de línea", 
        line_style_bmp, shortHelp=u"Estilo de línea")
        
        self.line_width_tool = self.AddLabelTool(-1, u"Grosor de línea", 
        line_width_bmp, shortHelp=u"Grosor de línea")
        
        self.line_label_tool = self.AddLabelTool(-1, u"Etiqueta de línea", 
        line_label_bmp, shortHelp=u"Etiqueta de línea")
        
        self.show_legend_tool = self.AddLabelTool(-1, u"Mostrar leyendas", 
        show_legend_bmp, shortHelp=u"Mostrar leyendas")
        
        self.AddSeparator()
        
        self.text_tool = self.AddLabelTool(-1, u"Texto", 
        text_bmp, shortHelp=u"Insertar texto/anotación")
        
        self.AddSeparator()
        
        self.pie_labels_tool = self.AddLabelTool(-1, u"Pie Labels", 
        pie_labels_bmp, shortHelp=u"Pie Labels")
        
        self.AddSeparator()
        
        self.move_line_tool = self.AddLabelTool(-1, u"Mover línea", 
        move_line_bmp, shortHelp=u"Mover línea")
        
        self.move_text_tool = self.AddLabelTool(-1, u"Mover texto", 
        move_text_bmp, shortHelp=u"Mover texto")


if __name__=='__main__':
    test_axestoolbar()
