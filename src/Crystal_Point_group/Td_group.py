import sys, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import sqrt, cos, sin, pi
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height),shape=(1,2))

def Td_plotter():
    pl.subplot(0, 0)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Tetra = pv.Tetrahedron(radius=r)
    PlotSettings.Ref_sphere_small(pl)
    pl.add_mesh(Tetra, color=DefaultSettings.Tetra_color, opacity=0.8)
    Points = np.array([[r, r, r], [-r, -r, r], [r, -r, -r], [-r, r, -r]]) / sqrt(3)
    Points2 = np.array([[r, -r, r], [-r, r, r], [r, r, -r], [-r, -r, -r]]) / sqrt(3)
    HPlane1 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(0, 1, 1))
    HPlane2 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(0, 1, -1))
    PlotSettings.Add_points(pl, Points, 1)
    PlotSettings.Add_points(pl, Points2, 2)
    pl.add_mesh(HPlane1, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane2, color=DefaultSettings.Plane_color2, opacity=0.5)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    PlotSettings.Opposite_line(pl, np.array([0, R, 0]), 2)
    PlotSettings.Opposite_line(pl, np.array([R, 0, 0]), 2)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), -R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), -R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([-R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)

    pl.add_text(rf"$T_d$ group with 3 $C_2$'s, 4 $C_3$'s, 6 reflections and 3$S_4$'s", font='times',
                position=(0.02, 0.9), viewport=True, color='red', font_size=10)
    pl.add_text(rf"Brown line $C_2$'s, blue line $C_3$'s", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=10)
    pl.add_text(rf"Here one pair of reflection planes are shown, similar for remainings", font='times',
                position=(0.02, 0.8),
                viewport=True,
                color='magenta', font_size=10)
    pl.add_text(rf"Reflection planes are from $C_2$'s in $O$ group", font='times', position=(0.02, 0.75),
                viewport=True,
                color='purple', font_size=10)

    pl.subplot(0, 1)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Tetra = pv.Tetrahedron(radius=r)
    PlotSettings.Ref_sphere_small(pl)
    pl.add_mesh(Tetra, color=DefaultSettings.Tetra_color, opacity=0.8)
    Points = np.array([[r, r, r], [-r, -r, r], [r, -r, -r], [-r, r, -r]]) / sqrt(3)
    Points2 = np.array([[r, -r, r], [-r, r, r], [r, r, -r], [-r, -r, -r]]) / sqrt(3)
    PlotSettings.Add_points(pl, Points, 1)
    PlotSettings.Add_points(pl, Points2, 2)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    PlotSettings.Opposite_line(pl, np.array([0, R, 0]), 2)
    PlotSettings.Opposite_line(pl, np.array([R, 0, 0]), 2)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), -R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), -R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([-R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)

    n = 4
    for i in range(n):
        vec = (sin(i * 2 * pi / n + pi / n), -cos(i * 2 * pi / n + pi / n), 0.0)
        Plane = pv.Plane(
            center=(0.75 * r * cos(i * 2 * pi / n + pi / n), 0.75 * r * sin(i * 2 * pi / n + pi / n), 0.75 * r),
            direction=vec, i_size=1.5 * r,
            j_size=1.5 * r, i_resolution=1, j_resolution=1)
        Plane2 = pv.Plane(
            center=(0.75 * r * cos(i * 2 * pi / n + pi / n), 0.75 * r * sin(i * 2 * pi / n + pi / n), -0.75 * r),
            direction=vec, i_size=1.5 * r,
            j_size=1.5 * r, i_resolution=1, j_resolution=1)
        if i % 2 == 0:
            pl.add_mesh(Plane, color=DefaultSettings.Plane_color1, opacity=0.5)
        else:
            pl.add_mesh(Plane2, color=DefaultSettings.Plane_color3, opacity=0.5)

    pl.add_text(rf"$T_d$ group with 3 $C_2$'s, 4 $C_3$'s, 6 reflections and 3$S_4$'s", font='times',
                position=(0.02, 0.9), viewport=True, color='red', font_size=10)
    pl.add_text(rf"Brown line $C_2$'s, blue line $C_3$'s", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=10)
    pl.add_text(rf"Here shown is one $S_4$ with reflection", font='times', position=(0.02, 0.8),
                viewport=True,
                color='magenta', font_size=10)
    pl.add_text(rf"$S_4$'s are from $C_4$'s in $O$ group", font='times', position=(0.02, 0.75),
                viewport=True,
                color='purple', font_size=10)

Td_plotter()

pl.show()