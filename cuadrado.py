import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES
# ============================

A = (0, 0, 0)
B = (1, 0, 0)
C = (1, 1, 0)
D = (0, 1, 0)
E = (0, 0, 1)
F = (1, 0, 1)
G = (1, 1, 1)
H = (0, 1, 1)
vertices = [A, B, C, D, E, F, G, H]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  

# ============================
# 3. DIBUJAR LAS SEIS CARAS
# ============================

caras = [
    [A, B, C, D],
    [E, F, G, H],
    [A, B, F, E],
    [B, C, G, F],
    [C, D, H, G],
    [D, A, E, H]
]

coleccion_caras = Poly3DCollection(
    caras,
    alpha=0.4,
    edgecolor="black",
    facecolor="deepskyblue",
    linewidth=1.5
)

ax.add_collection3d(coleccion_caras)

# ============================
# 4. DIBUJAR LOS VÉRTICES
# ============================

for nombre, vertice in zip("ABCDEFGH", vertices):

    x, y, z = vertice

    ax.scatter(x, y, z, s=80)

    ax.text(
        x,
        y,
        z + 0.1,
        nombre,
        fontsize=12
    )

# ============================
# 5. DIBUJAR LAS ARISTAS
# ============================

aristas = [
    (A, B), (B, C), (C, D), (D, A),
    (E, F), (F, G), (G, H), (H, E),
    (A, E), (B, F), (C, G), (D, H)
]

for inicio, fin in aristas:

    ax.plot(
        [inicio[0], fin[0]],
        [inicio[1], fin[1]],
        [inicio[2], fin[2]],
        linewidth=2
    )

# ============================
# 6. CONFIGURAR LA ESCENA
# ============================

ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.set_zlim(-0.2, 1.2)
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=25, azim=35)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.set_title(
    "Cubo en 3D"
)

plt.show()