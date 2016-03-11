La interfaz de NanchiPlot
=========================

Descripción general
-------------------

La idea al desarrollar NanchiPlot es tener un interfaz sencilla que permita agilizar el proceso de graficado mediante 
utilidades accesibles a través de íconos dispuestos en las barras de herramientas.

Se pueden distinguir cinco componentes fundamentales en la interfaz inicial, a saber:

* Área de gráficos
* Área de datos
* Barra de menú
* Barra de operaciones
* Barra del axes

Enseguida se describirá cada uno de los componentes y las funciones que desempeñan dentro del flujo de trabajo de NanchiPlot.


Área de gráficos
----------------

El **Área de gráficos** es la parte de NanchiPlot en donde se trazan y muestran todas las gráficas/imágenes. Junto con el **Área de 
datos** conforman el *Notebook* principal, de modo que pueden distribuirse estas dos áreas de manera conveniente para el usuario, 
arrastrando cualesquiera de las dos áreas hasta conseguir un *layout* que se ajuste a sus preferencias.

El área de gráficos está compuesta por tres elementos fundamentales:

* Canvas
* Figure
* Axes

Los tres componentes anteriores son heredados de Matplotlib, con wxPython como backend, por lo cual, si desea documentarse más 
acerca de dichos elementos puede hacerlo en la documentación de Matplotlib. De manera resumida, el Canvas es el área principal 
u objeto padre que contiene a los otros gráficos, Figure es de igual forma un objeto de Matplotlib que sirve para contener 
a los Axes, y este último es, en cierto modo, el componente fundamental, en el cual se *dibujan* todas las gráficas en NanchiPlot.

En el caso de NanchiPlot solamente el Axes puede modificarse a través de las opciones disponibles en la **Barra del axes**, 
permitiendo la modificación de los colores de fondo, la grilla, las etiquetas y otros componentes esenciales.
