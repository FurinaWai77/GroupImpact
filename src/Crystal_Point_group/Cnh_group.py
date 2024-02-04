import sys, argparse, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import cos, sin, pi
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))

parser=argparse.ArgumentParser()
parser.add_argument('int_n',type=int,help='subscript of C_n group')
args=parser.parse_args()

def Cnh_plotter(n):
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Cylinder = pv.Cylinder(radius=r, height=2*r, direction=(0.0, 0.0, 1.0))
    Arrow = pv.Arrow(start=(r, 2*r, 0), direction=(1, -1, 0), scale=2)
    HPlane=pv.Plane(i_size=1.3*R,j_size=1.3*R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Cylinder, color=DefaultSettings.Cylinder_color, opacity=0.8)
    pl.add_mesh(Arrow, color=DefaultSettings.Arrow_color)
    pl.add_mesh(HPlane,color=DefaultSettings.Plane_color3,opacity=0.9)

    for i in range(n):
        vec = (cos(i * 2 * pi / n), -sin(i * 2 * pi / n), 0.0)
        Plane = pv.Plane(center=(0.75*r* sin(i * 2 * pi / n), 0.75*r * cos(i * 2 * pi / n), 0.75), direction=vec, i_size=1.5*r,
                         j_size=1.5*r, i_resolution=1, j_resolution=1)
        Plane2 = pv.Plane(center=(0.75 * r * sin(i * 2 * pi / n), 0.75 * r * cos(i * 2 * pi / n), -0.75),
                              direction=vec, i_size=1.5 * r,
                              j_size=1.5 * r, i_resolution=1, j_resolution=1)
        pl.add_mesh(Plane, color=DefaultSettings.Plane_color1, opacity=0.5)
        pl.add_mesh(Plane2, color=DefaultSettings.Plane_color3, opacity=0.5)

    PlotSettings.Opposite_line(pl, np.array([0, 0, r]), 2)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 1)
    pl.add_text(rf"$C_{n}h$ group", font='times', position=(0, 0.9), viewport=True, color='red')
    pl.add_text(rf"Here $h$ represents horizontal reflection", font='times', position=(0, 0.85), viewport=True,
                    color='green')
    pl.add_text(rf"Note that the upper and lower zone should be distinguished", font='times', position=(0, 0.8), viewport=True,
                    color='purple')

Cnh_plotter(args.int_n)

pl.show()