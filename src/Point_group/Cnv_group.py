import sys, argparse, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import cos, sin, pi
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))

parser=argparse.ArgumentParser()
parser.add_argument('int_n',type=int,help='subscript of C_nv group')
args=parser.parse_args()


def Cnv_plotter(n):
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=n).rotate_z(-90, point=axes.origin, inplace=False)
    Circle = pv.Circle(radius=1)

    pl.add_mesh(Polygon, color=DefaultSettings.Polygon_color, opacity=0.8)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)

    for i in range(2*n):
        vec = (sin(i * pi / n), -cos(i * pi / n), 0.0)
        Plane = pv.Plane(center=(0.75*r* cos(i * pi / n), 0.75*r * sin(i * pi / n), 0), direction=vec, i_size=3*r,
                         j_size=1.5*r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color2, opacity=0.5)
    for i in range(2 * n):
        Points = np.array([[cos(i * pi / n), sin(i * pi / n), 0.0]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 1)
    pl.add_text(rf"$C_{n}v$ group with {n} $\sigma_v$'s and 1 $C_{n}$", font='times', position=(0.02, 0.9), viewport=True,
                color='red',font_size=12)
    pl.add_text(rf"Yellow planes are $\sigma_v$'s, black line $C_{n}$", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue',font_size=12)
    pl.add_text(rf"Note that the upper and lower zone shouldn't be distinguished", font='times', position=(0.02, 0.8), viewport=True,
                    color='purple',font_size=12)

Cnv_plotter(args.int_n)

pl.show()