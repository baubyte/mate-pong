# Importamos Turtle para poder realizar gráficos
import turtle
# Importamos Time para poder controlar el tiempo
import time
# Importamos Threading para poder realizar tareas en segundo plano
import threading
# Importamos Playsound para poder dar efectos de sonido
from playsound import playsound

# Area para el Juego (tablero)
ventana = turtle.Screen()
ventana.title("MatePong")
#ventana.bgcolor("#159e4a")
ventana.bgpic("./img/mateImg.png")
ventana.setup(width=800, height=640)
#Deshabilitar maximizar
ventana.cv._rootwindow.resizable(False, False)
ventana.tracer(0)

# Para el Marcador
puntosA = 0
puntosB = 0

# Paleta A definimos todos los atributos para la paleta
# Creamos la paleta
mateA = turtle.Turtle()
# Velocidad
mateA.speed(0)
# Forma
mateA.shape("circle")
# Color
mateA.color("white")
# Ancho y Alto
mateA.shapesize(stretch_wid=5, stretch_len=1)
# Dibujamos la paleta
mateA.penup()
# Movemos el lápiz
mateA.goto(-380, 0)

# Paleta B definimos todos los atributos para la paleta
# Creamos la paleta
mateB = turtle.Turtle()
# Velocidad
mateB.speed(0)
# Forma
mateB.shape("circle")
# Color
mateB.color("red")
# Ancho y Alto
mateB.shapesize(stretch_wid=5, stretch_len=1)
# Dibujamos la paleta
mateB.penup()
# Movemos el lápiz
mateB.goto(380, 0)

# Definimos la linea para dividir el tablero
# Creamos la linea
linea = turtle.Turtle()
# Velocidad
linea.speed(0)
# Forma
linea.shape("square")
# Color
linea.color("white")
# Ancho y Alto
linea.shapesize(stretch_wid=30, stretch_len=0.07)
# Dibujamos la linea
linea.penup()
# Movemos el lápiz
linea.goto(0, 0)

# Definimos la pelota
# Creamos la pelota
pelota = turtle.Turtle()
# Velocidad
pelota.speed(0)
# Forma
pelota.shape("circle")
# Color
pelota.color("#95e11e")
# Dibujamos la pelota
pelota.penup()
# Movemos el lápiz
pelota.goto(0, 0)
# Definimos el espacio en pixeles que tanto en el eje X como Y
# con las variables dx y dy
pelota.dx = 1.1
pelota.dy = 1.1
# Variable que usaremos para cambiar el estado de la pelota
static = True

# Definimos el Marcador Inicial
# Creamos el marcador
marcadorInicial = turtle.Turtle()
# Velocidad
marcadorInicial.speed(0)
# Color
marcadorInicial.color("white")
# Dibujamos la marcadorInicial
marcadorInicial.penup()
# Escondemos a Turtle
marcadorInicial.hideturtle()
# Movemos el lápiz
marcadorInicial.goto(-2.5, 260)
# Escribimos el Marcador
marcadorInicial.write("Mate A: 0 Mate B: 0", align="center",
                      font=("Fixedsys", 20, "bold"))

# Definimos el Mensaje Inicial
# Creamos el mensaje
mensaje = turtle.Turtle()
# Velocidad
mensaje.speed(0)
# Color
mensaje.color("white")
# Dibujamos la mensaje
mensaje.penup()
# Escondemos a Turtle
mensaje.hideturtle()
# Movemos el lápiz
mensaje.goto(0, -260)
# Escribimos el Marcador
mensaje.write("PRESIONA ENTER Y COMENZAMOS",
              align="center", font=("Fixedsys", 20, "bold"))


"""
    Pasamos a Definir todas las funciones que manejaran el movimientos de la palatas
    y la pelota.
"""

# Mover paleta "A" hacia arriba
def mateAup():
    # Obtenemos la coordenada actual
    y = mateA.ycor()
# Comprobamos que sea menor o igual a 240
    if y <= 240:
        y += 50
        # Seteamos la posición
        mateA.sety(y)

# Mover paleta "A" hacia abajo
def mateAdown():
    # Obtenemos la coordenada actual
    y = mateA.ycor()
# Comprobamos que sea mayor o igual a -220
    if y >= -220:
        y -= 50
        # Seteamos la posición
        mateA.sety(y)

# Mover paleta "B" hacia arriba
def mateBup():
    # Obtenemos la coordenada actual
    y = mateB.ycor()
# Comprobamos que sea menor o igual a 240
    if y <= 240:
        y += 50
        # Seteamos la posición
        mateB.sety(y)

# Mover paleta "B" hacia abajo
def mateBdown():
    # Obtenemos la coordenada actual
    y = mateB.ycor()
# Comprobamos que sea mayor o igual a -220
    if y >= -220:
        y -= 50
        # Seteamos la posición
        mateB.sety(y)

# Funcion para reproducir el sonido
def playSound(sonido):
    playsound("./sounds/"+sonido+".mp3")

# Funcion para realizar la tarea en segundo plano
def initPlaySound(sonido):
    # Creamos una tarea
    tarea = threading.Thread(target=lambda:playSound(sonido))
    # Comenzamos la tarea
    tarea.start()

# Funcion para iniciar el juego
def initGame():
    # Variable global
    global static
    static = False
    mensaje.clear()

# Funcion para limpiar la pantalla luego de cada punto
def resetScreen():
    pelota.goto(0, 0)
    pelota.dx *= -1
    mensaje.write("PRESIONA ENTER Y COMENZAMOS",
                  align="center", font=("Fixedsys", 20, "bold"))
    mateA.goto(-380, 0)
    mateB.goto(380, 0)

# Funcion para actualizar el tanteador
def updateScore():
    marcadorInicial.clear()
    marcadorInicial.write("Mate A: {} Mate B: {}".format(
        puntosA, puntosB), align="center", font=("Fixedsys", 20, "bold"))


# Escuchamos los eventos del teclado
ventana.listen()
ventana.onkeypress(mateAup, "w")
ventana.onkeypress(mateAdown, "s")
ventana.onkeypress(mateBup, "Up")
ventana.onkeypress(mateBdown, "Down")
ventana.onkeypress(initGame, "Return")

# Comenzamos toda la lógica del juego
while True:
    try:
        ventana.update()
        
        # Mueve la Pelota
        if static == False:
            pelota.setx(pelota.xcor() + pelota.dx)
            pelota.sety(pelota.ycor() + pelota.dy)
        # Rebote en el márgen superior
        if pelota.ycor() > 290:
            pelota.sety(290)
            pelota.dy *= -1
            initPlaySound("pong")
        # Rebote en el márgen inferior
        if pelota.ycor() < -290:
            pelota.sety(-290)
            pelota.dy *= -1
            initPlaySound("pong")
        #Pelota sobrepasa mateB
        if pelota.xcor() > 390:
            puntosA += 1
            updateScore()
            static = True
            initPlaySound("point")
            time.sleep(1)
            resetScreen()
        #Pelota sobrepasa mateA
        if pelota.xcor() < -390:
            puntosB += 1
            updateScore()
            static = True
            initPlaySound("point")
            time.sleep(1)
            resetScreen()
        #Rebote en mateB
        if (pelota.xcor() > 370 and pelota.xcor() < 380) and (pelota.ycor() < mateB.ycor() + 50 and pelota.ycor() > mateB.ycor() - 50):
            pelota.setx(370)
            pelota.dx *= -1
            initPlaySound("pong")
        #Rebote en mateA
        if (pelota.xcor() < -370 and pelota.xcor() > -380) and (pelota.ycor() < mateA.ycor() + 50 and pelota.ycor() > mateA.ycor() - 50):
            pelota.setx(-370)
            pelota.dx *= -1
            initPlaySound("pong")
    except:
        break
