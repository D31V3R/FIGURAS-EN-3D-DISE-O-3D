import math
from tkinter import Canvas, Tk

# Vértices 3D del modelo de Steve (Cabeza, Torso y Brazos)
# Formato: [X, Y, Z]
vertices = [
    # Cabeza (Cubo superior)
    [-0.5, 0.5, -0.5],
    [0.5, 0.5, -0.5],
    [0.5, 1.5, -0.5],
    [-0.5, 1.5, -0.5],
    [-0.5, 0.5, 0.5],
    [0.5, 0.5, 0.5],
    [0.5, 1.5, 0.5],
    [-0.5, 1.5, 0.5],
    # Torso (Cubo central)
    [-0.5, -0.7, -0.3],
    [0.5, -0.7, -0.3],
    [0.5, 0.5, -0.3],
    [-0.5, 0.5, -0.3],
    [-0.5, -0.7, 0.3],
    [0.5, -0.7, 0.3],
    [0.5, 0.5, 0.3],
    [-0.5, 0.5, 0.3],
    # Brazo Izquierdo
    [-0.9, -0.7, -0.2],
    [-0.5, -0.7, -0.2],
    [-0.5, 0.5, -0.2],
    [-0.9, 0.5, -0.2],
    # Brazo Derecho
    [0.5, -0.7, -0.2],
    [0.9, -0.7, -0.2],
    [0.9, 0.5, -0.2],
    [0.5, 0.5, -0.2],
]

# Líneas que unen las esquinas de cada cubo
aristas = [
    # Cabeza
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
    # Torso
    (8, 9),
    (9, 10),
    (10, 11),
    (11, 8),
    (12, 13),
    (13, 14),
    (14, 15),
    (15, 12),
    (8, 12),
    (9, 13),
    (10, 14),
    (11, 15),
    # Brazos
    (16, 17),
    (17, 18),
    (18, 19),
    (19, 16),
    (20, 21),
    (21, 22),
    (22, 23),
    (23, 20),
]

angulo = 0


def animar():
  global angulo
  angulo += 0.03
  canvas.delete("all")

  puntos_2d = []
  for x, y, z in vertices:
    # Rotación en el eje Y
    x_rot = x * math.cos(angulo) - z * math.sin(angulo)
    z_rot = x * math.sin(angulo) + z * math.cos(angulo)

    # Proyección ortográfica a 2D
    px = 250 + int(x_rot * 90)
    py = 230 - int(y * 90)
    puntos_2d.append((px, py))

  # Dibujar las aristas del personaje
  for a, b in aristas:
    # Si la línea pertenece a la cabeza la pintamos marrón/piel, si es cuerpo azul cyan
    color_linea = "#5c4033" if a < 8 or b < 8 else "#00a8a8"
    canvas.create_line(
        puntos_2d[a][0],
        puntos_2d[a][1],
        puntos_2d[b][0],
        puntos_2d[b][1],
        fill=color_linea,
        width=3,
    )

  # Ojos icónicos de Steve (en la cara frontal)
  if math.cos(angulo) > -0.2:  # Mostrar solo cuando mira al frente
    p_ref = puntos_2d[0]
    canvas.create_rectangle(
        p_ref[0] + 15,
        p_ref[1] - 50,
        p_ref[0] + 25,
        p_ref[1] - 40,
        fill="#0000aa",
    )
    canvas.create_rectangle(
        p_ref[0] + 45,
        p_ref[1] - 50,
        p_ref[0] + 55,
        p_ref[1] - 40,
        fill="#0000aa",
    )

  root.after(30, animar)


# Crear ventana
root = Tk()
root.title("Steve 3D - Minecraft")
canvas = Canvas(root, width=500, height=500, bg="#1e1e1e")
canvas.pack()

animar()
root.mainloop()