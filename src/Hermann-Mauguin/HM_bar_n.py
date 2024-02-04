import sys, argparse, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import cos, sin, pi
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))

parser=argparse.ArgumentParser()
parser.add_argument('int_n',type=int,help='number of rotation with inversion')
args=parser.parse_args()
map_list=[0,2,1,6,4,0,3]

def HM_bar_n_plotter(n):
    n_map=map_list[n]
    if n_map%2==1:
        N=2*n_map
    else:
        N=n_map
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Cylinder = pv.Cylinder(radius=r, height=2*r, direction=(0.0, 0.0, 1.0))
    Line = pv.Line((0, 0, -R), (0, 0, R))
    Arrow = pv.Arrow(start=(r, 2*r, 0), direction=(1, -1, 0), scale=2)
    HPlane=pv.Plane(i_size=1.3*R,j_size=1.3*R, i_resolution=1, j_resolution=1)

    pl.add_mesh(Cylinder, color=DefaultSettings.Cylinder_color, opacity=0.8)
    pl.add_mesh(Line, color=DefaultSettings.Line_color1, line_width=3)
    pl.add_mesh(Arrow, color=DefaultSettings.Arrow_color)
    pl.add_mesh(HPlane,color=DefaultSettings.Plane_color3,opacity=0.7)

    for i in range(N):
        vec = (cos(i * 2 * pi / n), -sin(i * 2 * pi / n), 0.0)
        if i%2==0:
            Plane = pv.Plane(center=(0.75*r* sin(i * 2 * pi / n), 0.75*r * cos(i * 2 * pi / n), 0.75), direction=vec, i_size=1.5*r,
                         j_size=1.5*r, i_resolution=1, j_resolution=1)
        else:
            Plane = pv.Plane(center=(0.75 * r * sin(i * 2 * pi / n), 0.75 * r * cos(i * 2 * pi / n), -0.75),
                             direction=vec, i_size=1.5 * r,
                             j_size=1.5 * r, i_resolution=1, j_resolution=1)
        if i % 2 == 0:
            pl.add_mesh(Plane, color=DefaultSettings.Plane_color1, opacity=0.5)
        else:
            pl.add_mesh(Plane, color=DefaultSettings.Plane_color2, opacity=0.5)
    PlotSettings.Opposite_line(pl, np.array([0, 0, r]), 1)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    pl.add_text(rf"Hermann-Mauguin symbol: $\bar{n}$", font='times', position=(0, 0.9), viewport=True, color='red')
    pl.add_text(rf"Equivalent with $S_{n_map}$ group", font='times', position=(0, 0.85), viewport=True,
                    color='green')
    if n==6:
        pl.add_text(r"Also equivalent with $C_{3h}$ group", font='times', position=(0, 0.8), viewport=True,
                    color='purple')

HM_bar_n_plotter(args.int_n)

pl.show()