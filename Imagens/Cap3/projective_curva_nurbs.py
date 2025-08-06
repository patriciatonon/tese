# from geomdl import BSpline, NURBS
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np


# # ==== DADOS DA CURVA NURBS (CIRCUNFERÊNCIA QUADRÁTICA) ====
# degree = 2
# radius = 1.0
# ctrlpts = [
#     [1, 0],
#     [1, 1],
#     [0, 1],
#     [-1, 1],
#     [-1, 0],
#     [-1, -1],
#     [0, -1],
#     [1, -1],
#     [1, 0]  # fechamento
# ]
# weights = [
#     1, np.sqrt(2)/2, 1, np.sqrt(2)/2,
#     1, np.sqrt(2)/2, 1, np.sqrt(2)/2, 1
# ]
# knotvector = [0, 0, 0,
#               0.25, 0.25,
#               0.5, 0.5,
#               0.75, 0.75,
#               1, 1, 1]

# # ==== CURVA NURBS (projetada no plano z = 1) ====
# nurbs = NURBS.Curve()
# nurbs.degree = degree
# nurbs.ctrlpts = ctrlpts
# nurbs.weights = weights
# nurbs.knotvector = knotvector
# nurbs.sample_size = 100
# nurbs.evaluate()

# # ==== CURVA B-SPLINE EM R^3 (elevada com coordenadas homogêneas) ====
# factor = 3.0  # altura para a coordenada w
# ctrlpts_bsp3d = []
# for (x, y), w in zip(ctrlpts, weights):
#     ctrlpts_bsp3d.append([x * w, y * w, w * factor])

# bsp = BSpline.Curve()
# bsp.degree = degree
# bsp.ctrlpts = ctrlpts_bsp3d
# bsp.knotvector = knotvector
# bsp.sample_size = 100
# bsp.evaluate()

# # ==== PROJEÇÃO CENTRAL NO PLANO z = 1 ====
# evalpts_bsp3d = bsp.evalpts
# projected = [[x / z, y / z, 1] for (x, y, z) in evalpts_bsp3d]

# # ==== PLOTAGEM ====
# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_subplot(111, projection='3d')

# # Plano z = 1 (com malha cinza)
# xx, yy = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
# zz = np.ones_like(xx)
# ax.plot_surface(xx, yy, zz, color='gray', alpha=0.2, edgecolor='none')

# # Curva B-spline elevada (em preto)
# x_bsp, y_bsp, z_bsp = zip(*evalpts_bsp3d)
# ax.plot(x_bsp, y_bsp, z_bsp, 'k', linewidth=2)

# # Curva NURBS projetada (em vermelho, no plano z = 1)
# x_nurbs, y_nurbs, z_nurbs = zip(*projected)
# ax.plot(x_nurbs, y_nurbs, z_nurbs, 'r', linewidth=2)

# # Linhas de projeção: da origem até pontos elevados
# N = 5
# for i in range(0, len(evalpts_bsp3d), N):
#     xb, yb, zb = evalpts_bsp3d[i]
#     ax.plot([0, xb], [0, yb], [0, zb], color='blue', linewidth=0.5, alpha=0.6)

# # Rótulos matemáticos
# ax.text(x_bsp[70], y_bsp[70], z_bsp[70] + 0.2, r'$C^w(\xi)$', fontsize=12)
# ax.text(x_nurbs[70], y_nurbs[70], z_nurbs[70] + 0.2, r'$C(\xi)$', fontsize=12)

# # Eixos e visual
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
# ax.set_xlim([-2, 2])
# ax.set_ylim([-2, 2])
# ax.set_zlim([0, factor + 1])
# ax.view_init(elev=25, azim=135)
# ax.grid(True)

# plt.tight_layout()
# plt.show()
from geomdl import BSpline, NURBS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter

# ==== DADOS DA CURVA NURBS (CIRCUNFERÊNCIA QUADRÁTICA) ====
degree = 2
radius = 1.0
ctrlpts = [
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0]  # fechamento
]
weights = [
    1, np.sqrt(2)/2, 1, np.sqrt(2)/2,
    1, np.sqrt(2)/2, 1, np.sqrt(2)/2, 1
]
knotvector = [0, 0, 0,
              0.25, 0.25,
              0.5, 0.5,
              0.75, 0.75,
              1, 1, 1]

# ==== CURVA NURBS (projetada no plano z = 1) ====
nurbs = NURBS.Curve()
nurbs.degree = degree
nurbs.ctrlpts = ctrlpts
nurbs.weights = weights
nurbs.knotvector = knotvector
nurbs.sample_size = 100
nurbs.evaluate()

# ==== CURVA B-SPLINE EM R^3 (elevada com coordenadas homogêneas) ====
factor = 3.0  # altura para a coordenada w
ctrlpts_bsp3d = []
for (x, y), w in zip(ctrlpts, weights):
    ctrlpts_bsp3d.append([x * w, y * w, w * factor])

bsp = BSpline.Curve()
bsp.degree = degree
bsp.ctrlpts = ctrlpts_bsp3d
bsp.knotvector = knotvector
bsp.sample_size = 100
bsp.evaluate()

# ==== PROJEÇÃO CENTRAL NO PLANO z = 1 ====
evalpts_bsp3d = bsp.evalpts
projected = [[x / z, y / z, 1] for (x, y, z) in evalpts_bsp3d]

# ==== PLOTAGEM ====
fig = plt.figure(figsize=(10, 7))

plt.rcParams['mathtext.fontset'] = 'cm'  # Usa Computer Modern
plt.rcParams['font.family'] = 'serif'    # Deixa o texto com estilo semelhante ao LaTeX

ax = fig.add_subplot(111, projection='3d')


ax.xaxis.set_major_locator(MultipleLocator(0.5))  # A cada 1.0 no eixo x
ax.yaxis.set_major_locator(MultipleLocator(0.5))  # A cada 1.0 no eixo y
ax.zaxis.set_major_locator(MultipleLocator(1.0))  # A cada 1.0 no eixo z

# Plano z = 1 (com malha cinza)
xx, yy = np.meshgrid(np.linspace(-1, 1, 20), np.linspace(-1, 1, 20))
zz = np.ones_like(xx)
ax.plot_surface(xx, yy, zz, color='gray', alpha=0.2, edgecolor='none')

# Curva B-spline elevada (em preto)
x_bsp, y_bsp, z_bsp = zip(*evalpts_bsp3d)
ax.plot(x_bsp, y_bsp, z_bsp, 'k', linewidth=2)

# Curva NURBS projetada (em vermelho, no plano z = 1)
x_nurbs, y_nurbs, z_nurbs = zip(*projected)
ax.plot(x_nurbs, y_nurbs, z_nurbs, 'r', linewidth=2)

# Linhas de projeção: da origem até pontos elevados
N = 5
for i in range(0, len(evalpts_bsp3d), N):
    xb, yb, zb = evalpts_bsp3d[i]
    ax.plot([0, xb], [0, yb], [0, zb], color='black', linewidth=0.5, alpha=0.5)

# Rótulos matemáticos
# ax.text(x_bsp[70], y_bsp[70], z_bsp[70] + 0.2, r'$C^w(\xi)$', fontsize=12)
# ax.text(x_nurbs[70], y_nurbs[70], z_nurbs[70] + 0.2, r'$C(\xi)$', fontsize=12)

# Eixos e visual
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([0, factor + 1])
ax.view_init(elev=15, azim=135)
# ax.grid(False)  # Remove a grade


plt.tight_layout()
plt.show()
