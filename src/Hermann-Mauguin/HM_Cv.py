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


def HM_Cv_plotter(n):
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
    if n==2:
        pl.add_text(rf"Hermann Mauguin symbol: mm2", font='times', position=(0.02, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Equivalent with $C_{n}v$ group", font='times', position=(0.02, 0.85), viewport=True,
                    color='blue')
        pl.add_text(rf"Here $m$ represents vertical reflection", font='times', position=(0.02, 0.8), viewport=True,
                    color='green')
        pl.add_text(rf"Principal axis $C_{n}$, 2 classes of vertical reflections (each contains 1)", font='times', position=(0.02, 0.75), viewport=True,
                    color='purple')
    elif n==3:
        pl.add_text(rf"Hermann Mauguin symbol: 3m", font='times', position=(0.02, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Equivalent with $C_{n}v$ group", font='times', position=(0.02, 0.85), viewport=True,
                    color='blue')
        pl.add_text(rf"Here $m$ represents vertical reflection", font='times', position=(0.02, 0.8), viewport=True,
                    color='green')
        pl.add_text(rf"Principal axis $C_{n}$, 1 class of vertical reflections containing 3", font='times', position=(0.02, 0.75), viewport=True,
                    color='purple')
    elif n==4:
        pl.add_text(rf"Hermann Mauguin symbol: 4mm", font='times', position=(0.02, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Equivalent with $C_{n}v$ group", font='times', position=(0.02, 0.85), viewport=True,
                    color='blue')
        pl.add_text(rf"Here $m$ represents vertical reflection", font='times', position=(0.02, 0.8), viewport=True,
                    color='green')
        pl.add_text(rf"Principal axis $C_{n}$, 2 class of vertical reflections (each containing 2)", font='times', position=(0.02, 0.75), viewport=True,
                    color='purple')
    elif n==6:
        pl.add_text(rf"Hermann Mauguin symbol: 6mm", font='times', position=(0.02, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Equivalent with $C_{n}v$ group", font='times', position=(0.02, 0.85), viewport=True,
                    color='blue')
        pl.add_text(rf"Here $m$ represents vertical reflection", font='times', position=(0.02, 0.8), viewport=True,
                    color='green')
        pl.add_text(rf"Principal axis $C_{n}$, 2 class of vertical reflections (each containing 3)", font='times', position=(0.02, 0.75), viewport=True,
                    color='purple')

HM_Cv_plotter(args.int_n)

pl.show()