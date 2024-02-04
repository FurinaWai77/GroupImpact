import sys, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import cos, sin, pi, sqrt
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))

def Yh_plotter():
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

    HPlane1 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1 + phi, 1 + 1 / phi, 1))
    HPlane2 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1 + phi, -1 - 1 / phi, 1))
    HPlane3 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1 + 1 / phi, 1, 1 + phi))
    HPlane4 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1 + 1 / phi, -1, 1 + phi))
    HPlane5 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1 + phi, 1 + 1 / phi, -1))
    HPlane6 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1 + phi, -1 - 1 / phi, -1))
    HPlane7 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1 + 1 / phi, 1, -1 - phi))
    HPlane8 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1 + 1 / phi, -1, -1 - phi))
    HPlane9 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1, 1 + phi, 1 + 1 / phi))
    HPlane10 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1, 1 + phi, -1 - 1 / phi))
    HPlane11 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(-1, 1 + phi, 1 + 1 / phi))
    HPlane12 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(-1, 1 + phi, -1 - 1 / phi))
    HPlane13 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(phi, 0, 0))
    HPlane14 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(0, phi, 0))
    HPlane15 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(0, 0, phi))
    pl.add_mesh(HPlane1, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane2, color=DefaultSettings.Plane_color2, opacity=0.7)
    """
    pl.add_mesh(HPlane3, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane4, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane5, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane6, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane7, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane8, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane9, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane10, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane11, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane12, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane13, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane14, color=DefaultSettings.Plane_color2, opacity=0.7)
    pl.add_mesh(HPlane15, color=DefaultSettings.Plane_color2, opacity=0.7)
    """

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

    pl.add_text(rf"$Y_h$ group with 15 $C_2$'s, 10 $C_3$'s, 6 $C_5$'s and $\sigma_h$", font='times', position=(0, 0.9), viewport=True,
                color='red')
    pl.add_text(rf"Brown $C_2$'s, blue $C_3$‘s, orange $C_5$'s", font='times', position=(0, 0.85),
                viewport=True,
                color='blue')
    pl.add_text(rf"Equivalently 15 reflections, perpendicular to $C_2$'s, here 2 are shown", font='times', position=(0, 0.8),
                viewport=True,
                color='purple')
    pl.add_text(rf"Reflection planes cross centers and vertices of each pentagon", font='times', position=(0, 0.75),
                viewport=True,
                color='green')


Yh_plotter()

pl.show()