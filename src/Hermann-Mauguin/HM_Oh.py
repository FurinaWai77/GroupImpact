import sys, pyvista as pv, numpy as np, pyautogui
sys.path.insert(0,r"../../")
from math import sqrt
from vtk import vtkMatplotlibMathTextUtilities
from settings import DefaultSettings, PlotSettings

screensize=pyautogui.size()
PlotSettings.pv_Setting()
pl = pv.Plotter(notebook=0, window_size=(screensize.width, screensize.height),shape=(1,2))

def HM_Oh_plotter():
    pl.subplot(0, 0)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Oct = pv.Octahedron(radius=r)
    PlotSettings.Ref_sphere_small(pl)
    Points = np.array([[r / sqrt(2), r / sqrt(2), 0], [r / sqrt(2), -r / sqrt(2), 0], [-r / sqrt(2), r / sqrt(2), 0],
                       [-r / sqrt(2), -r / sqrt(2), 0], [0, 0, r], [0, 0, -r]])
    HPlane1 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(0, 0, 1))
    HPlane2 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(0, 1, 0))
    HPlane3 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1, 0, 0))
    pl.add_mesh(HPlane1, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane2, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane3, color=DefaultSettings.Plane_color2, opacity=0.5)
    PlotSettings.Add_points(pl, Points, 1)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    PlotSettings.Opposite_line(pl, np.array([R, R, 0]) / sqrt(2), 2)
    PlotSettings.Opposite_line(pl, np.array([R, -R, 0]) / sqrt(2), 2)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), -R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), -R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([-R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([sqrt(2) * R / sqrt(3), 0, R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([sqrt(2) * R / sqrt(3), 0, -R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([0, sqrt(2) * R / sqrt(3), R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([0, sqrt(2) * R / sqrt(3), -R / sqrt(3)]), 4)
    pl.add_mesh(Oct, color=DefaultSettings.Tetra_color, opacity=0.8)

    pl.subplot(0, 1)
    R = DefaultSettings.Ex_radius
    r = DefaultSettings.In_radius
    PlotSettings.BasePlotSetting(pl)
    Oct = pv.Octahedron(radius=r)
    PlotSettings.Ref_sphere_small(pl)
    Points = np.array([[r / sqrt(2), r / sqrt(2), 0], [r / sqrt(2), -r / sqrt(2), 0], [-r / sqrt(2), r / sqrt(2), 0],
                       [-r / sqrt(2), -r / sqrt(2), 0], [0, 0, r], [0, 0, -r]])
    HPlane1 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(0, 1, 1))
    HPlane2 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(0, 1, -1))
    HPlane3 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1, 1, 0))
    HPlane4 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1, -1, 0))
    HPlane5 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1, 0, 1))
    HPlane6 = pv.Plane(i_size=1.3 * R, j_size=1.3 * R, i_resolution=1, j_resolution=1, direction=(1, 0, -1))
    pl.add_mesh(HPlane1, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane2, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane3, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane4, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane5, color=DefaultSettings.Plane_color2, opacity=0.5)
    pl.add_mesh(HPlane6, color=DefaultSettings.Plane_color2, opacity=0.5)
    PlotSettings.Add_points(pl, Points, 1)
    PlotSettings.Opposite_line(pl, np.array([0, 0, R]), 2)
    PlotSettings.Opposite_line(pl, np.array([R, R, 0]) / sqrt(2), 2)
    PlotSettings.Opposite_line(pl, np.array([R, -R, 0]) / sqrt(2), 2)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), R / sqrt(3), -R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([R / sqrt(3), -R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([-R / sqrt(3), R / sqrt(3), R / sqrt(3)]), 3)
    PlotSettings.Opposite_line(pl, np.array([sqrt(2) * R / sqrt(3), 0, R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([sqrt(2) * R / sqrt(3), 0, -R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([0, sqrt(2) * R / sqrt(3), R / sqrt(3)]), 4)
    PlotSettings.Opposite_line(pl, np.array([0, sqrt(2) * R / sqrt(3), -R / sqrt(3)]), 4)
    pl.add_mesh(Oct, color=DefaultSettings.Tetra_color, opacity=0.8)

    pl.add_text(rf"Hermann-Mauguin symbol: 4/m $\bar 3$ 2/m", font='times',
                position=(0, 0.9), viewport=True,
                color='red')
    pl.add_text(rf"Here m represents reflections, 9 in total, '/' represents perpendicular (perp)", font='times', position=(0, 0.85),
                viewport=True,
                color='blue')
    pl.add_text(rf"3 $C_4$'s perp to reflections, 4 inversion $\bar 3$'s, 6 $C_2$'s perp to reflections", font='times', position=(0, 0.8),
                viewport=True,
                color='green')

HM_Oh_plotter()

pl.show()