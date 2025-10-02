import os
import numpy as np
from geomdl import NURBS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# =====================================================
# Definição do volume NURBS
# =====================================================
vol = NURBS.Volume()

# Graus em cada direção
vol.degree_u = 2
vol.degree_v = 2
vol.degree_w = 2

# Dimensões de pontos de controle
size_u = 6  # pontos por linha
size_v = 3  # número de linhas
size_w = 3  # camadas em z

# Pontos de controle na camada z = 0
base_ctrlpts = [
 [3.5355339059e-01, -3.5355339059e-01, 0.0, 1.0],
 [1.0069052197e+00, -1.0069052197e+00, 0.0, 1.0],
 [2.0000000000e+00, -2.0000000000e+00, 0.0, 1.0],

 [4.2099142644e-01, -2.8611535475e-01, 0.0, 9.2677669530e-01],
 [1.0475821302e+00, -7.6781561080e-01, 0.0, 1.0],
 [2.0000000000e+00, -1.5000000000e+00, 0.0, 1.0],

 [5.0000000000e-01, -1.0355339059e-01, 0.0, 8.5355339059e-01],
 [1.0952380952e+00, -2.6087347369e-01, 0.0, 1.0],
 [2.0000000000e+00, -5.0000000000e-01, 0.0, 1.0],

 [5.0000000000e-01,  1.0355339059e-01, 0.0, 8.5355339059e-01],
 [1.0952380952e+00,  2.6087347369e-01, 0.0, 1.0],
 [2.0000000000e+00,  5.0000000000e-01, 0.0, 1.0],

 [4.2099142644e-01,  2.8611535475e-01, 0.0, 8.5355339059e-01],
 [1.0475821302e+00,  7.6781561080e-01, 0.0, 1.0],
 [2.0000000000e+00,  1.5000000000e+00, 0.0, 1.0],

 [3.5355339059e-01,  3.5355339059e-01, 0.0, 9.2677669530e-01],
 [1.0069052197e+00,  1.0069052197e+00, 0.0, 1.0],
 [2.0000000000e+00,  2.0000000000e+00, 0.0, 1.0],
]

# Função para replicar camadas em z
def extrude_layers(points, z_values):
    layers = []
    for z in z_values:
        layer = [[x, y, z, w] for (x, y, _, w) in points]
        layers.extend(layer)
    return layers

# Cria camadas em z = 0, 0.5, 1.0
ctrlpts = extrude_layers(base_ctrlpts, [0.0, 0.5, 1.0])

# Define pontos no volume
vol.set_ctrlpts(ctrlpts, size_u, size_v, size_w)

# Vetores de nós
vol.knotvector_u = [0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 4.0, 4.0, 4.0]
vol.knotvector_v = [0.0, 0.0, 0.0, 1.0, 1.0, 1.0]
vol.knotvector_w = [0.0, 0.0, 0.0, 1.0, 1.0, 1.0]

vol.evaluate()

# =====================================================
# Funções auxiliares
# =====================================================

def extract_isoparametric_curve(volume, fixed_params, direction='u', n=50):
    """Extrai curva isoparamétrica fixando dois parâmetros."""
    points = []
    param_range = np.linspace(0.0, 1.0, n)
    for t in param_range:
        if direction == 'u':
            v0, w0 = fixed_params
            pt = volume.evaluate_single((t, v0, w0))
        elif direction == 'v':
            u0, w0 = fixed_params
            pt = volume.evaluate_single((u0, t, w0))
        else:  # direction == 'w'
            u0, v0 = fixed_params
            pt = volume.evaluate_single((u0, v0, t))
        points.append(pt)
    return np.array(points)

def extract_isoparametric_surface(volume, fixed_param, direction='u', n=30):
    """Extrai superfície isoparamétrica fixando um parâmetro."""
    points = []
    grid = np.linspace(0.0, 1.0, n)
    for v in grid:
        row = []
        for w in grid:
            if direction == 'u':
                pt = volume.evaluate_single((fixed_param, v, w))
            elif direction == 'v':
                pt = volume.evaluate_single((v, fixed_param, w))
            else:  # direction == 'w'
                pt = volume.evaluate_single((v, w, fixed_param))
            row.append(pt)
        points.append(row)
    return np.array(points)

# =====================================================
# Plotando curvas e superfícies
# =====================================================
fig, ax = plt.subplots(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')

# Obter knots únicos normalizados
knots_u = sorted(set(k/vol.knotvector_u[-1] for k in vol.knotvector_u))
knots_v = sorted(set(k/vol.knotvector_v[-1] for k in vol.knotvector_v))
knots_w = sorted(set(k/vol.knotvector_w[-1] for k in vol.knotvector_w))

# --- Desenhar curvas isoparamétricas ---
for v in knots_v:
    for w in knots_w:
        curve = extract_isoparametric_curve(vol, (v, w), direction='u')
        ax.plot(curve[:,0], curve[:,1], curve[:,2], color='red', linewidth=1.0)

for u in knots_u:
    for w in knots_w:
        curve = extract_isoparametric_curve(vol, (u, w), direction='v')
        ax.plot(curve[:,0], curve[:,1], curve[:,2], color='red', linewidth=1.0)

for u in knots_u:
    for v in knots_v:
        curve = extract_isoparametric_curve(vol, (u, v), direction='w')
        ax.plot(curve[:,0], curve[:,1], curve[:,2], color='red', linewidth=1.0)

# --- Desenhar superfícies isoparamétricas (exemplo u=0.5, v=0.5, w=0.5) ---
for u in [0.0,0.25,0.5,0.75,1.0]:
    surf = extract_isoparametric_surface(vol, u, direction='u', n=20)
    X, Y, Z = surf[:,:,0], surf[:,:,1], surf[:,:,2]
    ax.plot_surface(X, Y, Z, color='grey', alpha=0.15, edgecolor='none')

for v in [0.0,1.0]:
    surf = extract_isoparametric_surface(vol, v, direction='v', n=20)
    X, Y, Z = surf[:,:,0], surf[:,:,1], surf[:,:,2]
    ax.plot_surface(X, Y, Z, color='grey', alpha=0.15, edgecolor='none')

for w in [0.0,1.0]:
    surf = extract_isoparametric_surface(vol, w, direction='w', n=20)
    X, Y, Z = surf[:,:,0], surf[:,:,1], surf[:,:,2]
    ax.plot_surface(X, Y, Z, color='grey', alpha=0.15, edgecolor='none')

ax.axis('off')              # <<< desativa os eixos
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
plt.show()
