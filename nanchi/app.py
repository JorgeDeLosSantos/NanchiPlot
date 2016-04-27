# -*- coding: utf-8 -*-
#
# NanchiPlot 0.1.0-dev
# License: MIT License
# Author: Pedro Jorge De Los Santos
# E-mail: delossantosmfq@gmail.com
# Code: https://github.com/JorgeDeLosSantos/NanchiPlot
#
#~ from __future__ import absolute_import

import wx
import os
import numpy as np
import matplotlib
matplotlib.use('WXAgg') # wxPython backend
import matplotlib.cm as cm # Colormap
import setplot as setplot # Axes & Figure props
import iodata as io # Read & Write data
import uibase as ui # Base interfaces
import uiaux as aux # Auxiliar interfaces
import uitoolbar as tb
import image as image # Image operations
from _const_ import * # Constants


class NanchiPlot(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,title=NANCHI_MAIN_CAPTION,size=(800,600))
        self.initMenu()
        self.initCtrls()
        self.initCtrls()
        self.initToolBar()
        self.initSizers()
        self.initEvents()
        
        # Icon
        self.icon = wx.Icon(PATH_NANCHI_LOGO)
        self.SetIcon(self.icon)
        
        self.axes = self.notebook.graphs.axes
        self.figure = self.notebook.graphs.figure
        self.canvas = self.notebook.graphs.canvas
        self.data = self.notebook.data
        
        self.Centre(True)
        self.Show()
        
    def initMenu(self):
        """
        Creating Menu bar
        """
        m_file = wx.Menu()
        save = m_file.Append(-1, "Save image... \tCtrl+S")
        export_img = m_file.Append(-1, "Export data as image...")
        export_txt = m_file.Append(-1, "Export data as ASCII...")
        m_file.AppendSeparator()
        import_data = m_file.Append(-1, "Import data... \tCtrl+I")
        import_image = m_file.Append(-1, "Import image...")
        m_file.AppendSeparator()
        _exit = m_file.Append(-1, "Quit \tCtrl+Q")
        
        # Not support for image in 0.1.0 version
        #~ m_image = wx.Menu()
        #~ filters = wx.Menu()
        #~ sobel = wx.MenuItem(filters, -1, "Sobel")
        #~ filters.AppendItem(sobel)
        #~ roberts = wx.MenuItem(filters, -1, "Roberts")
        #~ filters.AppendItem(roberts)
        #~ prewitt = wx.MenuItem(filters, -1, "Prewitt")
        #~ filters.AppendItem(prewitt)
        #~ m_image.AppendMenu(-1, "Filters", filters)
        #~ binarizar = m_image.Append(-1, "Binarize")
        
        m_help = wx.Menu()
        _help = m_help.Append(-1, "Help")
        about = m_help.Append(-1, "About...")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(m_file, "File")
        #~ menu_bar.Append(m_image, "Imagen")
        menu_bar.Append(m_help, "Help")
        self.SetMenuBar(menu_bar)
        
        self.Bind(wx.EVT_MENU, self.OnSave, save)
        self.Bind(wx.EVT_MENU, self.OnExportASCII, export_txt)
        self.Bind(wx.EVT_MENU, self.OnExportImage, export_img)
        
        self.Bind(wx.EVT_MENU, self.OnImport, import_data)
        self.Bind(wx.EVT_MENU, self.OnLoadImage, import_image)
        
        #~ self.Bind(wx.EVT_MENU, self.OnSobel, sobel)
        #~ self.Bind(wx.EVT_MENU, self.OnRoberts, roberts)
        #~ self.Bind(wx.EVT_MENU, self.OnPrewitt, prewitt)
        #~ self.Bind(wx.EVT_MENU, self.OnBinarize, binarize)
        
        self.Bind(wx.EVT_MENU, self.OnAbout, about)
        self.Bind(wx.EVT_MENU, self.OnHelp, _help)
        self.Bind(wx.EVT_MENU, self.OnExit, _exit)
        
    def initSizers(self):
        """
        Inicializar los sizers
        """
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        self.panelsz = wx.BoxSizer(wx.HORIZONTAL)
        
        self.mainsz.Add(self.toolbar, 0, wx.EXPAND)
        self.panelsz.Add(self.notebook, 1, wx.EXPAND|wx.ALL, 2)
		
        self.panelsz.Add(self.axestoolbar, 0, wx.EXPAND|wx.ALL) # Quitando el borde
        self.panelsz.Add(self.linetoolbar, 0, wx.EXPAND|wx.ALL) # Quitando el borde
		
        self.mainsz.Add(self.mainpanel, 1, wx.EXPAND)
        
        self.mainpanel.SetSizer(self.panelsz)
        self.SetSizer(self.mainsz)
        
    def initCtrls(self):
        """
        Init basic controls
        """
        # Status bar
        self.SB_FONT = wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL)
        self.SB_FONT.SetFaceName(u"DejaVu Sans Mono")
        self.sb = aux.StatusBar(self, -1)
        self.sb.SetFont(self.SB_FONT)
        self.sb.SetForegroundColour("#aa00aa")
        self.SetStatusBar(self.sb)
        self.sb.SetStatusText(SB_ON_INIT)
        
        self.mainpanel = wx.Panel(self,-1)
        self.notebook = ui.NanchiNoteBook(self.mainpanel)
        
    def initToolBar(self):
        """
        Init tool bar
        """
        self.toolbar = tb.MainToolbar(self)
        self.toolbar.Realize()
        
        self.axestoolbar = tb.AxesToolbar(self.mainpanel)
        self.axestoolbar.Realize()
        
        self.linetoolbar = tb.LineToolbar(self.mainpanel)
        self.linetoolbar.Realize()
        
    def initEvents(self):
        """
        Init events
        """
        self.graphs = self.notebook.graphs
        
        self.Bind(wx.EVT_TOOL, self.OnImport, self.toolbar.import_tool)
        self.Bind(wx.EVT_TOOL, self.OnLoadImage, self.toolbar.load_image_tool)
        self.Bind(wx.EVT_TOOL, self.OnFunction, self.toolbar.function_tool)
        self.Bind(wx.EVT_TOOL, self.OnBivariableFunction, self.toolbar.bivariable_function_tool)
        self.Bind(wx.EVT_TOOL, self.OnPlot, self.toolbar.plot_tool)
        #self.Bind(wx.EVT_TOOL, self.OnPolar, self.toolbar.polar_tool)
        self.Bind(wx.EVT_TOOL, self.OnBar, self.toolbar.bar_tool)
        self.Bind(wx.EVT_TOOL, self.OnScatter, self.toolbar.scatter_tool)
        self.Bind(wx.EVT_TOOL, self.OnPie, self.toolbar.pie_tool)
        self.Bind(wx.EVT_TOOL, self.OnImage, self.toolbar.image_tool)
        self.Bind(wx.EVT_TOOL, self.OnContour, self.toolbar.contour_tool)
        self.Bind(wx.EVT_TOOL, self.OnContourf, self.toolbar.contourf_tool)
        
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnZoom, self.axestoolbar.zoom_box_tool)
        self.Bind(wx.EVT_TOOL, self.OnResetView, self.axestoolbar.reset_view_tool)
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnBackground, self.axestoolbar.axes_color_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnGridColor, self.axestoolbar.grid_color_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnGridStyle, self.axestoolbar.grid_style_tool)
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnXLabel, self.axestoolbar.xlabel_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnYLabel, self.axestoolbar.ylabel_tool)
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnXTicks, self.axestoolbar.xticks_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnYTicks, self.axestoolbar.yticks_tool)
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnLineColor, self.linetoolbar.line_color_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnLineWidth, self.linetoolbar.line_width_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnLineStyle, self.linetoolbar.line_style_tool)
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnLineLabel, self.linetoolbar.line_label_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnShowLegend, self.linetoolbar.show_legend_tool)
        
        self.Bind(wx.EVT_TOOL, self.OnPieLabels, self.linetoolbar.pie_labels_tool)
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnMoveLine, self.linetoolbar.move_line_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnMoveText, self.linetoolbar.move_text_tool)
        
        self.Bind(wx.EVT_TOOL, self.OnPieLabels, self.linetoolbar.pie_labels_tool)
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnMoveLine, self.linetoolbar.move_line_tool)
        self.Bind(wx.EVT_TOOL, self.graphs.OnMoveText, self.linetoolbar.move_text_tool)
        
        self.Bind(wx.EVT_TOOL, self.graphs.OnText, self.linetoolbar.text_tool)

        
    def OnExit(self,event):
        """
        Archivo -> Salir -> (Atajo) Ctrl+Q 
        """
        self.Close(True)
        
    def OnHelp(self,event):
        """
        Ayuda -> Ayuda
        
        Abre la documentación en HTML
        """
        try:
            os.startfile(PATH_DOCUMENTATION_HTML)
        except WindowsError:
            """ Not exist file"""
            pass
            
        
    def OnSave(self,event):
        """
        File -> Save image... -> (Short-Cut) Ctrl + S
        """
        wldc = "PNG (*.png)|*.png|PDF (*.pdf)|*.pdf|EPS (*.eps)|*.eps|JPG (*.jpg)|*jpg"
        dlg=wx.FileDialog(self, "Save", os.getcwd(), style=wx.SAVE, wildcard=wldc)
        if dlg.ShowModal() == wx.ID_OK:
            self.figure.savefig(dlg.GetPath())
        dlg.Destroy()
        
    def OnExportASCII(self,event):
        data = self.data.grid_data.GetArrayData()
        wldc = "TXT File (*.txt)|*.txt|DAT (*.dat)|*.dat"
        dlg=wx.FileDialog(self, "Save", os.getcwd(), style=wx.SAVE, wildcard=wldc)
        if dlg.ShowModal() == wx.ID_OK:
            fname = dlg.GetPath()
            io.write_txt(fname, data)
        dlg.Destroy()
        
    def OnExportImage(self,event):
        data = self.data.grid_data.GetArrayData()
        wldc = "PNG (*.png)|*.png|PDF (*.pdf)|*.pdf|JPG (*.jpg)|*jpg"
        dlg=wx.FileDialog(self, "Save", os.getcwd(), style=wx.SAVE, wildcard=wldc)
        if dlg.ShowModal() == wx.ID_OK:
            fname = dlg.GetPath()
            io.imsave(fname, data)
        dlg.Destroy()
    
        
    def OnImport(self,event):
        """
        Import data
        """
        dlg = aux.ImportDialog(None)
        if dlg.ShowModal() == wx.ID_OK:
            busy_dlg = aux.BusyInfo("Wait a moment...", self)
            data = dlg.GetData()
            if data is None:
                self.sb.SetStatusText(SB_ON_IMPORT_DATA_FAIL%(path))
                del busy_dlg
            else:
                self.data.grid_data.SetArrayData(data)
                del busy_dlg
        dlg.Destroy()
        
            
    def OnLoadImage(self,event):
        path = ""
        wildcard = "*.png"
        dlg = wx.FileDialog(self, message="Select an image",
        defaultDir=os.getcwd(), wildcard=wildcard, style=wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            busy_dlg = aux.BusyInfo("Wait a moment...", self)
            path = dlg.GetPath()
            data = io.imread(path)
            self.data.grid_data.SetArrayData(data)
            self.sb.SetStatusText(SB_ON_IMPORT_IMAGE%(path))
            del busy_dlg
        else:
            self.sb.SetStatusText(SB_ON_IMPORT_IMAGE_CANCEL)
        dlg.Destroy()
            
    def OnFunction(self,event):
        from numpy import (sin,cos,tan,log,exp)
        dialog = aux.FunctionDialog(None)
        if dialog.ShowModal() == wx.ID_OK:
            fx,a,b = dialog.GetData()
            x = np.linspace(float(a), float(b), 100)
            fx = eval(fx)
            self.data.grid_data.SetArrayData(np.array([x,fx]).transpose())
            self.data.grid_data.SetColLabelValue(0,"x")
            self.data.grid_data.SetColLabelValue(1,"f(x)")
            self.sb.SetStatusText(SB_ON_CREATE_DATA_FUNCTION)
        dialog.Destroy()
        
    def OnBivariableFunction(self,event):
        from numpy import (sin,cos,tan,log,exp)
        dialog = aux.BivariableFunctionDialog(None)
        if dialog.ShowModal() == wx.ID_OK:
            fxy,x,y = dialog.GetData()
            x1,x2 = [float(n) for n in x]
            y1,y2 = [float(n) for n in y]
            xx = np.linspace(x1, x2, 100)
            yy = np.linspace(y1, y2, 100)
            x,y = np.meshgrid(xx,yy)
            Z = eval(fxy)
            self.data.grid_data.SetArrayData(Z)
            self.sb.SetStatusText(SB_ON_CREATE_DATA_BIVARIABLE_FUNCTION)
        dialog.Destroy()
        
    def OnPlot(self,event):
        setplot.set_default_params(self.axes,self.figure)
        busy_dlg = aux.BusyInfo("Wait a moment...", self)
        X = self.data.grid_data.GetArrayData()
        rows,cols = X.shape
        if cols == 2: # Common case
            self.axes.plot(X[:,0],X[:,1], picker=True)
        elif cols == 1:
            self.axes.plot(X[:,0], picker=True)
        elif cols > 2:
            for col in range(cols):
                #clabel = self.data.grid_data.GetColLabelValue(col)
                self.axes.plot(X[:,col], picker=True)
        self.canvas.draw()
        del busy_dlg
        
    def OnPolar(self,event):
        """
        Unavailable
        """
        pass
        
    def OnBar(self,event):
        setplot.set_default_params(self.axes,self.figure)
        X = self.data.grid_data.GetArrayData()
        rows,cols = X.shape
        wf = 0.6
        if cols == 1: # Common case
            x = range(len(X[:,0]))
            self.axes.bar(x,X[:,0], width=0.6 ,align="center")
            self.axes.set_xlim(0 - wf, x[-1] + wf)
        self.canvas.draw()
        
    def OnScatter(self,event):
        setplot.set_default_params(self.axes,self.figure)
        X = self.data.grid_data.GetArrayData()
        rows,cols = X.shape
        if cols == 2: # Common case
            self.axes.plot(X[:,0],X[:,1],"bo")
        elif cols == 1:
            self.axes.plot(X[:,0],"bo")
        self.canvas.draw()
        
    def OnPie(self,event):
        setplot.set_default_params(self.axes,self.figure)
        X = self.data.grid_data.GetArrayData()
        rows,cols = X.shape
        if cols == 1:
            _ , self.pie_labels = self.axes.pie(X[:,0], labels=X[:,0])
            self.axes.set_aspect("equal")
        else:
            pass
        self.canvas.draw()
        
    def OnPieLabels(self,event):
        if hasattr(self,"pie_labels"):
            dlg = aux.PieLabelsDialog(None,self.pie_labels)
            if dlg.ShowModal() == wx.ID_OK:
                dlg.GetData()
            dlg.Destroy()
        else:
            self.sb.SetStatusText(u"Pie plots unavailables")
        self.canvas.draw()
        
    def OnImage(self,event):
        setplot.set_default_params(self.axes,self.figure)
        X = self.data.grid_data.GetArrayData()
        rows,cols = X.shape
        self.axes.imshow(X, cmap=cm.gray)
        self.canvas.draw()
        
    def OnContour(self,event):
        setplot.set_default_params(self.axes,self.figure)
        X = self.data.grid_data.GetArrayData()
        rows,cols = X.shape
        self.axes.contour(X)
        self.canvas.draw()
        
    def OnContourf(self,event):
        setplot.set_default_params(self.axes,self.figure)
        X = self.data.grid_data.GetArrayData()
        rows,cols = X.shape
        self.axes.contourf(X)
        self.canvas.draw()
        
    # Image operations ============================
    def OnSobel(self,event):
        cx = self.data.grid_data.GetArrayData()
        xmod = image.sobel(cx)
        self.data.grid_data.SetArrayData(xmod)
        
    def OnPrewitt(self,event):
        cx = self.data.grid_data.GetArrayData()
        xmod = image.prewitt(cx)
        self.data.grid_data.SetArrayData(xmod)
        
    def OnRoberts(self,event):
        cx = self.data.grid_data.GetArrayData()
        xmod = image.roberts(cx)
        self.data.grid_data.SetArrayData(xmod)
        
    def OnBinarize(self,event):
        cx = self.data.grid_data.GetArrayData()
        xmod = image.binarize(cx)
        self.data.grid_data.SetArrayData(xmod)
        
    def OnResetView(self,event):
        self.axes.autoscale()
        self.axes.set_aspect("auto")
        self.canvas.disconnect_all()
        self.canvas.draw()
        
    def OnAbout(self,event):
        aux.AboutDialog(None)


class App(wx.App):
    """
    Override OnInit
    """
    def OnInit(self):
        frame = NanchiPlot(None)
        return True

def run():
    REDIRECT = False
    LOG_FILE = "nanchi.log"
    app = App(REDIRECT)
    app.MainLoop()

if __name__=='__main__':
    run() # Run app
