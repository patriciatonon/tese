from geomdl import BSpline
from geomdl.visualization import VisMPL
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Criar a curva
curve = BSpline.Curve()
curve.degree = 2
curve.ctrlpts = [[0, 0], [0.5,1], [1, 0]]
curve.knotvector = [0, 0, 0, 1, 1, 1]
curve.sample_size = 100
curve.evaluate()


# Avaliar ponto físico correspondente a ξ = 0.0,0.5,1.0
param_val_0 = 0.0
mapped_point_0 = curve.evaluate_single(param_val_0)

param_val_05 = 0.5
mapped_point_05 = curve.evaluate_single(param_val_05)

param_val_1 = 1.0
mapped_point_1 = curve.evaluate_single(param_val_1)

# Obter os pontos da curva para plotagem
curve_points = curve.evalpts
x_vals, y_vals = zip(*curve_points)

# Plotando os pontos de controle
ctrl_x, ctrl_y = zip(*curve.ctrlpts)



plt.figure(figsize=(4, 4))
plt.plot(x_vals, y_vals, label="Curva NURBS",color='red', linewidth=1.5)
plt.plot(ctrl_x, ctrl_y, label="Pontos de Controle", color='black', linewidth=1.5, marker='o', markersize=7, markerfacecolor='blue', markeredgecolor='blue')  # 'bo-' para círculos azuis conectados por linhas
# plt.legend()
# plt.grid(True)
plt.xlabel("y1")
plt.ylabel("y2")
# plt.axis("equal")
plt.xlim([-0.02,1.02])  # exemplo de limite no eixo x
plt.ylim([-0.02,1.02])  # exemplo de limite no eixo y
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))  # espaçamento de 0.5 no eixo x
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))  # espaçamento de 1.0 no eixo y
plt.show()

plt.figure(figsize=(4,4))
plt.plot(x_vals, y_vals, label="Curva NURBS",color='red', linewidth=1.5)
plt.plot(*mapped_point_0, marker='s', markersize=7, markerfacecolor='red', markeredgecolor='red')
plt.plot(*mapped_point_1, marker='s', markersize=7, markerfacecolor='red', markeredgecolor='red')
# plt.grid(True)
plt.xlabel("y1")
plt.ylabel("y2")
plt.xlim([-0.02,1.02])  # exemplo de limite no eixo x
plt.ylim([-0.02,1.02])  # exemplo de limite no eixo y
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))  # espaçamento de 0.5 no eixo x
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))  # espaçamento de 1.0 no eixo y
plt.show()



# Inserir um novo nó
curve.insert_knot(0.5)

# Avaliar ponto físico correspondente a ξ = 0.0,0.5,1.0
param_val_0 = 0.0
mapped_point_0 = curve.evaluate_single(param_val_0)

param_val_05 = 0.5
mapped_point_05 = curve.evaluate_single(param_val_05)

param_val_1 = 1.0
mapped_point_1 = curve.evaluate_single(param_val_1)

# Obter os pontos da curva para plotagem
curve_points = curve.evalpts
x_vals, y_vals = zip(*curve_points)

# Plotando os pontos de controle
ctrl_x, ctrl_y = zip(*curve.ctrlpts)



plt.figure(figsize=(4, 4))
plt.plot(x_vals, y_vals, label="Curva NURBS",color='red', linewidth=1.5)
plt.plot(ctrl_x, ctrl_y, label="Pontos de Controle", color='black', linewidth=1.5, marker='o', markersize=7, markerfacecolor='blue', markeredgecolor='blue')  # 'bo-' para círculos azuis conectados por linhas
# plt.legend()
# plt.grid(True)
plt.xlabel("y1")
plt.ylabel("y2")
# plt.axis("equal")
plt.xlim([-0.02,1.02])  # exemplo de limite no eixo x
plt.ylim([-0.02,1.02])  # exemplo de limite no eixo y
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))  # espaçamento de 0.5 no eixo x
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))  # espaçamento de 1.0 no eixo y
plt.show()

plt.figure(figsize=(4,4))
plt.plot(x_vals, y_vals, label="Curva NURBS",color='red', linewidth=1.5)
plt.plot(*mapped_point_0, marker='s', markersize=7, markerfacecolor='red', markeredgecolor='red')
plt.plot(*mapped_point_05, marker='s', markersize=7, markerfacecolor='red', markeredgecolor='red')
plt.plot(*mapped_point_1, marker='s', markersize=7, markerfacecolor='red', markeredgecolor='red')
# plt.grid(True)
plt.xlabel("y1")
plt.ylabel("y2")
plt.xlim([-0.02,1.02])  # exemplo de limite no eixo x
plt.ylim([-0.02,1.02])  # exemplo de limite no eixo y
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))  # espaçamento de 0.5 no eixo x
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))  # espaçamento de 1.0 no eixo y
plt.show()



# from geomdl import BSpline
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import numpy as np

# # Função para calcular a base B-spline recursivamente
# def bspline_basis(degree, kv, i, u):
#     if degree == 0:
#         return 1.0 if kv[i] <= u < kv[i + 1] else 0.0
#     else:
#         left = 0.0
#         right = 0.0
#         if kv[i + degree] != kv[i]:
#             left = (u - kv[i]) / (kv[i + degree] - kv[i]) * bspline_basis(degree - 1, kv, i, u)
#         if kv[i + degree + 1] != kv[i + 1]:
#             right = (kv[i + degree + 1] - u) / (kv[i + degree + 1] - kv[i + 1]) * bspline_basis(degree - 1, kv, i + 1, u)
#         return left + right

# # Criar a curva
# curve = BSpline.Curve()
# curve.degree = 2
# curve.ctrlpts = [[0, 0], [0.5, 1], [1, 0]]
# curve.knotvector = [0, 0, 0, 1, 1, 1]
# curve.sample_size = 100
# curve.evaluate()

# # Inserir um novo nó
# # curve.insert_knot(0.5)

# # Obter o número de funções base
# n_basis = len(curve.ctrlpts)
# degree = curve.degree
# kv = curve.knotvector

# # Domínio paramétrico
# u_vals = np.linspace(kv[degree], kv[-degree - 1], 200)

# # Plot das funções base
# plt.figure(figsize=(4, 4))
# for i in range(n_basis):
#     b_vals = [bspline_basis(degree, kv, i, u) for u in u_vals]
#     plt.plot(u_vals, b_vals, label=f"$N_{{{i},{degree}}}$")

# plt.xlabel(r"$\xi$")
# plt.ylabel("Funções base B-spline")
# plt.xlim([-0.002,1.002])  # exemplo de limite no eixo x
# plt.ylim([-0.002,1.002])  # exemplo de limite no eixo y
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(0.2))
# plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# # plt.grid(True)
# # plt.legend(fontsize=14)
# plt.title("Funções base B-spline no espaço paramétrico")
# plt.show()
