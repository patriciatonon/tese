import os
from geomdl import NURBS
from geomdl import exchange
from geomdl.visualization import VisVTK as vis
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from geomdl import operations

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS surface instance
surf = NURBS.Surface()

# Set degrees
surf.degree_u = 2
surf.degree_v = 2

# Dimensões da malha de controle
size_u = 5  # número de pontos por linha
size_v = 4  # número de linhas

# Pontos de controle com pesos (x, y, z, w)
ctrlpts = [
    [0.0, 0.0, 0, 1.0], [0.0, 0.6, 0.3, 1.0], [0.0, 1.4, 0.3, 1.0], [0.0, 2.0, 0, 1.0],
    [0.3, 0.0, 0, 1.0], [0.3, 0.6, 0.3, 1.0], [0.3, 1.4, 0.3, 1.0], [0.3, 2.0, 0, 1.0],
    [1.0, 0.0, 0, 1.0], [1.0, 0.6, 0.3, 1.0], [1.0, 1.4, 0.3, 1.0], [1.0, 2.0, 0, 1.0],
    [1.7, 0.0, 0, 1.0], [1.7, 0.6, 0.3, 1.0], [1.7, 1.4, 0.3, 1.0], [1.7, 2.0, 0, 1.0],
    [2.0, 0.0, 0, 1.0], [2.0, 0.6, 0.3, 1.0], [2.0, 1.4, 0.3, 1.0], [2.0, 2.0, 0, 1.0],
]

# Atribuir pontos e pesos
surf.set_ctrlpts(ctrlpts, size_u, size_v)

# Knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 1.0, 2.0, 2.0, 2.0]

# Resolução da superfície
surf.delta = (0.01, 0.01)

# Avaliar os pontos da superfície
surf.evaluate()

# ----------------------
# Função para extrair curvas isoparamétricas
def extract_isoparametric_curve(surface, fixed_param, direction='u', n=100):
    points = []
    param_range = np.linspace(0.0, 1.0, n)
    for t in param_range:
        if direction == 'u':
            pt = surface.evaluate_single((fixed_param, t))
        else:
            pt = surface.evaluate_single((t, fixed_param))
        points.append(pt)
    return points

# Obter todos os knots (inclusivos) normalizados
knots_u = sorted(set([kv / surf.knotvector_u[-1] for kv in surf.knotvector_u if 0 <= kv <= surf.knotvector_u[-1]]))
knots_v = sorted(set([kv / surf.knotvector_v[-1] for kv in surf.knotvector_v if 0 <= kv <= surf.knotvector_v[-1]]))

# Obter curvas isoparamétricas ao longo de todos os knots (inclusivos)
isoparam_curves = []

# Para todos os knots em u
for u in knots_u:
    isoparam_curves.append(extract_isoparametric_curve(surf, u, direction='u'))

# Para todos os knots em v
for v in knots_v:
    isoparam_curves.append(extract_isoparametric_curve(surf, v, direction='v'))

# Renderização com Matplotlib para mostrar as curvas dos knots
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Organizar pontos da superfície
eval_pts = np.array(surf.evalpts)
res_u = int(1 / surf.delta[0])
res_v = int(1 / surf.delta[1])

X = eval_pts[:, 0].reshape((res_u, res_v))
Y = eval_pts[:, 1].reshape((res_u, res_v))
Z = eval_pts[:, 2].reshape((res_u, res_v))

# Superfície colorida
# Superfície cinza claro e lisa (sem malha)
ax.plot_surface(X, Y, Z, color='#f9f9f9', alpha=0.2, linewidth=0)


# Curvas dos knots (incluindo extremos)
for curve in isoparam_curves:
    c = np.array(curve)
    ax.plot(c[:, 0], c[:, 1], c[:, 2], color='red', linewidth=1.5)

# PLOT DA REDE DE PONTOS DE CONTROLE
ctrlpts_np = np.array(surf.ctrlpts2d)

# Linhas em u (varrendo v)
for row in ctrlpts_np:
    row = np.array(row)
    ax.plot(row[:, 0], row[:, 1], row[:, 2], color='black', linewidth=1.5, marker='o', markersize=5,  markerfacecolor='blue', markeredgecolor='blue')

# Linhas em v (varrendo u)
for col_idx in range(len(ctrlpts_np[0])):
    col = np.array([ctrlpts_np[row_idx][col_idx] for row_idx in range(len(ctrlpts_np))])
    ax.plot(col[:, 0], col[:, 1], col[:, 2], color='black', linewidth=1.5, marker='o', markersize=5, markerfacecolor='blue', markeredgecolor='blue')

def set_axes_equal(ax):
    '''Deixa os eixos 3D com a mesma escala visual'''
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    plot_radius = 0.5 * max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])

# Mostra a figura com escala igual nos eixos
set_axes_equal(ax)
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_axis_off()
plt.show()




