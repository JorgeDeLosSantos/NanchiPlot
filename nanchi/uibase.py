# -*- coding: utf-8 -*-
import wx
import wx.aui as aui
import wx.grid as grid
import wx.lib.scrolledpanel as scrolled
import os
import numpy as np
import matplotlib

import matplotlib.pyplot as plt
from uimpl import FigureCanvas # Customized canvas
from matplotlib.figure import Figure

import setplot
import uimpl
import uiaux as aux
from util import isempty, rgb2hex
from _const_ import *  # String & Constants values

class NanchiNoteBook(aui.AuiNotebook):
    def __init__(self, parent):
        _styles = aui.AUI_NB_TOP | aui.AUI_NB_TAB_SPLIT | aui.AUI_NB_TAB_MOVE
        aui.AuiNotebook.__init__(self, parent=parent, style=_styles)
        
        # Graph Panel
        self.graphs = GraphPanel(self)
        self.data = DataPanel(self)
        #self.setup = SetupPanel(self)
        self.axes = self.graphs.axes
        self.figure = self.graphs.figure
        self.canvas = self.graphs.canvas
        
        self.AddPage(self.graphs, u"Graphs")
        self.AddPage(self.data, u"Data")
        #self.AddPage(self.setup, u"Settings")

        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self.OnPageChanged)

    def OnPageChanged(self, event):
        pass
        #gp = pickle.load(open("graph_properties.dat","rb"))
        #self.axes.set_xlabel(gp["xlabel"])
        #self.axes.set_ylabel(gp["ylabel"])
        #self.canvas.draw() # Draw canvas 
        

class GraphPanel(wx.Panel):
    def __init__(self,parent,*args,**kwargs):
        wx.Panel.__init__(self,parent,-1)
        # Sizer
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        
        # Init canvas Figure & Axes
        self.initCanvas()
        
        # Color properties
        self.SetBackgroundColour(PANEL_BG_COLOR)
        
        # Status bar from NanchiPlot App
        self.sb = self.GetParent().GetParent().GetParent().GetStatusBar()
        #print self.sb # debug
        
        # Configurar sizer
        self.SetSizer(self.mainsz)
        
    def initCanvas(self):
        # Creating Figure & Axes
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        
        self.EVT_ON_RIGHT = self.canvas.mpl_connect('button_press_event', self.OnRightClick)
        # Graph properties
        setplot.set_default_params(self.axes,self.figure)
        # FigureCanvas
        self.mainsz.Add(self.canvas, 1, wx.EXPAND|wx.ALL, 2)
    
    def OnRightClick(self,event):
        if event.button == 3:
            self.InitPopUpMenu()
        else:
            pass
            

    def InitPopUpMenu(self):
        pum = wx.Menu()
        
        ls = wx.Menu() # Line Style
        pum.AppendMenu(-1, u"Line style", ls)
        linecolor = wx.MenuItem(pum, -1, u"Line color")
        pum.AppendItem(linecolor)
        linewidth = wx.MenuItem(pum, -1, u"Line width")
        pum.AppendItem(linewidth)
        
        pum.AppendSeparator()
        
        gs = wx.Menu()
        pum.AppendMenu(-1, "Grid style", gs)
        gridcolor = wx.MenuItem(pum, -1, u"Grid color")
        pum.AppendItem(gridcolor)
        
        pum.AppendSeparator()
        axbackg = wx.MenuItem(pum, -1, u"Background Color")
        pum.AppendItem(axbackg)
        aspax = wx.Menu()
        _aspax_auto = wx.MenuItem(aspax, -1, u"auto")
        aspax.AppendItem(_aspax_auto)        
        _aspax_equal = wx.MenuItem(aspax, -1, u"equal")
        aspax.AppendItem(_aspax_equal)
        pum.AppendMenu(-1, "Axes aspect", aspax)
        
        pum.AppendSeparator()
        xlabel = wx.MenuItem(pum, -1, u"X-Label")
        pum.AppendItem(xlabel)
        ylabel = wx.MenuItem(pum, -1, u"Y-Label")
        pum.AppendItem(ylabel)
        title = wx.MenuItem(pum, -1, u"Insert title")
        pum.AppendItem(title)
        intext = wx.MenuItem(pum, -1, u"Insert text/annotation")
        pum.AppendItem(intext)
        
        pum.AppendSeparator()
        setxticks = wx.MenuItem(pum, -1, u"Update xticks")
        pum.AppendItem(setxticks)
        setyticks = wx.MenuItem(pum, -1, u"Update yticks")
        pum.AppendItem(setyticks)
        
        pum.AppendSeparator()
        zoom_box = wx.MenuItem(pum, -1, u"Zoom Box")
        pum.AppendItem(zoom_box)
        
        # Binds
        self.Bind(wx.EVT_MENU, self.OnText, intext)
        self.Bind(wx.EVT_MENU, self.OnBackground, axbackg)
        self.Bind(wx.EVT_MENU, self.OnGridColor, gridcolor)
        self.Bind(wx.EVT_MENU, self.OnXLabel, xlabel)
        self.Bind(wx.EVT_MENU, self.OnYLabel, ylabel)
        self.Bind(wx.EVT_MENU, self.OnTitle, title)
        self.Bind(wx.EVT_MENU, self.OnZoom, zoom_box)
        
        self.Bind(wx.EVT_MENU, self.OnAxesAspect, _aspax_equal)
        self.Bind(wx.EVT_MENU, self.OnAxesAspect, _aspax_auto)
        
        # Lines
        self.Bind(wx.EVT_MENU, self.OnLineColor, linecolor)
        self.Bind(wx.EVT_MENU, self.OnLineWidth, linewidth)
        
        # Ticks
        self.Bind(wx.EVT_MENU, self.OnXTicks, setxticks)
        self.Bind(wx.EVT_MENU, self.OnYTicks, setyticks)
        
        # Show
        self.PopupMenu(pum)
        pum.Destroy()
            
            
    def OnText(self,event):
        self.TEXT_EVT = self.canvas.mpl_connect("button_press_event", self.set_text)
        
    def set_text(self,event):
        cx = event.xdata
        cy = event.ydata
        dialog = wx.TextEntryDialog(self,"Insert text",
        NANCHI_MAIN_CAPTION, u"", style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            if not cx is None and not cy is None:
                self.axes.text(cx, cy, unicode(dialog.GetValue()), picker=True)
                self.canvas.draw()
            else:
                msg = wx.MessageDialog(self,u"Select a position inside of Axes",
                caption=DEFAULT_DIALOG_CAPTION, style=wx.ICON_ERROR|wx.OK)
                msg.ShowModal()
                msg.Destroy()
        dialog.Destroy()
        self.canvas.mpl_disconnect(self.TEXT_EVT)
        
    def OnBackground(self,event):
        dlg = wx.ColourDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            color = dlg.GetColourData().Colour
            r,g,b = color.Red(),color.Green(),color.Blue()
            self.axes.set_axis_bgcolor(rgb2hex(r,g,b))
        dlg.Destroy()
        self.canvas.draw()
        
    def OnAxesAspect(self,event):
        aspect = event.GetEventObject().GetLabel(event.GetId())
        self.axes.set_aspect(aspect)
        self.canvas.draw()
        
    def OnGridColor(self,event):
        dlg = wx.ColourDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            color = dlg.GetColourData().Colour
            r,g,b = color.Red(),color.Green(),color.Blue()
            self.axes.grid(color=rgb2hex(r,g,b))
        dlg.Destroy()
        self.canvas.draw()
        
    def OnGridStyle(self,event):
        _gs = event.GetEventObject().GetLabel(event.GetId())
        self.axes.grid(ls=_gs)
        self.canvas.draw()
        
    def OnLineColor(self,event):
        self.LINE_COLOR_EVT = self.canvas.mpl_connect("pick_event", self.set_line_color)
        
    def set_line_color(self,event):
        dlg = wx.ColourDialog(self)
        if dlg.ShowModal() == wx.ID_OK:
            color = dlg.GetColourData().Colour
            r,g,b = color.Red(),color.Green(),color.Blue()
            event.artist.set_color(rgb2hex(r,g,b))
        dlg.Destroy()
        self.canvas.draw()
        self.canvas.mpl_disconnect(self.LINE_COLOR_EVT)
        
    def OnLineStyle(self,event):
        dlg = aux.LineStyleDialog(None)
        if dlg.ShowModal() == wx.ID_OK:
            self._ls = dlg.GetData()
            self.LINE_STYLE_EVT = self.canvas.mpl_connect("pick_event", self.set_line_style)
        dlg.Destroy()
        
    def set_line_style(self,event):
        event.artist.set_linestyle(self._ls)
        self.canvas.mpl_disconnect(self.LINE_STYLE_EVT)
        self.canvas.draw()
        
    def OnLineWidth(self,event):
        self.LINE_WIDTH_EVT = self.canvas.mpl_connect("pick_event", self.set_line_width)
        
        
    def set_line_width(self,event):
        self.canvas.mpl_disconnect(self.LINE_WIDTH_EVT)
        dlg = wx.TextEntryDialog(self, u"Inserte un grosor de línea", NANCHI_MAIN_CAPTION)
        if dlg.ShowModal()==wx.ID_OK:
            _lw = float(dlg.GetValue())
            event.artist.set_linewidth(_lw)
        dlg.Destroy()
        self.canvas.draw()
        
        
    def OnXLabel(self,event):
        current_label = unicode(self.axes.get_xlabel())
        dialog = wx.TextEntryDialog(None,
        "Inserte la etiqueta en X",
        NANCHI_MAIN_CAPTION, current_label, style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            self.axes.set_xlabel(dialog.GetValue())
            self.canvas.draw()
        dialog.Destroy()
        
    def OnYLabel(self,event):
        current_label = unicode(self.axes.get_ylabel())
        dialog = wx.TextEntryDialog(self,
        "Inserte la etiqueta en Y",
        NANCHI_MAIN_CAPTION, current_label, style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            self.axes.set_ylabel(dialog.GetValue())
            self.canvas.draw()
        dialog.Destroy()
        
    def OnTitle(self,event):
        dialog = wx.TextEntryDialog(self,
        u"Inserte el título",
        NANCHI_MAIN_CAPTION, "", style=wx.OK|wx.CANCEL)
        if dialog.ShowModal() == wx.ID_OK:
            self.axes.set_title(dialog.GetValue())
            self.canvas.draw()
        dialog.Destroy()
        
    def OnXTicks(self,event):
        dlg = aux.TickDialog(self, self.axes, "x")
        if dlg.ShowModal() == wx.ID_OK:
            ticks,labels = dlg.GetData()
            self.axes.set_xticks(ticks)
            self.axes.set_xticklabels(labels)
        dlg.Destroy()
        self.canvas.draw()
        
    def OnYTicks(self,event):
        dlg = aux.TickDialog(self, self.axes, "y")
        if dlg.ShowModal() == wx.ID_OK:
            ticks,labels = dlg.GetData()
            self.axes.set_yticks(ticks)
            self.axes.set_yticklabels(labels)
            self.sb.SetStatusText(u"")
        dlg.Destroy()
        self.canvas.draw()
        
    def OnLineLabel(self,event):
        self.LINE_LABEL_EVT = self.canvas.mpl_connect("pick_event", self.set_line_label)
        
    def set_line_label(self,event):
        self.canvas.mpl_disconnect(self.LINE_LABEL_EVT)
        dlg = wx.TextEntryDialog(self, u"Insert a label", NANCHI_MAIN_CAPTION)
        if dlg.ShowModal()==wx.ID_OK:
            _label = dlg.GetValue()
            event.artist.set_label(_label)
        dlg.Destroy()
        self.canvas.draw()
        
    def OnShowLegend(self,event):
        self.axes.legend(loc="best")
        self.canvas.draw()
        
        
    def OnPieLabels(self,event):
        pass
        
    def OnZoom(self,event):
        self.sb.SetStatusText(u"Drag the cursor to select a region")
        self.canvas.zoomit()
        #~ xl = self.axes.get_xlim()
        #~ yl = self.axes.get_ylim()
        #~ self.sb.SetStatusText(u"Zoom aplicado, nueva región: (%0.4f,%0.4f,%0.4f,%0.4f)"%
                              #~ (xl[0],xl[1],yl[0],yl[1]))
        
    def OnMoveLine(self,event):
        self.MOVE_LINE_EVT = self.canvas.mpl_connect("pick_event", self.move_line)
        self.sb.SetStatusText(u"Select a line to move")
        
    def move_line(self,event):
        self._selected_line = event.artist
        self._p0 = (event.mouseevent.xdata, event.mouseevent.ydata)
        self._xdata0 = self._selected_line.get_xdata()
        self._ydata0 = self._selected_line.get_ydata()
        self._mpl_ml_motion = self.canvas.mpl_connect("motion_notify_event", self._ml_motion)
        self._mpl_ml_release = self.canvas.mpl_connect("button_release_event", self._ml_release)
    
    def _ml_motion(self,event):
        cx = event.xdata
        cy = event.ydata
        deltax = cx - self._p0[0]
        deltay = cy - self._p0[1]
        self._selected_line.set_xdata(self._xdata0 + deltax)
        self._selected_line.set_ydata(self._ydata0 + deltay)
        self.canvas.draw()
        
    def _ml_release(self,event):
        self.canvas.mpl_disconnect(self._mpl_ml_motion)
        self.canvas.mpl_disconnect(self._mpl_ml_release)
        self.canvas.mpl_disconnect(self.MOVE_LINE_EVT)
        self.axes.relim()
        self.axes.autoscale_view(True,True,True)
        self.canvas.draw()
        self.sb.SetStatusText(u"Line %s has been moved"%(self._selected_line.__repr__()))
        

    def OnMoveText(self,event):
        self.MOVE_TEXT_EVT = self.canvas.mpl_connect("pick_event", self.move_text)
        self.sb.SetStatusText(u"Select a text to move")
        
    def move_text(self,event):
        self._selected_text = event.artist
        self._mpl_mt_motion = self.canvas.mpl_connect("motion_notify_event", self._mt_motion)
        self._mpl_mt_release = self.canvas.mpl_connect("button_release_event", self._mt_release)
    
    def _mt_motion(self,event):
        cx = event.xdata
        cy = event.ydata
        self._selected_text.set_position((cx,cy))
        self.canvas.draw()
        
    def _mt_release(self,event):
        self.canvas.mpl_disconnect(self._mpl_mt_motion)
        self.canvas.mpl_disconnect(self._mpl_mt_release)
        self.canvas.mpl_disconnect(self.MOVE_TEXT_EVT)
        self.axes.relim()
        self.axes.autoscale_view(True,True,True)
        self.canvas.draw()
        self.sb.SetStatusText(u"Text %s has been moved to the position (%0.4f,%0.4f)"
                              %(self._selected_text.get_text(),
                              self._selected_text.get_position()[0],
                              self._selected_text.get_position()[1]))

class GraphWindow(wx.Frame):
    def __init__(self,parent,title,*args,**kwargs):
        wx.Frame.__init__(self,parent=parent,title=title,*args,**kwargs)
        self.SetBackgroundColour(FRAME_BG_COLOR)
        self.Centre(True)
        
        
class DataPanel(scrolled.ScrolledPanel):
    def __init__(self,parent,*args,**kwargs):
        scrolled.ScrolledPanel.__init__(self,parent,-1,size=(100,-1),
        style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER)
                
        self.initCtrls()
        self.initSizers()
        self.initEvents()
        self.SetupScrolling()
        # Color properties
        self.SetBackgroundColour(PANEL_BG_COLOR)
        
    def initCtrls(self):
        self.grid_data = DataGrid(self,(10,2))
        
    def initSizers(self):
        # Create sizers
        self.mainsz = wx.BoxSizer(wx.VERTICAL)
        # Add to sizers
        self.mainsz.Add(self.grid_data, 5, wx.EXPAND|wx.ALL, 2)

        # Set Sizers
        self.SetSizer(self.mainsz)
        
    def initEvents(self):
        pass
        

class DataGrid(grid.Grid):
    def __init__(self,parent,gridsize,**kwargs):
        grid.Grid.__init__(self,parent=parent,id=-1,**kwargs)
        rows = int(gridsize[0])
        cols = int(gridsize[1])
        self.CreateGrid(rows,cols)
        self.SetRowLabelSize(20)
        
        # Para graficar desde rejilla
        if isinstance(self.GetParent(),DataPanel):
            self.axes = self.GetParent().GetParent().graphs.axes
            self.canvas = self.GetParent().GetParent().graphs.canvas
        
        self.Bind(grid.EVT_GRID_CELL_CHANGE, self.OnCellEdit)
        self.Bind(grid.EVT_GRID_CELL_RIGHT_CLICK, self.OnRightClick)
        
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
            
    def SetArrayData(self,data):
        """
        Data must be a numpy array
        """
        r,c = data.shape # For numpy array
        self.UpdateGridSize(r,c)
        for i in range(r):
            for j in range(c):
                val = str(data[i][j])
                self.SetCellValue(i,j,val)
        
    def GetArrayData(self):
        nrows = self.GetNumberRows()
        ncols = self.GetNumberCols()
        X = np.zeros((nrows,ncols))
        for i in range(nrows):
            for j in range(ncols):
                cval = self.GetCellValue(i,j)
                if not isempty(cval):
                    try:
                        X[i][j] = float(cval)
                    except:
                        # Revisar valores devueltos
                        X[i][j] = np.nan
                else:
                    X[i][j] = np.nan
        return X
        
    def GetSelectedData(self):
        scols = self.GetSelectedCols()
        srows = self.GetSelectedRows()
        X = np.zeros((len(srows),len(scols)))
        for ii,row in enumerate(srows):
            for jj,col in enumerate(scols):
                try:
                    X[ii][jj] = self.GetCellValue(row,col)
                except ValueError:
                    X[ii][jj] = np.nan
        return X
                
        
    def GetSelectedCols(self):
        scols = []
        top_left = self.GetSelectionBlockTopLeft()
        bottom_right = self.GetSelectionBlockBottomRight()
        if not isempty(bottom_right) and not isempty(top_left):
            max_col = bottom_right[0][1]
            min_col = top_left[0][1]
            scols = range(min_col,max_col+1)
        return scols
        
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
        """
        """
        row,col = (event.GetRow(),event.GetCol())
        cval = self.GetCellValue(row,col)
        if cval.startswith("="):
            try:
                cval = str(eval(cval[1:]))
                self.SetCellValue(row,col,cval)
            except:
                pass
        try:
            cval = float(cval)
        except ValueError:
            cval = np.nan
        self.SetCellValue(row,col,str(cval))
        
            
    def OnRightClick(self,event):
        pum = wx.Menu()
        delrows = wx.MenuItem(pum, -1, "Delete rows")
        pum.AppendItem(delrows)
        delcols = wx.MenuItem(pum, -1, "Delete columns")
        pum.AppendItem(delcols)
        pum.AppendSeparator()
        addrow = wx.MenuItem(pum, -1, "Add rows...")
        pum.AppendItem(addrow)
        addcol = wx.MenuItem(pum, -1, "Add columns...")
        pum.AppendItem(addcol)
        pum.AppendSeparator()
        editcollabel = wx.MenuItem(pum, -1, "Edit column label")
        pum.AppendItem(editcollabel)
        pum.AppendSeparator()
        randomfill = wx.MenuItem(pum, -1, "Fill column randomly")
        pum.AppendItem(randomfill)
        
        # Not support for plot from data panel
        #~ pum.AppendSeparator()
        #~ plot = wx.MenuItem(pum, -1, u"Graficar líneas")
        #~ pum.AppendItem(plot)
        #~ bar = wx.MenuItem(pum, -1, u"Graficar barras")
        #~ pum.AppendItem(bar)
        
        # Binds
        pum.Bind(wx.EVT_MENU, self.del_rows, delrows)
        pum.Bind(wx.EVT_MENU, self.del_cols, delcols)
        pum.Bind(wx.EVT_MENU, self.add_row, addrow)
        pum.Bind(wx.EVT_MENU, self.add_col, addcol)
        pum.Bind(wx.EVT_MENU, self.edit_collabel, editcollabel)
        pum.Bind(wx.EVT_MENU, self.random_fill, randomfill)
        
        #~ pum.Bind(wx.EVT_MENU, self.plot, plot)
        #~ pum.Bind(wx.EVT_MENU, self.bar, bar)
        # Show 
        self.PopupMenu(pum)
        pum.Destroy()

    def del_rows(self,event):
        rows = self.GetSelectedRows()
        self.DeleteRows(rows[0],len(rows))
        
    def del_cols(self,event):
        cols = self.GetSelectedCols()
        self.DeleteCols(cols[0],len(cols))
        
    def add_row(self,event):
        self.AppendRows(1)
        
    def add_col(self,event):
        self.AppendCols(1)
        
    def edit_collabel(self,event):
        ccols = self.GetSelectedCols()
        dlg = wx.TextEntryDialog(None, "Insert new label...",
        DEFAULT_DIALOG_CAPTION)
        if dlg.ShowModal() == wx.ID_OK:
            label = dlg.GetValue()
        for col in ccols:
            self.SetColLabelValue(col,label)
    
    def random_fill(self,event):
        cols = self.GetSelectedCols()
        nrows = self.GetNumberRows()
        for ii in range(nrows):
            for col in cols:
                val = str(np.random.rand())
                self.SetCellValue(ii,col,val)
                
    def plot(self,event):
        data = self.GetSelectedData()
        self.axes.plot(data)
        self.canvas.draw()
        
    def bar(self,event):
        X = self.GetSelectedData()
        x = range(len(X[:,0]))
        self.axes.bar(x,X[:,0], width=0.6 ,align="center")
        self.canvas.draw()
        

        
if __name__=='__main__':
    app = wx.App()
    fr = GraphWindow(None,"Hi",size=(600,400))
    sz = wx.BoxSizer(wx.VERTICAL)
    dp = DataPanel(fr)
    sz.Add(dp, 1, wx.EXPAND)
    fr.SetSizer(sz)
    fr.Show()
    app.MainLoop()
