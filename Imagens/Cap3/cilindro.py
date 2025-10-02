
# from geomdl import NURBS
# from geomdl.visualization import VisMPL
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import math

# # Criar a curva NURBS
# D = 1.0
# sqrt2 = math.sqrt(2)
# curve = NURBS.Curve()
# curve.degree = 2
# curve.ctrlpts = [[sqrt2*D/4.0, -sqrt2*D/4.0],
#                  [D/sqrt2, 0.0],
#                  [sqrt2*D/4.0, sqrt2*D/4.0]]

# curve.weights = [1.0, sqrt2/2.0, 1.0]  # pesos iniciais iguais a 1.0
# curve.knotvector = [0, 0, 0, 1, 1, 1]
# curve.sample_size = 100
# curve.evaluate()

# # Obter os pontos da curva para plotagem
# curve_points = curve.evalpts
# x_vals, y_vals = zip(*curve_points)

# # Plotando os pontos de controle
# ctrl_x, ctrl_y = zip(*curve.ctrlpts)

# plt.figure(figsize=(4, 4))
# plt.plot(x_vals, y_vals, label="Curva NURBS", color='red', linewidth=1.5)
# plt.plot(ctrl_x, ctrl_y, label="Pontos de Controle", color='black', linewidth=1.5,
#          marker='o', markersize=7, markerfacecolor='blue', markeredgecolor='blue')
# plt.xlabel("y1")
# plt.ylabel("y2")
# plt.xlim([0.3, 0.8])
# plt.ylim([-0.5, 0.5])
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# plt.show()

# # Inserir um novo nó
# curve.insert_knot(0.25)
# curve.insert_knot(0.5)
# curve.insert_knot(0.75)


# curve_points = curve.evalpts
# x_vals, y_vals = zip(*curve_points)
# ctrl_x, ctrl_y = zip(*curve.ctrlpts)

# plt.figure(figsize=(4, 4))
# plt.plot(x_vals, y_vals, label="Curva NURBS", color='red', linewidth=1.5)
# plt.plot(ctrl_x, ctrl_y, label="Pontos de Controle", color='black', linewidth=1.5,
#          marker='o', markersize=7, markerfacecolor='blue', markeredgecolor='blue')
# plt.xlabel("y1")
# plt.ylabel("y2")
# plt.xlim([0.3, 0.8])
# plt.ylim([-0.5, 0.5])
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# plt.show()

# with open("pontos_controle.txt", "w") as f:
#     f.write("x y peso\n")
#     for pt, w in zip(curve.ctrlpts, curve.weights):
#         f.write(f"{pt[0]} {pt[1]} {w}\n")


# # plt.figure(figsize=(4, 4))
# # plt.plot(x_vals, y_vals, label="Curva NURBS", color='red', linewidth=1.5)
# # plt.plot(*mapped_point_0, marker='s', markersize=7, markerfacecolor='red', markeredgecolor='red')
# # plt.plot(*mapped_point_05, marker='s', markersize=7, markerfacecolor='red', markeredgecolor='red')
# # plt.plot(*mapped_point_1, marker='s', markersize=7, markerfacecolor='red', markeredgecolor='red')
# # plt.xlabel("y1")
# # plt.ylabel("y2")
# # plt.xlim([-0.02, 1.02])
# # plt.ylim([-0.02, 1.02])
# # ax = plt.gca()
# # ax.spines['top'].set_visible(False)
# # ax.spines['right'].set_visible(False)
# # ax.xaxis.set_major_locator(ticker.MultipleLocator(0.2))
# # ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
# # plt.show()


# #Curva intermediaria
# from geomdl import NURBS
# from geomdl.visualization import VisMPL
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import math

# # Criar a curva NURBS
# D = 1.0
# sqrt2 = math.sqrt(2)
# curve = NURBS.Curve()
# curve.degree = 2
# curve.ctrlpts = [[3.5355339059e-01, -3.5355339059e-01], 
# [4.2099142644e-01, -2.8611535475e-01],
# [5.0000000000e-01, -1.0355339059e-01],
# [5.0000000000e-01, 1.0355339059e-01],
# [4.2099142644e-01, 2.8611535475e-01],
# [3.5355339059e-01, 3.5355339059e-01]]

# curve.weights = [1.0000000000e+00,9.2677669530e-01,8.5355339059e-01,8.5355339059e-01,9.2677669530e-01,1.0000000000e+00]  # pesos iniciais iguais a 1.0
# curve.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve.sample_size = 100
# curve.evaluate()

# curve_points = curve.evalpts
# x_vals, y_vals = zip(*curve_points)
# ctrl_x, ctrl_y = zip(*curve.ctrlpts)

# curve2 = NURBS.Curve()
# curve2.degree = 2
# curve2.ctrlpts = [[2.0000000000e+00, -2.0000000000e+00], 
# [2.0000000000e+00, -1.5000000000e+00], 
# [2.0000000000e+00, -5.0000000000e-01],
# [2.0000000000e+00, 5.0000000000e-01], 
# [2.0000000000e+00, 1.5000000000e+00], 
# [2.0000000000e+00, 2.0000000000e+00]]

# curve2.weights = [1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00]  # pesos iniciais iguais a 1.0
# curve2.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve2.sample_size = 100
# curve2.evaluate()

# curve_points2 = curve.evalpts
# x_vals2, y_vals2 = zip(*curve_points2)
# ctrl_x2, ctrl_y2 = zip(*curve2.ctrlpts)


# plt.figure(figsize=(4, 4))
# # plt.plot(x_vals, y_vals, label="Curva NURBS", color='red', linewidth=1.5)
# plt.plot(ctrl_x, ctrl_y, label="Pontos de Controle", color='black', linewidth=1.5,
#          marker='o', markersize=7, markerfacecolor='blue', markeredgecolor='blue')
# # plt.plot(x_vals2, y_vals2, label="Curva NURBS", color='red', linewidth=1.5)
# plt.plot(ctrl_x2, ctrl_y2, label="Pontos de Controle", color='black', linewidth=1.5,
#          marker='o', markersize=7, markerfacecolor='blue', markeredgecolor='blue')
# plt.xlabel("y1")
# plt.ylabel("y2")
# plt.xlim([0.3, 2.1])
# plt.ylim([-2.1, 2.1])
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# plt.show()


# #Curva intermediaria
# from geomdl import NURBS
# from geomdl.visualization import VisMPL
# import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker
# import math

# # Criar a curva NURBS
# D = 1.0
# sqrt2 = math.sqrt(2)
# curve = NURBS.Curve()
# curve.degree = 2
# curve.ctrlpts = [[3.5355339059e-01, -3.5355339059e-01, 0.0], 
# [4.2099142644e-01, -2.8611535475e-01, 0.0],
# [5.0000000000e-01, -1.0355339059e-01, 0.0],
# [5.0000000000e-01, 1.0355339059e-01, 0.0],
# [4.2099142644e-01, 2.8611535475e-01, 0.0],
# [3.5355339059e-01, 3.5355339059e-01, 0.0]]

# curve.weights = [1.0000000000e+00,9.2677669530e-01,8.5355339059e-01,8.5355339059e-01,9.2677669530e-01,1.0000000000e+00]  # pesos iniciais iguais a 1.0
# curve.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve.sample_size = 100
# curve.evaluate()

# curve_points = curve.evalpts
# x_vals, y_vals,z_vals= zip(*curve_points)
# ctrl_x, ctrl_y,ctrl_z= zip(*curve.ctrlpts)


# curve1 = NURBS.Curve()
# curve1.degree = 2
# curve1.ctrlpts = [[1.0069052197e+00, -1.0069052197e+00, 0.5],
# [1.0475821302e+00, -7.6781561080e-01, 0.5],
# [1.0952380952e+00, -2.6087347369e-01,0.5],
# [1.0952380952e+00, 2.6087347369e-01,0.5],
# [1.0475821302e+00, 7.6781561080e-01,0.5],
# [1.0069052197e+00, 1.0069052197e+00,0.5]]

# curve1.weights = [1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00]  # pesos iniciais iguais a 1.0
# curve1.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve1.sample_size = 100
# curve1.evaluate()

# curve_points1 = curve.evalpts
# x_vals1, y_vals1, z_vals1 = zip(*curve_points1)
# ctrl_x1, ctrl_y1, ctrl_z1 = zip(*curve1.ctrlpts)


# curve2 = NURBS.Curve()
# curve2.degree = 2
# curve2.ctrlpts = [[2.0000000000e+00, -2.0000000000e+00,1.0], 
# [2.0000000000e+00, -1.5000000000e+00,1.0], 
# [2.0000000000e+00, -5.0000000000e-01,1.0],
# [2.0000000000e+00, 5.0000000000e-01,1.0], 
# [2.0000000000e+00, 1.5000000000e+00,1.0], 
# [2.0000000000e+00, 2.0000000000e+00,1.0]]

# curve2.weights = [1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00,1.0000000000e+00]  # pesos iniciais iguais a 1.0
# curve2.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve2.sample_size = 100
# curve2.evaluate()

# curve_points2 = curve.evalpts
# x_vals2, y_vals2,z_vals2 = zip(*curve_points2)
# ctrl_x2, ctrl_y2,ctrl_z2  = zip(*curve2.ctrlpts)


# plt.figure(figsize=(4, 4))

# # Plotar os pontos de controle das curvas
# for cx, cy in [(ctrl_x, ctrl_y), (ctrl_x1, ctrl_y1), (ctrl_x2, ctrl_y2)]:
#     plt.plot(cx, cy, label="Pontos de Controle", color='black', linewidth=1.5,
#              marker='o', markersize=7, markerfacecolor='blue', markeredgecolor='blue')

# # Conectar pontos radialmente (cada linha: curva + curva1 + curva2)
# num_points = len(ctrl_x)  # Número de pontos de controle por curva (6)
# for i in range(num_points):
#     x_line = [ctrl_x[i], ctrl_x1[i], ctrl_x2[i]]
#     y_line = [ctrl_y[i], ctrl_y1[i], ctrl_y2[i]]
#     plt.plot(x_line, y_line, color='black', linewidth=1.0)  # linha vermelha tracejada

# plt.xlabel("y1")
# plt.ylabel("y2")
# plt.xlim([0.3, 2.1])
# plt.ylim([-2.1, 2.1])
# ax = plt.gca()
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
# ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
# plt.show()

from geomdl import NURBS
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

# --- Curva 0 ---
curve = NURBS.Curve()
curve.degree = 2
curve.ctrlpts = [
    [3.5355339059e-01, -3.5355339059e-01, 0.0], 
    [4.2099142644e-01, -2.8611535475e-01, 0.0],
    [5.0000000000e-01, -1.0355339059e-01, 0.0],
    [5.0000000000e-01,  1.0355339059e-01, 0.0],
    [4.2099142644e-01,  2.8611535475e-01, 0.0],
    [3.5355339059e-01,  3.5355339059e-01, 0.0]
]
curve.weights = [1.0, 0.9267766953, 0.85355339059, 0.85355339059, 0.9267766953, 1.0]
curve.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
curve.sample_size = 100
curve.evaluate()

curve_points = curve.evalpts
x_vals, y_vals, z_vals = zip(*curve_points)
ctrl_x, ctrl_y, ctrl_z = zip(*curve.ctrlpts)


# --- Curva 1 ---
curve1 = NURBS.Curve()
curve1.degree = 2
curve1.ctrlpts = [
    [1.0069052197, -1.0069052197, 0.0],
    [1.0475821302, -0.7678156108, 0.0],
    [1.0952380952, -0.26087347369, 0.0],
    [1.0952380952,  0.26087347369, 0.0],
    [1.0475821302,  0.7678156108, 0.0],
    [1.0069052197,  1.0069052197, 0.0]
]
curve1.weights = [1.0]*6
curve1.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
curve1.sample_size = 100
curve1.evaluate()

curve_points1 = curve1.evalpts
x_vals1, y_vals1, z_vals1 = zip(*curve_points1)
ctrl_x1, ctrl_y1, ctrl_z1 = zip(*curve1.ctrlpts)


# --- Curva 2 ---
curve2 = NURBS.Curve()
curve2.degree = 2
curve2.ctrlpts = [
    [2.0, -2.0, 0.0], 
    [2.0, -1.5, 0.0], 
    [2.0, -0.5, 0.0],
    [2.0,  0.5, 0.0], 
    [2.0,  1.5, 0.0], 
    [2.0,  2.0, 0.0]
]
curve2.weights = [1.0]*6
curve2.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
curve2.sample_size = 100
curve2.evaluate()

curve_points2 = curve2.evalpts
x_vals2, y_vals2, z_vals2 = zip(*curve_points2)
ctrl_x2, ctrl_y2, ctrl_z2 = zip(*curve2.ctrlpts)



# --- PLOT 3D ---
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

# Curvas avaliadas
ax.plot(x_vals, y_vals, z_vals, color='red', linewidth=2)
ax.plot(x_vals1, y_vals1, z_vals1, color='green', linewidth=2)
ax.plot(x_vals2, y_vals2, z_vals2, color='blue', linewidth=2)

# # Pontos de controle (com linhas conectando)
# for cx, cy, cz in [(ctrl_x, ctrl_y, ctrl_z),
#                    (ctrl_x1, ctrl_y1, ctrl_z1),
#                    (ctrl_x2, ctrl_y2, ctrl_z2),
#                    (ctrl_x01, ctrl_y01, ctrl_z01),
#                    (ctrl_x11, ctrl_y11, ctrl_z11),
#                    (ctrl_x21, ctrl_y21, ctrl_z21),
#                    (ctrl_x02, ctrl_y02, ctrl_z02),
#                    (ctrl_x12, ctrl_y12, ctrl_z12),
#                    (ctrl_x22, ctrl_y22, ctrl_z22),
#                    ]:
#     ax.plot(cx, cy, cz, color='black', linewidth=0.5,
#             marker='o', markersize=6, markerfacecolor='blue', markeredgecolor='blue')



#set_axes_equal(ax)
# ax.grid(False)
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])
# ax.set_axis_off()
plt.show()

# # --- Curva 0-1 ---
# curve01 = NURBS.Curve()
# curve01.degree = 2
# curve01.ctrlpts = [
#     [3.5355339059e-01, -3.5355339059e-01, 0.5], 
#     [4.2099142644e-01, -2.8611535475e-01, 0.5],
#     [5.0000000000e-01, -1.0355339059e-01, 0.5],
#     [5.0000000000e-01,  1.0355339059e-01, 0.5],
#     [4.2099142644e-01,  2.8611535475e-01, 0.5],
#     [3.5355339059e-01,  3.5355339059e-01, 0.5]
# ]
# curve01.weights = [1.0, 0.9267766953, 0.85355339059, 0.85355339059, 0.9267766953, 1.0]
# curve01.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve01.sample_size = 100
# curve01.evaluate()

# curve_points01 = curve01.evalpts
# x_vals01, y_vals01, z_vals01 = zip(*curve_points01)
# ctrl_x01, ctrl_y01, ctrl_z01 = zip(*curve01.ctrlpts)


# # --- Curva 1-1 ---
# curve11 = NURBS.Curve()
# curve11.degree = 2
# curve11.ctrlpts = [
#     [1.0069052197, -1.0069052197, 0.5],
#     [1.0475821302, -0.7678156108, 0.5],
#     [1.0952380952, -0.26087347369, 0.5],
#     [1.0952380952,  0.26087347369, 0.5],
#     [1.0475821302,  0.7678156108, 0.5],
#     [1.0069052197,  1.0069052197, 0.5]
# ]
# curve11.weights = [1.0]*6
# curve11.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve11.sample_size = 100
# curve11.evaluate()

# curve_points11 = curve11.evalpts
# x_vals11, y_vals11, z_vals11 = zip(*curve_points11)
# ctrl_x11, ctrl_y11, ctrl_z11 = zip(*curve11.ctrlpts)


# # --- Curva 2-1 ---
# curve21 = NURBS.Curve()
# curve21.degree = 2
# curve21.ctrlpts = [
#     [2.0, -2.0, 0.5], 
#     [2.0, -1.5, 0.5], 
#     [2.0, -0.5, 0.5],
#     [2.0,  0.5, 0.5], 
#     [2.0,  1.5, 0.5], 
#     [2.0,  2.0, 0.5]
# ]
# curve21.weights = [1.0]*6
# curve21.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve21.sample_size = 100
# curve21.evaluate()

# curve_points21 = curve21.evalpts
# x_vals21, y_vals21, z_vals21 = zip(*curve_points21)
# ctrl_x21, ctrl_y21, ctrl_z21 = zip(*curve21.ctrlpts)




# # --- Curva 0-2 ---
# curve02 = NURBS.Curve()
# curve02.degree = 2
# curve02.ctrlpts = [
#     [3.5355339059e-01, -3.5355339059e-01, 1.0], 
#     [4.2099142644e-01, -2.8611535475e-01, 1.0],
#     [5.0000000000e-01, -1.0355339059e-01, 1.0],
#     [5.0000000000e-01,  1.0355339059e-01, 1.0],
#     [4.2099142644e-01,  2.8611535475e-01, 1.0],
#     [3.5355339059e-01,  3.5355339059e-01, 1.0]
# ]
# curve02.weights = [1.0, 0.9267766953, 0.85355339059, 0.85355339059, 0.9267766953, 1.0]
# curve02.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve02.sample_size = 100
# curve02.evaluate()

# curve_points02 = curve02.evalpts
# x_vals02, y_vals02, z_vals02 = zip(*curve_points02)
# ctrl_x02, ctrl_y02, ctrl_z02 = zip(*curve02.ctrlpts)


# # --- Curva 1-2 ---
# curve12 = NURBS.Curve()
# curve12.degree = 2
# curve12.ctrlpts = [
#     [1.0069052197, -1.0069052197, 1.0],
#     [1.0475821302, -0.7678156108, 1.0],
#     [1.0952380952, -0.26087347369, 1.0],
#     [1.0952380952,  0.26087347369, 1.0],
#     [1.0475821302,  0.7678156108, 1.0],
#     [1.0069052197,  1.0069052197, 1.0]
# ]
# curve12.weights = [1.0]*6
# curve12.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve12.sample_size = 100
# curve12.evaluate()

# curve_points12 = curve12.evalpts
# x_vals12, y_vals12, z_vals12 = zip(*curve_points12)
# ctrl_x12, ctrl_y12, ctrl_z12 = zip(*curve12.ctrlpts)


# # --- Curva 2-2 ---
# curve22 = NURBS.Curve()
# curve22.degree = 2
# curve22.ctrlpts = [
#     [2.0, -2.0, 1.0], 
#     [2.0, -1.5, 1.0], 
#     [2.0, -0.5, 1.0],
#     [2.0,  0.5, 1.0], 
#     [2.0,  1.5, 1.0], 
#     [2.0,  2.0, 1.0]
# ]
# curve22.weights = [1.0]*6
# curve22.knotvector = [0, 0, 0, 0.25, 0.5, 0.75, 1, 1, 1]
# curve22.sample_size = 100
# curve22.evaluate()

# curve_points22 = curve22.evalpts
# x_vals22, y_vals22, z_vals22 = zip(*curve_points22)
# ctrl_x22, ctrl_y22, ctrl_z22 = zip(*curve22.ctrlpts)



# # --- PLOT 3D ---
# fig = plt.figure(figsize=(6, 6))
# ax = fig.add_subplot(111, projection='3d')

# # # Curvas avaliadas
# # ax.plot(x_vals, y_vals, z_vals, color='red', linewidth=2)
# # ax.plot(x_vals1, y_vals1, z_vals1, color='green', linewidth=2)
# # ax.plot(x_vals2, y_vals2, z_vals2, color='blue', linewidth=2)

# # Pontos de controle (com linhas conectando)
# for cx, cy, cz in [(ctrl_x, ctrl_y, ctrl_z),
#                    (ctrl_x1, ctrl_y1, ctrl_z1),
#                    (ctrl_x2, ctrl_y2, ctrl_z2),
#                    (ctrl_x01, ctrl_y01, ctrl_z01),
#                    (ctrl_x11, ctrl_y11, ctrl_z11),
#                    (ctrl_x21, ctrl_y21, ctrl_z21),
#                    (ctrl_x02, ctrl_y02, ctrl_z02),
#                    (ctrl_x12, ctrl_y12, ctrl_z12),
#                    (ctrl_x22, ctrl_y22, ctrl_z22),
#                    ]:
#     ax.plot(cx, cy, cz, color='black', linewidth=0.5,
#             marker='o', markersize=6, markerfacecolor='blue', markeredgecolor='blue')

# # Conectar pontos radialmente
# num_points = len(ctrl_x)
# for i in range(num_points):
#     x_line = [ctrl_x[i], ctrl_x1[i], ctrl_x2[i]]
#     y_line = [ctrl_y[i], ctrl_y1[i], ctrl_y2[i]]
#     z_line = [ctrl_z[i], ctrl_z1[i], ctrl_z2[i]]
#     ax.plot(x_line, y_line, z_line, color='black', linewidth=0.5)


# for i in range(num_points):
#     x_line = [ctrl_x01[i], ctrl_x11[i], ctrl_x21[i]]
#     y_line = [ctrl_y01[i], ctrl_y11[i], ctrl_y21[i]]
#     z_line = [ctrl_z01[i], ctrl_z11[i], ctrl_z21[i]]
#     ax.plot(x_line, y_line, z_line, color='black', linewidth=0.5)

# for i in range(num_points):
#     x_line = [ctrl_x02[i], ctrl_x12[i], ctrl_x22[i]]
#     y_line = [ctrl_y02[i], ctrl_y12[i], ctrl_y22[i]]
#     z_line = [ctrl_z02[i], ctrl_z12[i], ctrl_z22[i]]
#     ax.plot(x_line, y_line, z_line, color='black', linewidth=0.5)




# num_points = len(ctrl_z)

# num_points = len(ctrl_z)
# for i in range(num_points):
#     x_line = [ctrl_x[i], ctrl_x01[i], ctrl_x02[i]]
#     y_line = [ctrl_y[i], ctrl_y01[i], ctrl_y02[i]]
#     z_line = [ctrl_z[i], ctrl_z01[i], ctrl_z02[i]]
#     ax.plot(x_line, y_line, z_line, color='black', linewidth=0.5)


# for i in range(num_points):
#     x_line = [ctrl_x1[i], ctrl_x11[i], ctrl_x12[i]]
#     y_line = [ctrl_y1[i], ctrl_y11[i], ctrl_y12[i]]
#     z_line = [ctrl_z1[i], ctrl_z11[i], ctrl_z12[i]]
#     ax.plot(x_line, y_line, z_line, color='black', linewidth=0.5)

# for i in range(num_points):
#     x_line = [ctrl_x2[i], ctrl_x21[i], ctrl_x22[i]]
#     y_line = [ctrl_y2[i], ctrl_y21[i], ctrl_y22[i]]
#     z_line = [ctrl_z2[i], ctrl_z21[i], ctrl_z22[i]]
#     ax.plot(x_line, y_line, z_line, color='black', linewidth=0.5)



# #set_axes_equal(ax)
# ax.grid(False)
# ax.set_xticks([])
# ax.set_yticks([])
# ax.set_zticks([])
# ax.set_axis_off()
# plt.show()





