import sys, argparse, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import cos, sin, pi
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings


screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height),shape=(1,2))

parser=argparse.ArgumentParser()
parser.add_argument('int_n',type=int,help='subscript of D_nh group')
args=parser.parse_args()

def HM_Dh_plotter_even(n):
    pl.subplot(0, 0)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=n).rotate_z(-90, point=axes.origin, inplace=False)
    Circle = pv.Circle(radius=1)
    HPlane = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Polygon, color=DefaultSettings.Polygon_color, opacity=0.8)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(HPlane, color=DefaultSettings.Plane_color2, opacity=0.9)

    for i in range(n):
        right = np.array([R * cos(i * pi / n), R * sin(i * pi / n), 0.0])
        PlotSettings.Opposite_line(pl, right, 2)
        vec = (sin(i * 2 * pi / n), -cos(i * 2 * pi / n), 0.0)
        Plane = pv.Plane(center=(0.75 * r * cos(i * 2 * pi / n), 0.75 * r * sin(i * 2 * pi / n), 0.75 * r),
                         direction=vec, i_size=1.5 * r,
                         j_size=1.5 * r, i_resolution=1, j_resolution=1)
        Plane2 = pv.Plane(center=(0.75 * r * cos(i * 2 * pi / n), 0.75 * r * sin(i * 2 * pi / n), -0.75 * r),
                          direction=vec, i_size=1.5 * r,
                          j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color1, opacity=0.5)
        pl.add_mesh(Plane2, color=DefaultSettings.Plane_color3, opacity=0.5)
    for i in range(2 * n):
        Points = np.array([[cos(i * pi / n), sin(i * pi / n), 0.0]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)


    pl.subplot(0, 1)
    R = DefaultSettings.Ex_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=n).rotate_z(-90, point=axes.origin, inplace=False)
    Line = pv.Line((0, 0, -R), (0, 0, R))
    Circle = pv.Circle(radius=1)
    HPlane = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Polygon, color=DefaultSettings.Polygon_color, opacity=0.8)
    pl.add_mesh(Line, color=DefaultSettings.Line_color1, line_width=5)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(HPlane, color=DefaultSettings.Plane_color2, opacity=0.9)

    for i in range(2 * n):
        vec = (cos(i * pi / n), -sin(i * pi / n), 0.0)
        Plane = pv.Plane(center=(0.75 * r * sin(i * pi / n), 0.75 * r * cos(i * pi / n), 0), direction=vec,
                         i_size=3 * r,
                         j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color2, opacity=0.5)
        Points = np.array([[cos(i * pi / n), sin(i * pi / n), 0.0]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    if n==2:
        pl.add_text(rf"Hermann-Mauguin symbol: 2/m 2/m 2/m", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Here m represents reflection, 2 vertical 1 horizontal, '/' represents perpendicular(perp)", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue')
        pl.add_text(rf"3 $C_2$'s perp to reflections, belonging to different classes", font='times', position=(0.02, 0.8),
                viewport=True,
                color='purple')
    elif n==4:
        pl.add_text(rf"Hermann-Mauguin symbol: 4/m m m", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Here m represents reflection, 4 vertical 1 horizontal, '/' represents perpendicular", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue')
        pl.add_text(rf"1 $C_4$ perp to horizontal reflection, 4 $C_2$'s perp to vertical reflection, belonging to 2 classes", font='times', position=(0.02, 0.8),
                viewport=True,
                color='purple')
    elif n==6:
        pl.add_text(rf"Hermann-Mauguin symbol: 6/m 2/m 2/m", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Here m represents vertical reflection, 6 vertical 1 horizontal, '/' represents perpendicular", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue')
        pl.add_text(rf"1 $C_6$ perp to horizontal reflection, 6 $C_2$'s perp to vertical reflection, belonging to 2 classes", font='times', position=(0.02, 0.8),
                viewport=True,
                color='purple')


def HM_Dh_plotter_odd(n):
    pl.subplot(0, 0)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=n).rotate_z(-90, point=axes.origin, inplace=False)
    Line = pv.Line((0, 0, -R), (0, 0, R))
    Circle = pv.Circle(radius=1)
    HPlane = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Polygon, color=DefaultSettings.Polygon_color, opacity=0.8)
    pl.add_mesh(Line, color=DefaultSettings.Line_color1, line_width=5)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(HPlane, color=DefaultSettings.Plane_color2, opacity=0.9)

    for i in range(n):
        right = np.array([R * cos(i * pi / n), R * sin(i * pi / n), 0.0])
        PlotSettings.Opposite_line(pl, right, 2)
        vec = (sin(i * 2 * pi / n), -cos(i * 2 * pi / n), 0.0)
        Plane = pv.Plane(center=(0.75 * r * cos(i * 2 * pi / n), 0.75 * r * sin(i * 2 * pi / n), 0.75 * r),
                         direction=vec, i_size=1.5 * r,
                         j_size=1.5 * r, i_resolution=1, j_resolution=1)
        Plane2 = pv.Plane(center=(0.75 * r * cos(i * 2 * pi / n), 0.75 * r * sin(i * 2 * pi / n), -0.75 * r),
                          direction=vec, i_size=1.5 * r,
                          j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color1, opacity=0.5)
        pl.add_mesh(Plane2, color=DefaultSettings.Plane_color3, opacity=0.5)
    for i in range(2 * n):
        Points = np.array([[cos(i * pi / n), sin(i * pi / n), 0.0]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)

    pl.subplot(0, 1)
    R = DefaultSettings.Ex_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=n).rotate_z(-90, point=axes.origin, inplace=False)
    Line = pv.Line((0, 0, -R), (0, 0, R))
    Circle = pv.Circle(radius=1)
    HPlane = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Polygon, color=DefaultSettings.Polygon_color, opacity=0.8)
    pl.add_mesh(Line, color=DefaultSettings.Line_color1, line_width=5)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(HPlane, color=DefaultSettings.Plane_color2, opacity=0.9)

    for i in range(2 * n):
        vec = (cos(i * pi / n + pi / (2 * n)), -sin(i * pi / n + pi / (2 * n)), 0.0)
        Plane = pv.Plane(
            center=(0.75 * r * sin(i * pi / n + pi / (2 * n)), 0.75 * r * cos(i * pi / n + pi / (2 * n)), 0),
            direction=vec, i_size=3 * r,
            j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color2, opacity=0.5)
        Points = np.array([[cos(i * pi / n), sin(i * pi / n), 0.0]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    if n==3:
        pl.add_text(rf"Hermann-Mauguin symbol: $\bar 6m2$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red')
        pl.add_text(rf"Here m represents horizontal reflection", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue')
        pl.add_text(rf"Principal $\bar 6$, 3 $C_2$'s in 1 class", font='times', position=(0.02, 0.8),
                viewport=True,
                color='purple')


def HM_Dh_plotter(n):
    if n % 2 == 0:
        HM_Dh_plotter_even(n)
    else:
        HM_Dh_plotter_odd(n)

HM_Dh_plotter(args.int_n)

pl.show()