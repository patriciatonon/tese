import os
from geomdl import NURBS
from geomdl import exchange
from geomdl.visualization import VisVTK as vis
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from geomdl import operations
import matplotlib.ticker as ticker

# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a NURBS surface instance
surf = NURBS.Surface()

# Set degrees
surf.degree_u = 2
surf.degree_v = 2

# Dimensões da malha de controle
size_u = 6  # número de pontos por linha
size_v = 3  # número de linhas

# Pontos de controle com pesos (x, y, z, w)
ctrlpts = [
 [3.5355339059e-01, -3.5355339059e-01, 0.0, 1.0000000000e+00],
 [1.0069052197e+00, -1.0069052197e+00, 0.0, 1.0000000000e+00],
 [2.0000000000e+00, -2.0000000000e+00, 0.0, 1.0000000000e+00],

 [4.2099142644e-01, -2.8611535475e-01, 0.0, 9.2677669530e-01],
 [1.0475821302e+00, -7.6781561080e-01, 0.0, 1.0000000000e+00],
 [2.0000000000e+00, -1.5000000000e+00, 0.0, 1.0000000000e+00],

 [5.0000000000e-01, -1.0355339059e-01, 0.0, 8.5355339059e-01],
 [1.0952380952e+00, -2.6087347369e-01, 0.0, 1.0000000000e+00],
 [2.0000000000e+00, -5.0000000000e-01, 0.0, 1.0000000000e+00],

 [5.0000000000e-01, 1.0355339059e-01, 0.0, 8.5355339059e-01],
 [1.0952380952e+00, 2.6087347369e-01, 0.0, 1.0000000000e+00],
 [2.0000000000e+00, 5.0000000000e-01, 0.0, 1.0000000000e+00],

 [4.2099142644e-01, 2.8611535475e-01, 0.0, 8.5355339059e-01],
 [1.0475821302e+00, 7.6781561080e-01, 0.0, 1.0000000000e+00],
 [2.0000000000e+00, 1.5000000000e+00, 0.0, 1.0000000000e+00],

 [3.5355339059e-01, 3.5355339059e-01, 0.0, 9.2677669530e-01],
 [1.0069052197e+00, 1.0069052197e+00, 0.0, 1.0000000000e+00],
 [2.0000000000e+00, 2.0000000000e+00, 0.0, 1.0000000000e+00]
]


# Atribuir pontos e pesos
surf.set_ctrlpts(ctrlpts, size_u, size_v)

# Knot vectors
surf.knotvector_u = [0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 4.0, 4.0, 4.0]
surf.knotvector_v = [0.0, 0.0, 0.0, 1.0, 1.0, 1.0]

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


# Superfícies isoparamétricas em u
isos_u = [extract_isoparametric_curve(surf, u, direction='u') for u in knots_u]

# Superfícies isoparamétricas em v
isos_v = [extract_isoparametric_curve(surf, v, direction='v') for v in knots_v]



# Pontos avaliados da superfície (grid regular)
eval_pts = np.array(surf.evalpts)
res_u = int(1 / surf.delta[0])
res_v = int(1 / surf.delta[1])

X = eval_pts[:, 0].reshape((res_u, res_v))
Y = eval_pts[:, 1].reshape((res_u, res_v))

fig, ax = plt.subplots(figsize=(5,5))

# # Desenha fundo cinza claro para a superfície
# ax.pcolormesh(X, Y, np.zeros_like(X), shading='auto', color='lightgray', alpha=0.3)

# Plota curvas isoparamétricas em u (mantém v variando)
for curve in isos_u:
    curve = np.array(curve)
    ax.plot(curve[:,0], curve[:,1], 'r-', linewidth=1.0)  # vermelho

# Plota curvas isoparamétricas em v (mantém u variando)
for curve in isos_v:
    curve = np.array(curve)
    ax.plot(curve[:,0], curve[:,1], 'r-', linewidth=1.0)  # azul

# Ajustes finais do gráfico
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel("X")
ax.set_ylabel("Y")
# ax.set_title("Curvas Isoparamétricas da Superfície NURBS")
ax.axis('off')              # <<< desativa os eixos
plt.show()