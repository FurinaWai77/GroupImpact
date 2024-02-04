import sys, argparse, pyvista as pv, numpy as np,pyautogui
sys.path.insert(0,r"../../")
from math import cos, sin, pi
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))

parser=argparse.ArgumentParser()
parser.add_argument('int_n',type=int,help='subscript of D_n group')
args=parser.parse_args()

def HM_D_plotter(n):
    R = DefaultSettings.Ex_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=n).rotate_z(-90, point=axes.origin, inplace=False)
    Line = pv.Line((0, 0, -R), (0, 0, R))
    Circle = pv.Circle(radius=1)

    pl.add_mesh(Polygon, color=DefaultSettings.Polygon_color, opacity=0.8)
    pl.add_mesh(Line, color=DefaultSettings.Line_color1, line_width=5)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)

    for i in range(n):
        right = (R * cos(i * pi / n), R * sin(i * pi / n), 0.0)
        left = (-R * cos(i * pi / n), -R * sin(i * pi / n), 0.0)
        Line = pv.Line(right, left)
        pl.add_mesh(Line, color=DefaultSettings.Line_color2, opacity=1, line_width=5)
        Points = np.array(
            [[R * cos(i * pi / n), R * sin(i * pi / n), 0.0], [-R * cos(i * pi / n), -R * sin(i * pi / n), 0.0]])
        PlotSettings.Add_points(pl, Points, 2)
    for i in range(2 * n):
        Points = np.array([[cos(i * pi / n), sin(i * pi / n), 0.0]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    if n==3:
        pl.add_text(rf"Hermann-Mauguin symbol: 32", font='times', position=(0, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Equivalent with $D_{n}$ group", font='times', position=(0, 0.85), viewport=True,
                color='blue')
        pl.add_text(rf"Principal $C_n$, 1 class of $C_2$'s related to $C_n$", font='times', position=(0, 0.8), viewport=True,
                color='green')
    else :
        pl.add_text(rf"Hermann-Mauguin symbol: {n}22", font='times', position=(0, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Equivalent with $D_{n}$ group", font='times', position=(0, 0.85), viewport=True,
                color='blue')
        pl.add_text(rf"Principal $C_n$, 2 classes of $C_2$'s related to $C_n$", font='times', position=(0, 0.8), viewport=True,
                color='green')



HM_D_plotter(args.int_n)

pl.show()