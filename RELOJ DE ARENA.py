import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ============================
# 1. DEFINIR LOS VÉRTICES DEL RELOJ
# ============================

A = (0, 0, 2)
B = (1, 0, 2)
C = (1, 1, 2)
D = (0, 1, 2)
E = (0.38, 0.38, 1)
F = (0.62, 0.38, 1)
G = (0.62, 0.62, 1)
H = (0.38, 0.62, 1)
I = (0, 0, 0)
J = (1, 0, 0)
K = (1, 1, 0)
L = (0, 1, 0)

vertices = [A, B, C, D, E, F, G, H, I, J, K, L]

# ============================
# 2. CREAR LA FIGURA 3D
# ============================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  

# ============================
# 3. DIBUJAR EL VIDRIO TRANSLÚCIDO
# ============================

caras_vidrio = [
    [A, B, F, E], [B, C, G, F], [C, D, H, G], [D, A, E, H],
    [E, F, J, I], [F, G, K, J], [G, H, L, K], [H, E, I, L],
    [A, B, C, D], [I, J, K, L]
]

vidrio = Poly3DCollection(
    caras_vidrio,
    alpha=0.2,
    facecolor="lightcyan",
    edgecolor="steelblue",
    linewidth=1.5
)

ax.add_collection3d(vidrio)

# La arena forma un embudo en la cámara superior y un montón abajo.
arena_superior = [
    [(0.5, 0.5, 1.05), (0.35, 0.35, 1.45), (0.65, 0.35, 1.45)],
    [(0.5, 0.5, 1.05), (0.65, 0.35, 1.45), (0.65, 0.65, 1.45)],
    [(0.5, 0.5, 1.05), (0.65, 0.65, 1.45), (0.35, 0.65, 1.45)],
    [(0.5, 0.5, 1.05), (0.35, 0.65, 1.45), (0.35, 0.35, 1.45)],
    [(0.35, 0.35, 1.45), (0.65, 0.35, 1.45), (0.65, 0.65, 1.45), (0.35, 0.65, 1.45)]
]

arena_inferior = [
    [(0.5, 0.5, 0.92), (0.1, 0.1, 0.08), (0.9, 0.1, 0.08)],
    [(0.5, 0.5, 0.92), (0.9, 0.1, 0.08), (0.9, 0.9, 0.08)],
    [(0.5, 0.5, 0.92), (0.9, 0.9, 0.08), (0.1, 0.9, 0.08)],
    [(0.5, 0.5, 0.92), (0.1, 0.9, 0.08), (0.1, 0.1, 0.08)],
    [(0.1, 0.1, 0.08), (0.9, 0.1, 0.08), (0.9, 0.9, 0.08), (0.1, 0.9, 0.08)]
]

for caras_arena in [arena_superior, arena_inferior]:
    ax.add_collection3d(
        Poly3DCollection(caras_arena, alpha=0.9, facecolor="goldenrod", edgecolor="peru")
    )

ax.plot([0.5, 0.5], [0.5, 0.5], [1.02, 0.94], color="peru", linewidth=3)

# ============================
# 4. DIBUJAR LOS VÉRTICES
# ============================

for nombre, vertice in zip("ABCDEFGHIJKL", vertices):

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
    (I, J), (J, K), (K, L), (L, I),
    (A, E), (B, F), (C, G), (D, H),
    (E, I), (F, J), (G, K), (H, L)
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

ax.set_xlim(-0.15, 1.15)
ax.set_ylim(-0.15, 1.15)
ax.set_zlim(-0.1, 2.1)
ax.set_box_aspect((1, 1, 2))
ax.view_init(elev=24, azim=35)

ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
ax.set_zlabel("Eje Z")

ax.set_title(
    "Reloj de arena en 3D"
)

plt.show()