# -*- coding: utf-8 -*-
import os.path as path

#
VERSION = "0.1.0-dev"
NANCHI_MAIN_CAPTION = "NanchiPlot %s"%(VERSION)

# Colors
PANEL_BG_COLOR = "#ababab"
FRAME_BG_COLOR = "#aaf0f0"
AXES_BG_COLOR = "#efefef"
FIGURE_BG_COLOR = "#fafafa"

LINE_COLOR = "#000000"
GRID_COLOR = "#080808"
XTICK_COLOR = "#101635"
YTICK_COLOR = "#101635"

# Font sizes
TICK_LABEL_SIZE = 10


# Captions
DEFAULT_DIALOG_CAPTION = NANCHI_MAIN_CAPTION

# Graphics properties
LINE_STYLES = "'-' | '--' | '-.' | ':' | 'None' ".split("|")

# Icons & Images dirs
IMGS_PATH = "nanchi/img"
PATH_NANCHI_LOGO = path.join(IMGS_PATH,"nanchi_logo.png")
PATH_IMPORT_ICON = path.join(IMGS_PATH, "import_icon_32x32.png")
PATH_LOAD_IMAGE_ICON = path.join(IMGS_PATH, "load_image_icon_32x32.png")
PATH_FUNCTION_ICON = path.join(IMGS_PATH, "function_icon_32x32.png")
PATH_BIVARIABLE_FUNCTION_ICON = path.join(IMGS_PATH, "bivariable_function_icon_32x32.png")
PATH_PLOT_ICON = path.join(IMGS_PATH, "plot_icon_32x32.png")
PATH_POLAR_ICON = path.join(IMGS_PATH, "polar_icon_32x32.png")
PATH_BAR_ICON = path.join(IMGS_PATH, "bar_icon_32x32.png")
PATH_SCATTER_ICON = path.join(IMGS_PATH, "scatter_icon_32x32.png")
PATH_PIE_ICON = path.join(IMGS_PATH, "pie_icon_32x32.png")
PATH_IMAGE_ICON = path.join(IMGS_PATH, "image_icon_32x32.png")
PATH_CONTOUR_ICON = path.join(IMGS_PATH, "contour_icon_32x32.png")
PATH_CONTOURF_ICON = path.join(IMGS_PATH, "contourf_icon_32x32.png")


PATH_ZOOM_BOX_ICON = path.join(IMGS_PATH, "zoom_box_icon_24x24.png")
PATH_RESET_VIEW_ICON = path.join(IMGS_PATH, "reset_view_icon_24x24.png")
PATH_GRID_STYLE_ICON = path.join(IMGS_PATH, "grid_style_icon_24x24.png")
PATH_GRID_COLOR_ICON = path.join(IMGS_PATH, "grid_color_icon_24x24.png")
PATH_LINE_STYLE_ICON = path.join(IMGS_PATH, "line_style_icon_24x24.png")
PATH_LINE_COLOR_ICON = path.join(IMGS_PATH, "line_color_icon_24x24.png")
PATH_TEXT_ICON = path.join(IMGS_PATH, "text_icon_24x24.png")


# Documentation path
PATH_HTML_DOCUMENTATION = r"docs\build\html\index.html"

# Status for "Status bar"
SB_ON_INIT = "Importe o inserte datos para comenzar..."
SB_ON_IMPORT_IMAGE = "Imagen importada de %s"
SB_ON_IMPORT_IMAGE_CANCEL = "Imagen no importada..."
SB_ON_IMPORT_DATA = "Datos importados de %s"
SB_ON_IMPORT_DATA_FAIL = "Error al cargar el archivo %s"
SB_ON_CREATE_DATA_FUNCTION = "Datos definidos a partir de f(x)"
SB_ON_CREATE_DATA_BIVARIABLE_FUNCTION = "Datos definidos a partir de f(x,y)"


