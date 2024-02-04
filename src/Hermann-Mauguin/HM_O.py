import sys, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import sqrt
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))

def HM_O_plotter():
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Oct = pv.Octahedron(radius=r)
    PlotSettings.Ref_sphere_small(pl)
    Points = np.array([[r / sqrt(2), r / sqrt(2), 0], [r / sqrt(2), -r / sqrt(2), 0], [-r / sqrt(2), r / sqrt(2), 0],
                       [-r / sqrt(2), -r / sqrt(2), 0], [0, 0, r], [0, 0, -r]])
    PlotSettings.Add_points(pl, Points, 1)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    PlotSettings.Opposite_line(pl, np.array([R, R, 0])/sqrt(2), 2)
    PlotSettings.Opposite_line(pl, np.array([R, -R, 0])/sqrt(2), 2)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), -R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), -R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([-R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([sqrt(2) * R / sqrt(3), 0, R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([sqrt(2) * R / sqrt(3), 0, -R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([0, sqrt(2) * R / sqrt(3), R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([0, sqrt(2) * R / sqrt(3), -R / sqrt(3)]), 4)
    pl.add_mesh(Oct, color=DefaultSettings.Tetra_color, opacity=0.8)

    pl.add_text(rf"Hermann-Mauguin symbol: 432", font='times', position=(0, 0.9), viewport=True,
                color='red')
    pl.add_text(rf"Equivalent with O group", font='times', position=(0, 0.85),
                viewport=True,
                color='blue')
    pl.add_text(rf"Principal axes $C_4$'s, 1 class of $C_3$'s and 1 class of $C_2$'s", font='times', position=(0, 0.8),
                viewport=True,
                color='green')

HM_O_plotter()

pl.show()