# -*- coding: utf-8 -*-
import os.path as path

#
VERSION = "0.1.0-dev"
NANCHI_MAIN_CAPTION = "NanchiPlot "+VERSION

# Colors

PANEL_BG_COLOR = "#f0f0f0"
FRAME_BG_COLOR = "#aaf0f0"
AXES_BG_COLOR = "#ffffff"
FIGURE_BG_COLOR = "#ffffff"

LINE_COLOR = "#000000"
GRID_COLOR = "#99ddff"
XTICK_COLOR = "#280033"
YTICK_COLOR = "#280033"

# Captions
DEFAULT_DIALOG_CAPTION = "wxGraph 0.1.0"

# Graphics properties
LINE_STYLES = "'-' | '--' | '-.' | ':' | 'None' ".split("|")

# Icons & Images dirs
IMGS_PATH = "nanchi/img"
PATH_NANCHI_LOGO = path.join(IMGS_PATH,"nanchi_logo.png")
PATH_IMPORT_ICON = path.join(IMGS_PATH, "import_icon_32x32.png")
PATH_LOAD_IMAGE_ICON = path.join(IMGS_PATH, "load_image_icon_32x32.png")
PATH_FUNCTION_ICON = path.join(IMGS_PATH, "function_icon_32x32.png")
PATH_PLOT_ICON = path.join(IMGS_PATH, "plot_icon_32x32.png")
PATH_BAR_ICON = path.join(IMGS_PATH, "bar_icon_32x32.png")
PATH_SCATTER_ICON = path.join(IMGS_PATH, "scatter_icon_32x32.png")
PATH_PIE_ICON = path.join(IMGS_PATH, "pie_icon_32x32.png")
PATH_IMAGE_ICON = path.join(IMGS_PATH, "image_icon_32x32.png")
PATH_CONTOUR_ICON = path.join(IMGS_PATH, "contour_icon_32x32.png")
PATH_CONTOURF_ICON = path.join(IMGS_PATH, "contourf_icon_32x32.png")

# Documentation path
PATH_HTML_DOCUMENTATION = r"doc\build\html\index.html"


# Status for "Status bar"
SB_ON_INIT = "Importe o inserte datos para comenzar..."
SB_ON_IMPORT_IMAGE = "Imagen importada de %s"
SB_ON_IMPORT_IMAGE_CANCEL = "Imagen no importada..."
SB_ON_IMPORT_DATA = "Datos importados de %s"
SB_ON_IMPORT_DATA_FAIL = "Error al cargar el archivo %s"
SB_ON_CREATE_DATA_FUNCTION = "Datos definidos a partir de f(x)"


