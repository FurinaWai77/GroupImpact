import sys, argparse, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import cos, sin, pi
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings


screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height),shape=(1,2))

parser=argparse.ArgumentParser()
parser.add_argument('int_n',type=int,help='subscript of D_nd group')
args=parser.parse_args()

def Dnd_plotter_odd(n):
    pl.subplot(0, 0)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=n).rotate_z(-90, point=axes.origin).translate((0,0,r))
    Polygon2 = pv.Polygon(radius=1, n_sides=n).rotate_z(90, point=axes.origin).translate((0,0,-r))
    Polymulti=pv.MultiBlock([Polygon,Polygon2])
    Circle = pv.Circle(radius=1).translate((0,0,r))
    Circle2 = pv.Circle(radius=1).translate((0,0,-r))
    HPlane = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Polymulti, opacity=0.8, multi_colors=True)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(Circle2, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(HPlane, color=DefaultSettings.Plane_color1, opacity=0.9)

    for i in range(n):
        right = np.array([R * cos(i * pi / n+pi/(2*n)), R * sin(i * pi / n+pi/(2*n)), 0.0])
        PlotSettings.Opposite_line(pl,right,2)
        vec = (sin(i * 2 * pi / n), -cos(i * 2 * pi / n), 0.0)
        Plane = pv.Plane(center=(0.75 * r * cos(i * 2 * pi / n), 0.75 * r * sin(i * 2 * pi / n), 0.75 * r),
                         direction=vec, i_size=1.5 * r,
                         j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color1, opacity=0.5)
    for i in range(n):
        vec = (sin(i * 2 * pi / n+pi/n), -cos(i * 2 * pi / n+pi/n), 0.0)
        Plane2 = pv.Plane(center=(0.75 * r * cos(i * 2 * pi / n+pi/n), 0.75 * r * sin(i * 2 * pi / n+pi/n), -0.75 * r),
                          direction=vec, i_size=1.5 * r,
                          j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane2, color=DefaultSettings.Plane_color3, opacity=0.5)

    for i in range(2 * n):
        Points = np.array([[cos(i * pi / n), sin(i * pi / n), r]])
        Points2 = np.array([[cos(i * pi / n), sin(i * pi / n), -r]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points2, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 1)
    pl.add_text(rf"$D_{n}d$ group with {n} $C_2$'s, 1 $S_{2*n}$ and {n} reflections $\sigma_d$, no $\sigma_h$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red', font_size=12)
    pl.add_text(rf"Brown line $C_2$(central symmetry)'s, black line $S_{2*n}$", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=12)
    pl.add_text(rf"$n={n}$ is odd, so upper and lower polygon should be distinguished", font='times', position=(0.02, 0.8),
                viewport=True,
                color='green', font_size=12)
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0.02, 0.75),
                viewport=True,
                color='purple', font_size=12)

    pl.subplot(0, 1)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=n).rotate_z(-90, point=axes.origin).translate((0,0,r))
    Polygon2 = pv.Polygon(radius=1, n_sides=n).rotate_z(90, point=axes.origin).translate((0,0,-r))
    Polymulti=pv.MultiBlock([Polygon,Polygon2])
    Circle = pv.Circle(radius=1).translate((0,0,r))
    Circle2 = pv.Circle(radius=1).translate((0,0,-r))
    HPlane = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Polymulti, opacity=0.8, multi_colors=True)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(Circle2, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(HPlane, color=DefaultSettings.Plane_color1, opacity=0.9)

    for i in range(2 * n):
        vec = (cos(i * pi / n+pi/(2*n)), -sin(i * pi / n+pi/(2*n)), 0.0)
        Plane = pv.Plane(
            center=(0.75 * r * sin(i * pi / n+pi/(2*n)), 0.75 * r * cos(i * pi / n+pi/(2*n)), 0),
            direction=vec, i_size=3 * r,
            j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color2, opacity=0.5)
        Points = np.array([[cos(i * pi / n), sin(i * pi / n), r]])
        Points2 = np.array([[cos(i * pi / n), sin(i * pi / n), -r]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points2, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 1)
    pl.add_text(rf"$D_{n}d$ group with {n} $C_2$'s, 1 $S_{2*n}$ and 2 reflections $\sigma_d$, no $\sigma_h$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red', font_size=12)
    pl.add_text(rf"Here illustrating reflections as yellow, {n} vertical reflections $\sigma_d$", font='times',
                position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=12)
    pl.add_text(rf"$n={n}$ is odd, so upper and lower polygon should be distinguished", font='times', position=(0.02, 0.8),
                viewport=True,
                color='green', font_size=12)
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0.02, 0.75),
                viewport=True,
                color='purple', font_size=12)

def Dnd_plotter_even(n):
    pl.subplot(0, 0)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=2*n).rotate_z(-90, point=axes.origin, inplace=False)
    Circle = pv.Circle(radius=1)
    HPlane = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Polygon, color=DefaultSettings.Polygon_color, opacity=0.8)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(HPlane, color=DefaultSettings.Plane_color4, opacity=0.9)


    for i in range(2*n):
        right = np.array([R * cos(i * pi / 2/n), R * sin(i * pi / 2/n), 0.0])
        if i%2==0:
            PlotSettings.Opposite_line(pl,right,2)
        vec = (sin(i * pi / n), -cos(i * pi / n), 0.0)
        Plane = pv.Plane(center=(0.75 * r * cos(i * pi / n), 0.75 * r * sin(i *  pi / n), 0.75 * r),
                         direction=vec, i_size=1.5 * r,
                         j_size=1.5 * r, i_resolution=1, j_resolution=1)
        Plane2 = pv.Plane(center=(0.75 * r * cos(i * pi / n), 0.75 * r * sin(i * pi / n), -0.75 * r),
                          direction=vec, i_size=1.5 * r,
                          j_size=1.5 * r, i_resolution=1, j_resolution=1)
        if i%2==0:
            pl.add_mesh(Plane, color=DefaultSettings.Plane_color1, opacity=0.5)
        else:
            pl.add_mesh(Plane2, color=DefaultSettings.Plane_color3, opacity=0.5)
    for i in range(4 * n):
        Points = np.array([[cos(i * pi / (2*n)), sin(i * pi / (2*n)), 0.0]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 1)
    pl.add_text(rf"$D_{n}d$ group with {n} $C_2$'s, 1 $S_{2*n}$ and {n} reflections $\sigma_d$, no $\sigma_h$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red', font_size=12)
    pl.add_text(rf"Brown line $C_2$(central symmetry)'s, black line $S_{2*n}$", font='times', position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=12)
    pl.add_text(rf"$n={n}$ is even, so upper and lower polygon are the same", font='times', position=(0.02, 0.8),
                viewport=True,
                color='green', font_size=12)
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0.02, 0.75),
                viewport=True,
                color='purple', font_size=12)

    pl.subplot(0, 1)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    PlotSettings.BasePlotSetting(pl)
    Polygon = pv.Polygon(radius=1, n_sides=2*n).rotate_z(-90, point=axes.origin, inplace=False)
    Circle = pv.Circle(radius=1)
    HPlane = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Polygon, color=DefaultSettings.Polygon_color, opacity=0.8)
    pl.add_mesh(Circle, color=DefaultSettings.Circle_color2, opacity=0.3)
    pl.add_mesh(HPlane, color=DefaultSettings.Plane_color4, opacity=0.9)

    for i in range(2 * n):
        vec = (cos(i * pi / n + pi / (2 * n)), -sin(i * pi / n + pi / (2 * n)), 0.0)
        Plane = pv.Plane(
            center=(0.75 * r * sin(i * pi / n + pi / (2 * n)), 0.75 * r * cos(i * pi / n + pi / (2 * n)), 0),
            direction=vec, i_size=3 * r,
            j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color2, opacity=0.5)
    for i in range(4*n):
        Points = np.array([[cos(i * pi / (2*n)), sin(i * pi / (2*n)), 0.0]])
        if i % 2 == 0:
            PlotSettings.Add_points(pl, Points, 1)
        else:
            PlotSettings.Add_points(pl, Points, 3)

    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 1)
    pl.add_text(rf"$D_{n}d$ group with {n} $C_2$'s, 1 $S_{2*n}$ and 2 reflections $\sigma_d$, no $\sigma_h$", font='times',
                position=(0.02, 0.9), viewport=True,
                color='red', font_size=12)
    pl.add_text(rf"Here illustrating reflections as yellow, {n} vertical reflections $\sigma_d$", font='times',
                position=(0.02, 0.85),
                viewport=True,
                color='blue', font_size=12)
    pl.add_text(rf"$n={n}$ is even, so upper and lower polygon are the same", font='times', position=(0.02, 0.8),
                viewport=True,
                color='green', font_size=12)
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0.02, 0.75),
                viewport=True,
                color='purple', font_size=12)


def Dnd_plotter(n):
    if n % 2 == 0:
        Dnd_plotter_even(n)
    else:
        Dnd_plotter_odd(n)

Dnd_plotter(args.int_n)

pl.show()