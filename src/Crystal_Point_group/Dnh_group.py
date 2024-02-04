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

def Dnh_plotter_even(n):
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
    pl.add_text(rf"$D_{n}h$ group with {n} $C_2$'s, 1 $C_{n}$ and reflection $\sigma_h$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red', font_size=12)
    pl.add_text(rf"Brown line $C_2$(central symmetry)'s, black line $C_{n}$", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=12)
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0.02, 0.8),
                viewport=True,
                color='purple', font_size=12)

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
    pl.add_text(rf"$D_{n}h$ group with {n} $C_2$'s, 1 $C_{n}$ and reflection $\sigma_h$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red', font_size=12)
    pl.add_text(rf"Equivalently use reflections instead, {n} vertical reflections $\sigma_v$", font='times',
                position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=12)
    pl.add_text(rf"$n={n}$ is even, so inversion on original $D_{n}$", font='times', position=(0.02, 0.8),
                viewport=True,
                color='green', font_size=12)
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0.02, 0.75),
                viewport=True,
                color='purple', font_size=12)


def Dnh_plotter_odd(n):
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
    pl.add_text(rf"$D_{n}h$ group with {n} $C_2$'s, 1 $C_{n}$ and reflection $\sigma_h$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red', font_size=12)
    pl.add_text(rf"Brown line $C_2$(central symmetry)'s, black line $C_{n}$", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=12)
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0.02, 0.8),
                viewport=True,
                color='purple', font_size=12)

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
    pl.add_text(rf"$D_{n}h$ group with {n} $C_2$'s, 1 $C_{n}$ and reflection $\sigma_h$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red', font_size=12)
    pl.add_text(rf"Equivalently use reflections instead, {n} vertical reflections $\sigma_v$", font='times',
                position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=12)
    pl.add_text(rf"$n={n}$ is odd, so inversion on rotated $D_{2 * n}-D_{n}$", font='times', position=(0.02, 0.8),
                viewport=True,
                color='green', font_size=12)
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0.02, 0.75),
                viewport=True,
                color='purple', font_size=12)


def Dnh_plotter(n):
    if n % 2 == 0:
        Dnh_plotter_even(n)
    else:
        Dnh_plotter_odd(n)


Dnh_plotter(args.int_n)

pl.show()