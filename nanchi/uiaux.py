# -*- coding: utf-8 -*-
import wx

#~ class TestToolBar(wx.Frame):
    #~ def __init__(self, parent, log):
        #~ wx.Frame.__init__(self, parent, -1, 'Test ToolBar', size=(600, 400))
        #~ self.log = log
        #~ self.timer = None
        #~ self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
#~ 
        #~ client = wx.Panel(self)
        #~ client.SetBackgroundColour(wx.NamedColour("WHITE"))
#~ 
        #~ if FRAMETB:
            #~ # Use the wxFrame internals to create the toolbar and
            #~ # associate it all in one tidy method call.  By using
            #~ # CreateToolBar or SetToolBar the "client area" of the
            #~ # frame will be adjusted to exclude the toolbar.
            #~ tb = self.CreateToolBar( TBFLAGS )
#~ 
            #~ # Here's a 'simple' toolbar example, and how to bind it using SetToolBar()
            #~ #tb = wx.ToolBarSimple(self, -1, wx.DefaultPosition, wx.DefaultSize,
            #~ #               wx.TB_HORIZONTAL | wx.NO_BORDER | wx.TB_FLAT)
            #~ #self.SetToolBar(tb)
            #~ # But we're doing it a different way here.
#~ 
        #~ else:
            #~ # The toolbar can also be a child of another widget, and
            #~ # be managed by a sizer, although there may be some
            #~ # implications of doing this on some platforms.
            #~ tb = wx.ToolBar(client, style=TBFLAGS)
            #~ sizer = wx.BoxSizer(wx.VERTICAL)
            #~ sizer.Add(tb, 0, wx.EXPAND)
            #~ client.SetSizer(sizer)
            #~ 
#~ 
        #~ log.write("Default toolbar tool size: %s\n" % tb.GetToolBitmapSize())
#~ 
        #~ self.CreateStatusBar()
#~ 
        #~ tsize = (32,32)
        #~ import_bmp = wx.Bitmap("img/import_icon_32x32.png")
#~ 
        #~ tb.SetToolBitmapSize(tsize)
        #~ 
        #~ #tb.AddSimpleTool(10, new_bmp, "New", "Long help for 'New'")
        #~ tb.AddLabelTool(10, "New", new_bmp, shortHelp="New", longHelp="Long help for 'New'")
        #~ self.Bind(wx.EVT_TOOL, self.OnToolClick, id=10)
        #~ self.Bind(wx.EVT_TOOL_RCLICKED, self.OnToolRClick, id=10)
#~ 
        #~ #tb.AddSimpleTool(20, open_bmp, "Open", "Long help for 'Open'")
        #~ tb.AddLabelTool(20, "Open", open_bmp, shortHelp="Open", longHelp="Long help for 'Open'")
        #~ self.Bind(wx.EVT_TOOL, self.OnToolClick, id=20)
        #~ self.Bind(wx.EVT_TOOL_RCLICKED, self.OnToolRClick, id=20)
#~ 
        #~ tb.AddSeparator()
        #~ tb.AddSimpleTool(30, copy_bmp, "Copy", "Long help for 'Copy'")
        #~ self.Bind(wx.EVT_TOOL, self.OnToolClick, id=30)
        #~ self.Bind(wx.EVT_TOOL_RCLICKED, self.OnToolRClick, id=30)
#~ 
        #~ tb.AddSimpleTool(40, paste_bmp, "Paste", "Long help for 'Paste'")
        #~ self.Bind(wx.EVT_TOOL, self.OnToolClick, id=40)
        #~ self.Bind(wx.EVT_TOOL_RCLICKED, self.OnToolRClick, id=40)
#~ 
        #~ tb.AddSeparator()
#~ 
        #~ #tool = tb.AddCheckTool(50, images.Tog1.GetBitmap(), shortHelp="Toggle this")
        #~ tool = tb.AddCheckLabelTool(50, "Checkable", images.Tog1.GetBitmap(),
                                    #~ shortHelp="Toggle this")
        #~ self.Bind(wx.EVT_TOOL, self.OnToolClick, id=50)
#~ 
        #~ self.Bind(wx.EVT_TOOL_ENTER, self.OnToolEnter)
        #~ self.Bind(wx.EVT_TOOL_RCLICKED, self.OnToolRClick) # Match all
        #~ self.Bind(wx.EVT_TIMER, self.OnClearSB)
#~ 
        #~ tb.AddSeparator()
        #~ cbID = wx.NewId()
#~ 
        #~ tb.AddControl(
            #~ wx.ComboBox(
                #~ tb, cbID, "", choices=["", "This", "is a", "wx.ComboBox"],
                #~ size=(150,-1), style=wx.CB_DROPDOWN
                #~ ))
        #~ self.Bind(wx.EVT_COMBOBOX, self.OnCombo, id=cbID)
#~ 
        #~ tb.AddStretchableSpace()
        #~ search = TestSearchCtrl(tb, size=(150,-1), doSearch=self.DoSearch)
        #~ tb.AddControl(search)
#~ 
        #~ # Final thing to do for a toolbar is call the Realize() method. This
        #~ # causes it to render (more or less, that is).
        #~ tb.Realize()
#~ 
#~ 
    #~ def DoSearch(self,  text):
        #~ # called by TestSearchCtrl
        #~ self.log.WriteText("DoSearch: %s\n" % text)
        #~ # return true to tell the search ctrl to remember the text
        #~ return True
    #~ 
#~ 
    #~ def OnToolClick(self, event):
        #~ self.log.WriteText("tool %s clicked\n" % event.GetId())
        #~ #tb = self.GetToolBar()
        #~ tb = event.GetEventObject()
        #~ tb.EnableTool(10, not tb.GetToolEnabled(10))
#~ 
    #~ def OnToolRClick(self, event):
        #~ self.log.WriteText("tool %s right-clicked\n" % event.GetId())
#~ 
    #~ def OnCombo(self, event):
        #~ self.log.WriteText("combobox item selected: %s\n" % event.GetString())
#~ 
    #~ def OnToolEnter(self, event):
        #~ self.log.WriteText('OnToolEnter: %s, %s\n' % (event.GetId(), event.GetInt()))
#~ 
        #~ if self.timer is None:
            #~ self.timer = wx.Timer(self)
#~ 
        #~ if self.timer.IsRunning():
            #~ self.timer.Stop()
#~ 
        #~ self.timer.Start(2000)
        #~ event.Skip()
#~ 
#~ 
    #~ def OnClearSB(self, event):  # called for the timer event handler
        #~ self.SetStatusText("")
        #~ self.timer.Stop()
        #~ self.timer = None
#~ 
#~ 
    #~ def OnCloseWindow(self, event):
        #~ if self.timer is not None:
            #~ self.timer.Stop()
            #~ self.timer = None
        #~ self.Destroy()


class CustomTB(wx.ToolBar):
	def __init__(self,parent,**kwargs):
		wx.ToolBar.__init__(self,parent=parent,**kwargs)
		tbsize = (32,32)
		self.SetToolBitmapSize(tbsize)
		self.SetBackgroundColour("#ffffff")
		
		# Bitmaps
		import_bmp = wx.Bitmap("nanchi/img/import_icon_32x32.png")
		function_bmp = wx.Bitmap("nanchi/img/function_icon_32x32.png")
		load_image_bmp = wx.Bitmap("nanchi/img/load_image_icon_32x32.png")
		
		plot_bmp = wx.Bitmap("nanchi/img/plot_icon_32x32.png")
		bar_bmp = wx.Bitmap("nanchi/img/bar_icon_32x32.png")
		scatter_bmp = wx.Bitmap("nanchi/img/scatter_icon_32x32.png")
		pie_bmp = wx.Bitmap("nanchi/img/pie_icon_32x32.png")
		image_bmp = wx.Bitmap("nanchi/img/image_icon_32x32.png")
		
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
		


if __name__=='__main__':
	app = wx.App()
	fr = wx.Frame(None, -1, "Hi !!!", size=(800,600))
	sz = wx.BoxSizer(wx.VERTICAL)
	tb = CustomTB(fr)
	sz.Add(tb, 0, wx.EXPAND)
	fr.SetSizer(sz)
	tb.Realize()
	fr.Show()
	app.MainLoop()
	
