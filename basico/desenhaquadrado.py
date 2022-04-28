import turtle

def desenhaQuadrado(t, tam):
    """Faca a tartaruga t desenhar um quadrado de lado tam."""

    for i in range(4):
        t.forward(tam)
        t.left(90)


wn = turtle.Screen()              # Inicializa a janela e seus atributos
wn.bgcolor("lightgreen")

alex = turtle.Turtle()            # cria alex
desenhaQuadrado(alex, 50)         # Chama a função para desenhar um quadrado

wn.exitonclick()