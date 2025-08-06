import numpy as np
import matplotlib.pyplot as plt

# Função B-spline recursiva (Cox-de Boor)
def bspline_basis(i, p, knots, u):
    if p == 0:
        # Considera o valor no último nó como parte do suporte
        if knots[i] <= u < knots[i+1] or (u == knots[-1] and knots[i+1] == knots[-1]):
            return 1.0
        else:
            return 0.0
    else:
        denom1 = knots[i+p] - knots[i]
        denom2 = knots[i+p+1] - knots[i+1]

        term1 = 0.0
        term2 = 0.0

        if denom1 > 0:
            term1 = (u - knots[i]) / denom1 * bspline_basis(i, p-1, knots, u)
        if denom2 > 0:
            term2 = (knots[i+p+1] - u) / denom2 * bspline_basis(i+1, p-1, knots, u)

        return term1 + term2

# Grau da B-spline
degree = 2

# Vetor de nós
knot_vector = [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1]
num_basis = len(knot_vector) - degree - 1

# Cores para os patches
colors_patch1 = ['red'] * num_basis
colors_patch2 = ['blue'] * num_basis
colors_patch1[-1] = 'black'  # última do patch 1
colors_patch2[0] = 'black'   # primeira do patch 2

# Início do gráfico
fig, ax = plt.subplots(figsize=(10, 3))

# --- Patch 1 (intervalo [0, 1])
for i in range(num_basis):
    u_start = knot_vector[i]
    u_end = knot_vector[i + degree + 1]
    u_vals_i = np.linspace(u_start, u_end, 200)
    y_vals = [bspline_basis(i, degree, knot_vector, u) for u in u_vals_i]
    ax.plot(u_vals_i, y_vals, color=colors_patch1[i], linewidth=1.5)

# --- Patch 2 (mesmo espaço paramétrico, deslocado para a direita)
for i in range(num_basis):
    u_start = knot_vector[i]
    u_end = knot_vector[i + degree + 1]
    u_vals_i = np.linspace(u_start, u_end, 200)
    y_vals = [bspline_basis(i, degree, knot_vector, u) for u in u_vals_i]
    ax.plot(u_vals_i + 1, y_vals, color=colors_patch2[i], linewidth=1.5)

# Estética do gráfico
ax.set_xlim(-0.1, 2.1)
ax.set_ylim(-0.1, 1.1)
ax.axis('off')
plt.tight_layout()
plt.show()
