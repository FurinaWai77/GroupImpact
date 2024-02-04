import sys, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import sqrt
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))


def Y_plotter():
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Dod = pv.Dodecahedron(radius=r)
    Ico = pv.Icosahedron(radius=r)
    PlotSettings.Ref_sphere_small(pl)
    pl.add_mesh(Dod, color=DefaultSettings.Dod_color, opacity=0.9)
    pl.add_mesh(Ico, color=DefaultSettings.Ico_color, opacity=0.4)
    phi = (sqrt(5) + 1) / 2
    Points = np.array(
        [[1, 1, 1], [1, 1, -1], [1, -1, 1], [-1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1],
         [0, phi, 1 / phi], [0, -phi, 1 / phi], [0, phi, -1 / phi], [0, -phi, -1 / phi],
         [1 / phi, 0, phi], [1 / phi, 0, -phi], [-1 / phi, 0, phi], [-1 / phi, 0, -phi],
         [phi, 1 / phi, 0], [phi, -1 / phi, 0], [-phi, 1 / phi, 0], [-phi, -1 / phi, 0]
         ]) / sqrt(3)
    PlotSettings.Add_points(pl, Points, 1)
    Points = np.array(
        [[2 * phi + 1 / phi + 2, 0, phi + 2], [2 * phi + 1 / phi + 2, 0, -phi - 2],
         [phi + 2, 2 * phi + 1 / phi + 2, 0], [-phi - 2, 2 * phi + 1 / phi + 2, 0],
         [0, phi + 2, 2 * phi + 1 / phi + 2], [0, -phi - 2, 2 * phi + 1 / phi + 2]
         ]) / sqrt(5 * (4 * phi + 3)) * r
    PlotSettings.Add_points(pl, Points, 5)

    PlotSettings.Opposite_line(pl, np.array([1 + phi, 1 + 1 / phi, 1]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1 + phi, -1 - 1 / phi, 1]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1 + 1 / phi, 1, 1 + phi]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1 + 1 / phi, -1, 1 + phi]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1 + phi, 1 + 1 / phi, -1]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1 + phi, -1 - 1 / phi, -1]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1 + 1 / phi, 1, -1 - phi]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1 + 1 / phi, -1, -1 - phi]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1, 1 + phi, 1 + 1 / phi]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([1, 1 + phi, -1 - 1 / phi]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([-1, 1 + phi, 1 + 1 / phi]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([-1, 1 + phi, -1 - 1 / phi]) * R / 2 / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([phi, 0, 0]) * R / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([0, phi, 0]) * R / sqrt(1 + phi), 2)
    PlotSettings.Opposite_line(pl, np.array([0, 0, phi]) * R / sqrt(1 + phi), 2)

    PlotSettings.Opposite_line(pl, np.array([phi, 1 / phi, 0]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([phi, -1 / phi, 0]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([1, 1, 1]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([1, -1, 1]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([1, 1, -1]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([1, -1, -1]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([1 / phi, 0, phi]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([1 / phi, 0, -phi]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([0, phi, 1 / phi]) * R / sqrt(3), 3)
    PlotSettings.Opposite_line(pl, np.array([0, phi, -1 / phi]) * R / sqrt(3), 3)

    PlotSettings.Opposite_line(pl, np.array([2 * phi + 1 / phi + 2, 0, phi + 2]) / sqrt(5 * (4 * phi + 3)) * R, 4)
    PlotSettings.Opposite_line(pl, np.array([2 * phi + 1 / phi + 2, 0, -phi - 2]) / sqrt(5 * (4 * phi + 3)) * R, 4)
    PlotSettings.Opposite_line(pl, np.array([phi + 2, 2 * phi + 1 / phi + 2, 0]) / sqrt(5 * (4 * phi + 3)) * R, 4)
    PlotSettings.Opposite_line(pl, np.array([-phi - 2, 2 * phi + 1 / phi + 2, 0]) / sqrt(5 * (4 * phi + 3)) * R, 4)
    PlotSettings.Opposite_line(pl, np.array([0, phi + 2, 2 * phi + 1 / phi + 2]) / sqrt(5 * (4 * phi + 3)) * R, 4)
    PlotSettings.Opposite_line(pl, np.array([0, -phi - 2, 2 * phi + 1 / phi + 2]) / sqrt(5 * (4 * phi + 3)) * R, 4)

    pl.add_text(rf"$Y$ group with 15 $C_2$'s, 10 $C_3$'s and 6 $C_5$'s", font='times', position=(0, 0.9), viewport=True,
                color='red')
    pl.add_text(rf"Brown $C_2$'s, blue $C_3$‘s, orange $C_5$'s", font='times', position=(0, 0.85),
                viewport=True,
                color='blue')

Y_plotter()

pl.show()