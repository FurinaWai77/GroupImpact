import pyvista as pv
import numpy as np
from settings import DefaultSettings


def Add_points(plotter, points, color_index):
    if color_index == 1:
        Point_color = DefaultSettings.Point_color1
    elif color_index == 2:
        Point_color = DefaultSettings.Point_color2
    elif color_index == 3:
        Point_color = DefaultSettings.Point_color3
    elif color_index == 4:
        Point_color = DefaultSettings.Point_color4
    elif color_index == 5:
        Point_color = DefaultSettings.Point_color5
    else:
        raise NameError("Invalid color index.")
    for point in points:
        Sphere = pv.Sphere(radius=DefaultSettings.Point_radius, center=tuple(point))
        _ = plotter.add_mesh(Sphere, color=Point_color, render_points_as_spheres=True)


def Opposite_line(pl, single_point, color_index):
    if color_index == 1:
        Point_color = DefaultSettings.Point_color1
        Line_color = DefaultSettings.Line_color1
    elif color_index == 2:
        Point_color = DefaultSettings.Point_color2
        Line_color = DefaultSettings.Line_color2
    elif color_index == 3:
        Point_color = DefaultSettings.Point_color3
        Line_color = DefaultSettings.Line_color3
    elif color_index == 4:
        Point_color = DefaultSettings.Point_color4
        Line_color = DefaultSettings.Line_color4
    elif color_index == 5:
        Point_color = DefaultSettings.Point_color5
        Line_color = DefaultSettings.Line_color5
    else:
        raise NameError("Invalid color index.")
    points = np.array([single_point, -single_point])
    Point_pos = tuple(single_point)
    Point_neg = tuple(-single_point)
    Line = pv.Line(Point_pos, Point_neg)
    pl.add_mesh(Line, color=Line_color, line_width=5)
    Add_points(pl, points, color_index)
    for point in points:
        Sphere = pv.Sphere(radius=DefaultSettings.Point_radius, center=tuple(point))
        _ = pl.add_mesh(Sphere, color=Point_color, render_points_as_spheres=True)


def Add_axes(plotter):
    _ = plotter.add_axes(
        line_width=5,
        cone_radius=0.6,
        shaft_length=0.7,
        tip_length=0.3,
        ambient=0.5,
        label_size=(0.4, 0.16),
    )


def Ref_sphere(pl):
    R = DefaultSettings.Ex_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    Sphere = pv.Sphere(radius=R)
    Circle_ref1 = pv.Circle(radius=R)
    Circle_ref2 = pv.Circle(radius=R).rotate_x(90, point=axes.origin, inplace=False)
    Circle_ref3 = pv.Circle(radius=R).rotate_y(90, point=axes.origin, inplace=False)
    Arc1 = pv.CircularArc([R, 0, 0], [R, 0, 0], [0, 0, 0], negative=True)
    Arc2 = pv.CircularArc([R, 0, 0], [R, 0, 0], [0, 0, 0], negative=True).rotate_x(90, point=axes.origin, inplace=False)
    Arc3 = pv.CircularArc([R, 0, 0], [R, 0, 0], [0, 0, 0], negative=True).rotate_y(90, point=axes.origin, inplace=False)
    pl.add_mesh(Sphere, color=DefaultSettings.Sphere_color, opacity=0.04)
    pl.add_mesh(Circle_ref1, color=DefaultSettings.Circle_color1, opacity=0.1)
    pl.add_mesh(Circle_ref2, color=DefaultSettings.Circle_color1, opacity=0.1)
    pl.add_mesh(Circle_ref3, color=DefaultSettings.Circle_color1, opacity=0.1)
    pl.add_mesh(Arc1, color=DefaultSettings.Arc_color1, opacity=1, line_width=3)
    pl.add_mesh(Arc2, color=DefaultSettings.Arc_color1, opacity=1, line_width=3)
    pl.add_mesh(Arc3, color=DefaultSettings.Arc_color1, opacity=1, line_width=3)


def Ref_sphere_small(pl):
    R = DefaultSettings.In_radius
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    Sphere = pv.Sphere(radius=R)
    Circle_ref1 = pv.Circle(radius=R)
    Circle_ref2 = pv.Circle(radius=R).rotate_x(90, point=axes.origin, inplace=False)
    Circle_ref3 = pv.Circle(radius=R).rotate_y(90, point=axes.origin, inplace=False)
    Arc1 = pv.CircularArc([R, 0, 0], [R, 0, 0], [0, 0, 0], negative=True)
    Arc2 = pv.CircularArc([R, 0, 0], [R, 0, 0], [0, 0, 0], negative=True).rotate_x(90, point=axes.origin, inplace=False)
    Arc3 = pv.CircularArc([R, 0, 0], [R, 0, 0], [0, 0, 0], negative=True).rotate_y(90, point=axes.origin, inplace=False)
    pl.add_mesh(Sphere, color=DefaultSettings.Sphere_color, opacity=0.1)
    pl.add_mesh(Circle_ref1, color=DefaultSettings.Circle_color2, opacity=0.1)
    pl.add_mesh(Circle_ref2, color=DefaultSettings.Circle_color2, opacity=0.1)
    pl.add_mesh(Circle_ref3, color=DefaultSettings.Circle_color2, opacity=0.1)
    pl.add_mesh(Arc1, color=DefaultSettings.Arc_color2, opacity=1, line_width=3)
    pl.add_mesh(Arc2, color=DefaultSettings.Arc_color2, opacity=1, line_width=3)
    pl.add_mesh(Arc3, color=DefaultSettings.Arc_color2, opacity=1, line_width=3)


def Mouse_Instructions(plotter, fontsize=14):
    plotter.add_text(f"Hold left mouse button to rotate with respect to mouse movements", font='times',
                position=(0.1, 0.25), viewport=True,
                color='orange', font_size=fontsize)
    plotter.add_text(f"Scroll to zoom in/out", font='times', position=(0.1, 0.22), viewport=True,
                color='orange', font_size=fontsize)
    plotter.add_text(f"Hold middle mouse button/shift+left mouse button to translate", font='times', position=(0.1, 0.19),
                viewport=True,
                color='orange', font_size=fontsize)
    plotter.add_text(f"Hold ctrl+left mouse button to fix rotation axis to your view direction", font='times',
                position=(0.1, 0.16), viewport=True,
                color='orange', font_size=fontsize)


def BasePlotSetting(pl, fontsize=14, Instruction=True):
    Ref_sphere(pl)
    Add_axes(pl)
    if Instruction:
        Mouse_Instructions(pl, fontsize=fontsize)

def pv_Setting():
    pv.global_theme.show_scalar_bar = False
    #pv.OFF_SCREEN = True