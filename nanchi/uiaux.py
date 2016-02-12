# -*- coding: utf-8 -*-
import wx
import wx.html as html
import webbrowser
from _const_ import *

class CustomTB(wx.ToolBar):
	def __init__(self,parent,**kwargs):
		wx.ToolBar.__init__(self,parent=parent,**kwargs)
		tbsize = (32,32)
		self.SetToolBitmapSize(tbsize)
		self.SetBackgroundColour("#ffffff")
		
		# Bitmaps
		import_bmp = wx.Bitmap(PATH_IMPORT_ICON)
		function_bmp = wx.Bitmap(PATH_FUNCTION_ICON)
		load_image_bmp = wx.Bitmap(PATH_LOAD_IMAGE_ICON)
		
		plot_bmp = wx.Bitmap(PATH_PLOT_ICON)
		bar_bmp = wx.Bitmap(PATH_BAR_ICON)
		scatter_bmp = wx.Bitmap(PATH_SCATTER_ICON)
		pie_bmp = wx.Bitmap(PATH_PIE_ICON)
		image_bmp = wx.Bitmap(PATH_IMAGE_ICON)
		contour_bmp = wx.Bitmap(PATH_CONTOUR_ICON)
		contourf_bmp = wx.Bitmap(PATH_CONTOURF_ICON)
		
		# Toolbar components
		self.import_tool = self.AddLabelTool(-1, "Importar datos...", 
		import_bmp, shortHelp="Importar datos...")
		
		self.load_image_tool = self.AddLabelTool(-1, "Importar imagen...", 
		load_image_bmp, shortHelp="Importar imagen...")
		
		self.function_tool = self.AddLabelTool(-1, "Generar datos...", 
		function_bmp, shortHelp=u"Generar datos de función...")
		
		self.AddSeparator()
		
		self.plot_tool = self.AddLabelTool(-1, u"Líneas", 
		plot_bmp, shortHelp=u"Líneas")
		
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
		

# HELP WINDOW ====================================================================

class AboutDialog(wx.Frame):
	def __init__(self,parent,*args,**kwargs):
		_styles = wx.CAPTION|wx.CLOSE_BOX
		wx.Frame.__init__(self,parent=parent,title=NANCHI_MAIN_CAPTION,
		size=(350,200), style=_styles)
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
    

#---------------------------------------------------------------------------

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


if __name__=='__main__':
	test_about()
