import sys, argparse, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import sqrt
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))

def O_plotter():
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

    pl.add_text(rf"$O$ group with 6 $C_2$'s , 4 $C_3$'s and 3 $C_4$'s", font='times', position=(0, 0.9), viewport=True,
                color='red')
    pl.add_text(rf"Blue $C_2$'s, orange $C_3$‘s, brown $C_4$'s", font='times', position=(0, 0.85),
                viewport=True,
                color='blue')

O_plotter()

pl.show()