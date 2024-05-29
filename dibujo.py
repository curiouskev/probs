import turtle

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Dibujando formas con Turtle")

# Crear un objeto turtle
t = turtle.Turtle()
t.pensize(2)
t.speed(3)

# Función para dibujar un círculo
def dibujar_circulo(turtle_obj, radius):
    turtle_obj.circle(radius)

# Función para dibujar un cuadrado
def dibujar_cuadrado(turtle_obj, size):
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.right(90)

# Función para dibujar un triángulo
def dibujar_triangulo(turtle_obj, size):
    for _ in range(3):
        turtle_obj.forward(size)
        turtle_obj.left(120)

# Función para dibujar una estrella
def dibujar_estrella(turtle_obj, size):
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.right(144)

# Dibujar el círculo
t.penup()
t.goto(-150, 100)
t.pendown()
t.color("red")
dibujar_circulo(t, 50)

# Dibujar el cuadrado
t.penup()
t.goto(0, 100)
t.pendown()
t.color("green")
dibujar_cuadrado(t, 100)

# Dibujar el triángulo
t.penup()
t.goto(-150, -50)
t.pendown()
t.color("blue")
dibujar_triangulo(t, 100)

# Dibujar la estrella
t.penup()
t.goto(0, -50)
t.pendown()
t.color("purple")
dibujar_estrella(t, 100)

# Finalizar dibujo
turtle.done()
