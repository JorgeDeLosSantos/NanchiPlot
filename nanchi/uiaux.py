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
        self.SetBackgroundColour("#eeeeff")
        
        # Bitmaps
        zoom_box_bmp = wx.Bitmap(PATH_ZOOM_BOX_ICON)
        reset_view_bmp = wx.Bitmap(PATH_RESET_VIEW_ICON)
        axes_color_bmp = wx.Bitmap(PATH_AXES_COLOR_ICON)
        grid_color_bmp = wx.Bitmap(PATH_GRID_COLOR_ICON)
        grid_style_bmp = wx.Bitmap(PATH_GRID_STYLE_ICON)
        line_color_bmp = wx.Bitmap(PATH_LINE_COLOR_ICON)
        line_style_bmp = wx.Bitmap(PATH_LINE_STYLE_ICON)
        line_width_bmp = wx.Bitmap(PATH_LINE_WIDTH_ICON)
        
        xlabel_bmp = wx.Bitmap(PATH_XLABEL_ICON)
        ylabel_bmp = wx.Bitmap(PATH_YLABEL_ICON)
        xticks_bmp = wx.Bitmap(PATH_XTICKS_ICON)
        yticks_bmp = wx.Bitmap(PATH_YTICKS_ICON)
        
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
        
        self.line_color_tool = self.AddLabelTool(-1, u"Color de línea", 
        line_color_bmp, shortHelp=u"Color de línea")
        
        self.line_style_tool = self.AddLabelTool(-1, u"Estilo de línea", 
        line_style_bmp, shortHelp=u"Estilo de línea")
        
        self.line_width_tool = self.AddLabelTool(-1, u"Grosor de línea", 
        line_width_bmp, shortHelp=u"Grosor de línea")
        
        self.AddSeparator()
        
        self.text_tool = self.AddLabelTool(-1, u"Texto", 
        text_bmp, shortHelp=u"Insertar texto/anotación")
        
        self.AddSeparator()
        
        self.xlabel_tool = self.AddLabelTool(-1, u"XLabel", 
        xlabel_bmp, shortHelp=u"Modificar XLabel")
        
        self.ylabel_tool = self.AddLabelTool(-1, u"YLabel", 
        ylabel_bmp, shortHelp=u"Modificar YLabel")
        
        self.xticks_tool = self.AddLabelTool(-1, u"XTicks", 
        xticks_bmp, shortHelp=u"Modificar XTikcs")
        
        self.yticks_tool = self.AddLabelTool(-1, u"YTicks", 
        yticks_bmp, shortHelp=u"Modificar YTikcs")
        
        self.AddSeparator()
        
        self.move_line_tool = self.AddLabelTool(-1, u"Mover línea", 
        move_line_bmp, shortHelp=u"Mover línea")
        
        self.move_text_tool = self.AddLabelTool(-1, u"Mover texto", 
        move_text_bmp, shortHelp=u"Mover texto")
        
    

class FunctionDialog(wx.Dialog):
    def __init__(self,parent,**kwargs):
        #_styles = (wx.CLOSE_BOX|wx.CAPTION)
        wx.Dialog.__init__(self,parent=parent,title=DEFAULT_DIALOG_CAPTION,
                          size=(200,150))
        self.LABEL_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.initCtrls()
        self.initSizers()
        
        # Output properties
        self.data = ""
        self.out_fun = ""
        self.out_a = ""
        self.out_b = ""
        
        self.Centre(True)
        #self.Show()
        
    def initSizers(self):
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        self.pfunsz = wx.BoxSizer(wx.HORIZONTAL)
        self.prangesz = wx.BoxSizer(wx.HORIZONTAL)
        self.pbuttonsz = wx.BoxSizer(wx.HORIZONTAL)
        
        self.pfunsz.Add(self._fun, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        self.pfunsz.Add(self.fun, 4, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangesz.Add(self._a, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangesz.Add(self.a, 4, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangesz.Add(self._b, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangesz.Add(self.b, 4, wx.ALIGN_LEFT|wx.ALL, 5)
        
        self.pbuttonsz.Add(self.okbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.pbuttonsz.Add(self.cancelbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        for panel in [self.pfun, self.prange, self.pbutton]:
            self.mainsz.Add(panel, 1, wx.EXPAND)
        
        self.pfun.SetSizer(self.pfunsz)
        self.prange.SetSizer(self.prangesz)
        self.pbutton.SetSizer(self.pbuttonsz)
        self.SetSizer(self.mainsz)
        
    def initCtrls(self):
        self.pfun = wx.Panel(self, -1)
        self.prange = wx.Panel(self, -1)
        self.pbutton = wx.Panel(self, -1)
        self._fun = wx.StaticText(self.pfun, -1, u"f(x)", size=(-1,25))
        self.fun = wx.TextCtrl(self.pfun, -1, u"x**2", size=(-1,25))
        self._a = wx.StaticText(self.prange, -1, u"a", size=(-1,25))
        self.a = wx.TextCtrl(self.prange, -1, u"0", size=(50,25))
        self._b = wx.StaticText(self.prange, -1, u"b", size=(-1,25))
        self.b = wx.TextCtrl(self.prange, -1, u"10", size=(50,25))
        
        self.okbutton = wx.Button(self.pbutton, wx.ID_OK, u"Aceptar", size=(-1,25))
        self.cancelbutton = wx.Button(self.pbutton, wx.ID_CANCEL, u"Cancelar", size=(-1,25), 
                                style=wx.ID_CANCEL)
        
        for ctrl in [self._fun,self._a,self._b]:
            ctrl.SetFont(self.LABEL_FONT)
            
    def GetData(self):
        self.out_fun = self.fun.GetValue()
        self.out_a = self.a.GetValue()
        self.out_b = self.b.GetValue()
        self.data = (self.out_fun, self.out_a, self.out_b)
        return self.data
        

class BivariableFunctionDialog(wx.Dialog):
    def __init__(self,parent,**kwargs):
        #_styles = (wx.CLOSE_BOX|wx.CAPTION)
        wx.Dialog.__init__(self,parent=parent,title=DEFAULT_DIALOG_CAPTION,
                          size=(220,180))
        self.LABEL_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.initCtrls()
        self.initSizers()
        
        # Output properties
        self.data = ""
        self.out_fun = ""
        self.out_x = ""
        self.out_y = ""
        
        self.Centre(True)
        #self.Show()
        
    def initSizers(self):
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        self.pfunsz = wx.BoxSizer(wx.HORIZONTAL)
        self.prangexsz = wx.BoxSizer(wx.HORIZONTAL)
        self.prangeysz = wx.BoxSizer(wx.HORIZONTAL)
        self.pbuttonsz = wx.BoxSizer(wx.HORIZONTAL)
        
        self.pfunsz.Add(self._fun, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        self.pfunsz.Add(self.fun, 4, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangexsz.Add(self._x1, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangexsz.Add(self.x1, 4, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangexsz.Add(self._x2, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangexsz.Add(self.x2, 4, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangeysz.Add(self._y1, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangeysz.Add(self.y1, 4, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangeysz.Add(self._y2, 1, wx.ALIGN_LEFT|wx.ALL, 5)
        self.prangeysz.Add(self.y2, 4, wx.ALIGN_LEFT|wx.ALL, 5)
        
        self.pbuttonsz.Add(self.okbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.pbuttonsz.Add(self.cancelbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        for panel in [self.pfun, self.prangex, self.prangey, self.pbutton]:
            self.mainsz.Add(panel, 1, wx.EXPAND)
        
        self.pfun.SetSizer(self.pfunsz)
        self.prangex.SetSizer(self.prangexsz)
        self.prangey.SetSizer(self.prangeysz)
        self.pbutton.SetSizer(self.pbuttonsz)
        self.SetSizer(self.mainsz)
        
    def initCtrls(self):
        self.pfun = wx.Panel(self, -1)
        self.prangex = wx.Panel(self, -1)
        self.prangey = wx.Panel(self, -1)
        self.pbutton = wx.Panel(self, -1)
        self._fun = wx.StaticText(self.pfun, -1, u"f(x,y)", size=(-1,25))
        self.fun = wx.TextCtrl(self.pfun, -1, u"(x*y)/(x**2+y**2)", size=(-1,25))
        self._x1 = wx.StaticText(self.prangex, -1, u"x1", size=(-1,25))
        self.x1 = wx.TextCtrl(self.prangex, -1, u"-10", size=(50,25))
        self._x2 = wx.StaticText(self.prangex, -1, u"x2", size=(-1,25))
        self.x2 = wx.TextCtrl(self.prangex, -1, u"10", size=(50,25))
        self._y1 = wx.StaticText(self.prangey, -1, u"y1", size=(-1,25))
        self.y1 = wx.TextCtrl(self.prangey, -1, u"-10", size=(50,25))
        self._y2 = wx.StaticText(self.prangey, -1, u"y2", size=(-1,25))
        self.y2 = wx.TextCtrl(self.prangey, -1, u"10", size=(50,25))
        
        self.okbutton = wx.Button(self.pbutton, wx.ID_OK, u"Aceptar", size=(-1,25))
        self.cancelbutton = wx.Button(self.pbutton, wx.ID_CANCEL, u"Cancelar", size=(-1,25), 
                                style=wx.ID_CANCEL)
        
        for ctrl in [self._fun,self._x1, self._x2, self._y1, self._y2]:
            ctrl.SetFont(self.LABEL_FONT)
            
    def GetData(self):
        self.out_fun = self.fun.GetValue()
        self.out_x = [self.x1.GetValue(), self.x2.GetValue()]
        self.out_y = [self.y1.GetValue(), self.y2.GetValue()]
        self.data = (self.out_fun, self.out_x, self.out_y)
        return self.data


class AboutDialog(wx.Frame):
    def __init__(self,parent,*args,**kwargs):
        _styles = wx.CAPTION|wx.CLOSE_BOX
        wx.Frame.__init__(self,parent=parent,title=NANCHI_MAIN_CAPTION,
        size=(350,220), style=_styles)
        self.winhtml = HTMLWindow(self)
        self.winhtml.LoadPage("nanchi/help/about.html")
        self.Centre(True)
        self.Show()


class HTMLWindow(html.HtmlWindow):
    def __init__(self,parent,**kwargs):
        html.HtmlWindow.__init__(self,parent=parent,**kwargs)
    
    def OnLinkClicked(self, link):
        webbrowser.open(link.GetHref())


class StatusBar(wx.StatusBar):
    def __init__(self,*args,**kwargs):
        wx.StatusBar.__init__(self,*args,**kwargs)
        

class BusyInfo(object):
    def __init__(self, msg, parent=None, bgColour="#f0f0f0", fgColour="#8080ff"):
        self.frame = _InfoFrame(parent, msg, bgColour, fgColour)
        self.frame.Show()
        self.frame.Refresh()
        self.frame.Update()
        
    def __del__(self):
        self.Close()
        
    def Close(self):
        """
        Hide and close the busy info box
        """
        if self.frame:
            self.frame.Hide()
            self.frame.Close()
            self.frame = None
    
    # Magic methods for using this class as a Context Manager 
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close()
        return False


class _InfoFrame(wx.Frame):
    def __init__(self, parent, msg, bgColour=None, fgColour=None):
        wx.Frame.__init__(self, parent, style=wx.BORDER_SIMPLE|wx.FRAME_TOOL_WINDOW|wx.STAY_ON_TOP)

        bgColour = bgColour if bgColour is not None else wx.Colour(253, 255, 225)
        fgColour = fgColour if fgColour is not None else wx.BLACK

        panel = wx.Panel(self)
        text = wx.StaticText(panel, -1, msg)
        
        for win in [panel, text]:
            win.SetCursor(wx.HOURGLASS_CURSOR)
            win.SetBackgroundColour(bgColour)
            win.SetForegroundColour(fgColour)
            
        size = text.GetBestSize()
        self.SetClientSize((size.width + 60, size.height + 40))
        panel.SetSize(self.GetClientSize())
        text.Center()
        self.Center()


class LogCtrl(wx.TextCtrl):
    def __init__(self,parent,**kwargs):
        wx.TextCtrl.__init__(self, parent=parent, id=wx.ID_ANY,
                             style=wx.TE_MULTILINE, **kwargs)
        self.font = wx.Font(9, wx.MODERN, wx.NORMAL, wx.BOLD)
        self.SetFont(self.font)
        self.SetForegroundColour("#ff5050")
        
    def write(self,string):
        _nvalue = ">>> %s"%(string)
        self.SetValue(_nvalue)
    

class ImportDialog(wx.Dialog):
    def __init__(self,parent,**kwargs):
        wx.Dialog.__init__(self,parent=parent,title=DEFAULT_DIALOG_CAPTION,
                          size=(800,500))
        self.LABEL_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.VALUE_FONT = wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.initCtrls()
        self.initSizers()
        
        self.Centre(True)

    def initSizers(self):
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        self.panelsz = wx.BoxSizer(wx.HORIZONTAL)
        self.plogsz = wx.BoxSizer(wx.HORIZONTAL)
        self.pctrlssz = wx.BoxSizer(wx.VERTICAL)
        self.pbuttonsz = wx.BoxSizer(wx.HORIZONTAL)
        
        #
        self.pctrlssz.Add(self._dlm, 0, wx.EXPAND|wx.ALL, 5)
        self.pctrlssz.Add(self.dlm, 0, wx.EXPAND|wx.ALL, 5)
        self.pctrlssz.Add(self._skiprows, 0, wx.EXPAND|wx.ALL, 5)
        self.pctrlssz.Add(self.skiprows, 0, wx.EXPAND|wx.ALL, 5)
        self.pctrlssz.Add(self.preview, 0, wx.ALIGN_CENTRE|wx.ALL, 10)
        
        self.panelsz.Add(self.fctrl, 1, wx.EXPAND|wx.ALL, 5)
        self.panelsz.Add(self.pctrls, 1, wx.EXPAND|wx.ALL, 5)
        self.panelsz.Add(self.grid, 2, wx.EXPAND|wx.ALL, 5)
        
        self.plogsz.Add(self.log, 1, wx.EXPAND|wx.ALL, 5)
        
        self.pbuttonsz.Add(self.okbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        self.pbuttonsz.Add(self.cancelbutton, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        self.mainsz.Add(self.panel, 5, wx.EXPAND|wx.ALL, 5)
        self.mainsz.Add(self.plog, 1, wx.EXPAND|wx.ALL, 5)
        self.mainsz.Add(self.pbutton, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
        
        self.pctrls.SetSizer(self.pctrlssz)
        self.panel.SetSizer(self.panelsz)
        self.plog.SetSizer(self.plogsz)
        self.pbutton.SetSizer(self.pbuttonsz)
        self.SetSizer(self.mainsz)
        
    def initCtrls(self):
        self.panel = wx.Panel(self, -1)
        self.plog = wx.Panel(self, -1)
        self.pbutton = wx.Panel(self, -1)
        self.pctrls = wx.Panel(self.panel, -1)
        
        wc = IMPORT_DIALOG_WILDCARD
        
        self.fctrl = wx.FileCtrl(self.panel, -1, wildCard=wc)
        self.grid = ui.DataGrid(self.panel, (10,1))
        self.grid.SetRowLabelSize(0)
        self.grid.SetColLabelSize(0)
        
        # Controles conf.
        self._dlm = wx.StaticText(self.pctrls, -1, u"Delimitador", size=(-1,25))
        self.dlm = wx.TextCtrl(self.pctrls, -1, u",", size=(-1,25))
        self.dlm.SetFont(self.VALUE_FONT)
        self._skiprows = wx.StaticText(self.pctrls, -1, u"Leer a partir de fila:", size=(-1,25))
        self.skiprows = wx.SpinCtrl(self.pctrls, -1, min=1, max=100)
        self.preview = wx.Button(self.pctrls, -1, u"Vista previa")
        
        # Set labels
        for label in [self._dlm, self._skiprows]:
            label.SetFont(self.LABEL_FONT)
            label.SetForegroundColour("#556655")
        
        # Log 
        self.log = LogCtrl(self.plog)
        
        # Botones
        self.okbutton = wx.Button(self.pbutton, wx.ID_OK, u"Aceptar", size=(100,25))
        self.cancelbutton = wx.Button(self.pbutton, wx.ID_CANCEL, u"Cancelar", 
                                      size=(100,25), style=wx.ID_CANCEL)
        
        self.Bind(wx.EVT_BUTTON, self.OnPreview, self.preview)
        
    def OnPreview(self,event):
        self.grid.SetArrayData(np.array(([[],[]])))
        filename = self.fctrl.GetPath()
        delimiter = self.dlm.GetValue()
        skipr = self.skiprows.GetValue()
        mps = 100 # max preview size
        try:
            data = io.read_txt(filename, delimiter=delimiter, skiprows=skipr)
            if not data is None:
                if data.shape[0]>mps and data.shape[1]>mps:
                    self.grid.SetArrayData(data[:mps,:mps])
                elif data.shape[0]>mps and data.shape[1]<mps:
                    self.grid.SetArrayData(data[:mps,:])
                elif data.shape[0]<mps and data.shape[1]>mps:
                    self.grid.SetArrayData(data[:,:mps])
                else:
                    self.grid.SetArrayData(data)
                infostr = u"Vista previa de datos leídos de %s\nTamaño: (%g,%g)"%(
                                                            filename,
                                                            data.shape[0],
                                                            data.shape[1])
                self.log.write(infostr)
            else:
                self.log.write(u"No se han podido leer los datos")
        except Exception as exc:
            self.log.write(exc)

    def GetData(self):
        filename = self.fctrl.GetPath()
        delimiter = self.dlm.GetValue()
        skiprows = self.skiprows.GetValue()
        try:
            data = io.read_txt(filename, delimiter=delimiter, skiprows=skiprows)
            if not data is None:
                return data
            else:
                self.log.write("No se han podido leer los datos")
        except Exception as exc:
            self.log.write(exc)
        

class TickDialog(wx.Dialog):
    def __init__(self,parent,axes,xy,**kwargs):
        wx.Dialog.__init__(self,parent=parent,title=DEFAULT_DIALOG_CAPTION,
                          size=(200,400))
        #~ self.LABEL_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.xy = xy
        self.ctick = axes.get_xticks() if xy=="x" else axes.get_yticks()
        self.clabel = axes.get_xticklabels() if xy=="x" else axes.get_yticklabels()
        self.axes = axes
        self.initCtrls()
        self.initSizers()
        self.initConfig()
        self.Centre(True)
        
    def initCtrls(self):
        self.panel = wx.Panel(self, -1)
        self.pbutton = wx.Panel(self, -1)

        self.grid = TickGrid(self.panel)
        
        self.okbt = wx.Button(self.pbutton, wx.ID_OK, u"Aceptar")
        self.cancelbt =    wx.Button(self.pbutton, wx.ID_CANCEL, u"Cancelar")
        
    def initSizers(self):
        self.sz = wx.BoxSizer(wx.VERTICAL)
        self.panelsz = wx.BoxSizer(wx.VERTICAL)
        self.pbuttonsz = wx.BoxSizer(wx.HORIZONTAL)
        
        self.panelsz.Add(self.grid, 1, wx.EXPAND|wx.ALL, 5)
        
        self.pbuttonsz.Add(self.okbt, 1, wx.EXPAND|wx.ALL, 5)
        self.pbuttonsz.Add(self.cancelbt, 1, wx.EXPAND|wx.ALL, 5)
        
        self.sz.Add(self.panel, 8, wx.EXPAND|wx.ALL, 5)
        self.sz.Add(self.pbutton, 1, wx.EXPAND|wx.ALL, 5)
        
        self.SetSizer(self.sz)
        self.panel.SetSizer(self.panelsz)
        self.pbutton.SetSizer(self.pbuttonsz)
        
    def initConfig(self):
        nrows = len(self.ctick)
        self.grid.UpdateGridSize(nrows,2)
        for ii in range(nrows):
            self.grid.SetCellValue(ii,0,str(self.ctick[ii]))
            label = self.clabel[ii].get_text()
            if not label:
                self.grid.SetCellValue(ii,1,str(self.ctick[ii]))
            else:
                self.grid.SetCellValue(ii,1,label)
        
    def GetData(self):
        data = zip(*self.grid.GetArrayData())
        ticks = [float(xt) for xt in data[0]]
        labels = data[1]
        return ticks,labels


class TickGrid(wxgrid.Grid):
    def __init__(self,parent,**kwargs):
        wxgrid.Grid.__init__(self,parent=parent,id=-1,**kwargs)
        gridsize = (2,2)
        rows = int(gridsize[0])
        cols = int(gridsize[1])
        self.CreateGrid(rows,cols)
        self.SetRowLabelSize(0)
        self.SetColLabelValue(0, "Tick")
        self.SetColLabelValue(1, "Etiqueta")
        self.Bind(wxgrid.EVT_GRID_CELL_CHANGE, self.OnCellEdit)
        self.Bind(wxgrid.EVT_GRID_CELL_RIGHT_CLICK, self.OnRightClick)
        
    def GetArrayData(self):
        nrows = self.GetNumberRows()
        ncols = self.GetNumberCols()
        X = []
        for i in range(nrows):
            row = []
            for j in range(ncols):
                cval = self.GetCellValue(i,j)
                if not isempty(cval):
                    row.append(cval)
                else:
                    row.append("")
            X.append(row)
        return X
        
    def UpdateGridSize(self,rows,cols):
        self.ClearGrid()
        ccols = self.GetNumberCols()
        crows = self.GetNumberRows()
        
        if rows > crows:
            self.AppendRows(rows-crows)
        elif rows < crows:
            self.DeleteRows(0,crows-rows)
            
        if cols > ccols:
            self.AppendCols(cols-ccols)
        elif cols < ccols:
            self.DeleteCols(0,ccols-cols)
            
    def GetSelectedRows(self):
        srows = []
        top_left = self.GetSelectionBlockTopLeft()
        bottom_right = self.GetSelectionBlockBottomRight()
        if not isempty(bottom_right) and not isempty(top_left):
            max_row = bottom_right[0][0]
            min_row = top_left[0][0]
            srows = range(min_row,max_row+1)
        return srows
        
    def OnCellEdit(self,event):
        pass
        
    def OnRightClick(self,event):
        pum = wx.Menu()
        addrow = wx.MenuItem(pum, -1, "Agregar fila...")
        pum.AppendItem(addrow)
        
        pum.AppendSeparator()
        
        delrows = wx.MenuItem(pum, -1, "Eliminar filas")
        pum.AppendItem(delrows)
        
        pum.AppendSeparator()
        
        clearcell = wx.MenuItem(pum, -1, "Limpiar celdas")
        pum.AppendItem(clearcell)
        
        # Binds
        pum.Bind(wx.EVT_MENU, self.del_rows, delrows)
        pum.Bind(wx.EVT_MENU, self.add_row, addrow)
        pum.Bind(wx.EVT_MENU, self.clear_cell, clearcell)

        # Show 
        self.PopupMenu(pum)
        pum.Destroy()

    def del_rows(self,event):
        rows = self.GetSelectedRows()
        self.DeleteRows(rows[0],len(rows))
        
    def add_row(self,event):
        self.AppendRows(1)
        
    def clear_cell(self,event):
        top_left = self.GetSelectionBlockTopLeft()
        bottom_right = self.GetSelectionBlockBottomRight()
        row_range = range(top_left[0][0], bottom_right[0][0] + 1)
        col_range = range(top_left[0][1], bottom_right[0][1] + 1)
        for ii in row_range:
            for jj in col_range:
                self.SetCellValue(ii,jj,u"")



class LineStyleDialog(wx.Dialog):
    def __init__(self,parent,**kwargs):
        wx.Dialog.__init__(self,parent=parent,title=DEFAULT_DIALOG_CAPTION,
                          size=(200,120))
        self.LABEL_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD)
        self.initCtrls()
        self.initSizers()
        self.Centre(True)
        
    def initCtrls(self):
        self.panel = wx.Panel(self, -1)
        self.pbutton = wx.Panel(self, -1)
        
        self._label = wx.StaticText(self.panel, -1, u"Seleccione un estilo de línea")
        self._lstyles = "-|--|:|-.".split("|")
        self.options = wx.ComboBox(self.panel, -1, choices=self._lstyles)
        self.options.SetFont(self.LABEL_FONT)
        
        self.okbt = wx.Button(self.pbutton, wx.ID_OK, u"Aceptar")
        self.cancelbt =    wx.Button(self.pbutton, wx.ID_CANCEL, u"Cancelar")
        
    def initSizers(self):
        self.sz = wx.BoxSizer(wx.VERTICAL)
        self.panelsz = wx.BoxSizer(wx.VERTICAL)
        self.pbuttonsz = wx.BoxSizer(wx.HORIZONTAL)
        
        self.panelsz.Add(self._label, 1, wx.EXPAND|wx.ALL, 2)
        self.panelsz.Add(self.options, 1, wx.EXPAND|wx.ALL, 2)
        
        self.pbuttonsz.Add(self.okbt, 1, wx.EXPAND|wx.ALL, 3)
        self.pbuttonsz.Add(self.cancelbt, 1, wx.EXPAND|wx.ALL, 3)
        
        self.sz.Add(self.panel, 2, wx.EXPAND|wx.ALL, 2)
        self.sz.Add(self.pbutton, 1, wx.EXPAND|wx.ALL, 2)
        
        self.SetSizer(self.sz)
        self.panel.SetSizer(self.panelsz)
        self.pbutton.SetSizer(self.pbuttonsz)

    def GetData(self):
        _ls = self.options.GetValue()
        if not _ls in self._lstyles:
            _ls = "-"
        return _ls


def test_toolbar():
    app = wx.App()
    fr = wx.Frame(None, -1, "Hi !!!", size=(800,600))
    sz = wx.BoxSizer(wx.VERTICAL)
    tb = CustomTB(fr)
    sz.Add(tb, 0, wx.EXPAND)
    fr.SetSizer(sz)
    tb.Realize()
    fr.Show()
    app.MainLoop()    
    
    
def test_about():
    app=wx.App()
    fr = AboutDialog(None)
    app.MainLoop()


def test_function():
    app = wx.App()
    fr = BivariableFunctionDialog(None)
    if fr.ShowModal() == wx.ID_OK:
        print fr.GetData()
    fr.Destroy()
    app.MainLoop()


def test_import():
    app = wx.App()
    fr = ImportDialog(None)
    if fr.ShowModal() == wx.ID_OK:
        print fr.GetData()
    fr.Destroy()
    app.MainLoop()
    
    
def test_tick():
    f = plt.figure()
    ax = f.add_subplot(111)
    app = wx.App()
    fr = TickDialog(None,ax,"x")
    if fr.ShowModal() == wx.ID_OK:
        print fr.GetData()
    fr.Destroy()
    app.MainLoop()
    

def test_axestoolbar():
    app = wx.App()
    fr = wx.Frame(None, -1, "Hi !!!", size=(800,600))
    sz = wx.BoxSizer(wx.VERTICAL)
    tb = AxesToolbar(fr)
    sz.Add(tb, 0, wx.EXPAND)
    fr.SetSizer(sz)
    tb.Realize()
    fr.Show()
    app.MainLoop()    


def test_linestyle():
    app = wx.App()
    fr = LineStyleDialog(None)
    if fr.ShowModal() == wx.ID_OK:
        print fr.GetData()
    fr.Destroy()
    app.MainLoop()
    


if __name__=='__main__':
    test_linestyle()
