from geomdl import BSpline, NURBS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter

# ==== DADOS DA CURVA NURBS ====
degree = 2
ctrlpts = [
    [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0],
    [-1, -1], [0, -1], [1, -1], [1, 0]
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

# ==== ELEVAÇÃO DOS PONTOS DE CONTROLE ====
factor = 3.0
ctrlpts_bsp3d = [[x*w, y*w, w*factor] for (x, y), w in zip(ctrlpts, weights)]

# ==== PROJEÇÃO CENTRAL DOS PONTOS DE CONTROLE ====
ctrlpts_proj = [[x/z, y/z, 1] for (x, y, z) in ctrlpts_bsp3d]

# ==== PLOTAGEM ====
plt.rcParams['mathtext.fontset'] = 'cm'  # Usa Computer Modern
plt.rcParams['font.family'] = 'serif'    # Deixa o texto com estilo semelhante ao LaTeX
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')


ax.xaxis.set_major_locator(MultipleLocator(0.5))  # A cada 1.0 no eixo x
ax.yaxis.set_major_locator(MultipleLocator(0.5))  # A cada 1.0 no eixo y
ax.zaxis.set_major_locator(MultipleLocator(1.0))  # A cada 1.0 no eixo z

# Plano z = 1
xx, yy = np.meshgrid(np.linspace(-1, 1, 20), np.linspace(-1, 1, 20))
zz = np.ones_like(xx)
ax.plot_surface(xx, yy, zz, color='gray', alpha=0.2, edgecolor='none')

# === MALHA DE PONTOS DE CONTROLE ELEVADOS (R³) ===
x_bsp, y_bsp, z_bsp = zip(*ctrlpts_bsp3d)
ax.scatter(x_bsp, y_bsp, z_bsp, color='black', alpha=0.7, s=40)

# Conectando os pontos (malha R³)
for i in range(len(ctrlpts_bsp3d) - 1):
    pt1 = ctrlpts_bsp3d[i]
    pt2 = ctrlpts_bsp3d[i + 1]
    ax.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], [pt1[2], pt2[2]], color='black', linewidth=1)
# Fechamento
pt1 = ctrlpts_bsp3d[-1]
pt2 = ctrlpts_bsp3d[0]
ax.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], [pt1[2], pt2[2]], color='black', linewidth=1)

# === MALHA DE PONTOS PROJETADOS (z = 1) ===
x_proj, y_proj, z_proj = zip(*ctrlpts_proj)
ax.scatter(x_proj, y_proj, z_proj, color='blue', alpha=0.7,s=40)

# Conectando os pontos projetados (malha R²)
for i in range(len(ctrlpts_proj) - 1):
    pt1 = ctrlpts_proj[i]
    pt2 = ctrlpts_proj[i + 1]
    ax.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], [pt1[2], pt2[2]], color='black', linewidth=1)
# Fechamento
pt1 = ctrlpts_proj[-1]
pt2 = ctrlpts_proj[0]
ax.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], [pt1[2], pt2[2]], color='black', linewidth=1)

# === LINHAS DE PROJEÇÃO ===
for pt3d in ctrlpts_bsp3d:
    ax.plot([0, pt3d[0]], [0, pt3d[1]], [0, pt3d[2]], color='black', linewidth=0.5, alpha=1.0)

# Eixos
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
ax.grid(True)

plt.tight_layout()
plt.show()
