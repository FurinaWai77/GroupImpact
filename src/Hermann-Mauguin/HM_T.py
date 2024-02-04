import sys, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import sqrt
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))


def HM_T_plotter():
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Tetra = pv.Tetrahedron(radius=r)
    PlotSettings.Ref_sphere_small(pl)
    pl.add_mesh(Tetra, color=DefaultSettings.Tetra_color, opacity=0.8)
    Points = np.array([[r, r, r], [-r, -r, r], [r, -r, -r], [-r, r, -r]]) / sqrt(3)
    PlotSettings.Add_points(pl, Points, 1)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    PlotSettings.Opposite_line(pl, np.array([0, R, 0]), 2)
    PlotSettings.Opposite_line(pl, np.array([R, 0, 0]), 2)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), -R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), -R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([-R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)

    pl.add_text(rf"Hermann-Mauguin symbol: 23", font='times', position=(0, 0.9), viewport=True, color='red')
    pl.add_text(rf"Equivalent with T group", font='times', position=(0, 0.85),
                viewport=True,
                color='blue')
    pl.add_text(rf"Principal axes $C_2$'s, 1 class of $C_3$'s related to $C_2$'s", font='times', position=(0, 0.8),
                viewport=True,
                color='green')

HM_T_plotter()

pl.show()