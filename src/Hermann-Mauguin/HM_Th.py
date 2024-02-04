import sys, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import sqrt
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height))


def HM_Th_plotter():
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    axes = pv.Axes(show_actor=True, actor_scale=2.0, line_width=5)
    Tetra = pv.Tetrahedron(radius=r)
    Tetra2 = pv.Tetrahedron(radius=r).rotate_z(90, point=axes.origin)
    PlotSettings.Ref_sphere_small(pl)
    pl.add_mesh(Tetra, color=DefaultSettings.Tetra_color, opacity=0.8)
    pl.add_mesh(Tetra2, color='bisque', opacity=0.8)
    Points = np.array([[r, r, r], [-r, -r, r], [r, -r, -r], [-r, r, -r]]) / sqrt(3)
    Points2 = np.array([[r, -r, r], [-r, r, r], [r, r, -r], [-r, -r, -r]]) / sqrt(3)
    HPlane1 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1,direction=(0,0,1))
    HPlane2 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1,direction=(0,1,0))
    HPlane3 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1,direction=(1,0,0))
    PlotSettings.Add_points(pl, Points, 1)
    PlotSettings.Add_points(pl, Points2, 2)
    pl.add_mesh(HPlane1, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane2, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane3, color=DefaultSettings.Plane_color2, opacity=0.5)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    PlotSettings.Opposite_line(pl, np.array([0, R, 0]), 2)
    PlotSettings.Opposite_line(pl, np.array([R, 0, 0]), 2)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), -R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), -R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([-R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)

    pl.add_text(rf"Hermann-Mauguin symbol: 2/m $\bar 3$", font='times', position=(0, 0.9), viewport=True, color='red')
    pl.add_text(rf"Here m represents reflections, 3 in total, '/' represents perpendicular(perp)", font='times', position=(0, 0.85),
                viewport=True,
                color='blue')
    pl.add_text(rf"3 $C_2$'s perp to reflections, and 4 $\bar 3$ axes", font='times', position=(0, 0.8),
                viewport=True,
                color='magenta')

HM_Th_plotter()

pl.show()