import pygame

# Inicializa Pygame y todos sus modulos
pygame.init()

# Variables
displayWidth = 800
displayHeight = 600

# Colores en RGB (tu,plas)

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Surface principal
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

# Titulo de la Ventana
pygame.display.set_caption("Test")

# Reloj que controla el tiempo para animaciones y logica, fps
clock = pygame.time.Clock()

# Imagen
carImage = pygame.image.load("Resources/car.png")  # Carga la imagen de la carpeta
carImage = pygame.transform.scale(carImage, (850//8, 422//8))  # Escala la imagen a el size deseado
carImage = pygame.transform.rotate(carImage, 90)  # Rota la imagen en grados


# Mueve el carro a la posicion x y y deseada
def car(x, y):
    # Muestra en la superficie lo que se ingrese .blit(porIngresar, (x,y))
    gameDisplay.blit(carImage, (x, y))


# Posiciones iniciales
xo = displayWidth * 0.45
yo = displayHeight * 0.8

# Cambios de posicion
dx = 0
dy = 0

# Flag
crashed = False

# Loop
while not crashed:

    # Pygame verifica todos los events
    for event in pygame.event.get():

        # Si se cierra la ventana
        if event.type == pygame.QUIT:
            # Va a salir del while
            crashed = True
            print("QUIT")

        # Si se presiona una tecla
        if event.type == pygame.KEYDOWN:
            # Cambia la direccion del movimiento
            if event.key == pygame.K_LEFT:  # T. Izquierda
                dx = -5
            if event.key == pygame.K_RIGHT:  # T. Derecha
                dx = 5

        # Si se suelta una tecla
        if event.type == pygame.KEYUP:
            # Retorna el movimiento a 0, lo hace estatico de nuevo
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # T. Izquierda o T. Derecha
                dx = 0

    # Cambia la posicion actual del objeto
    xo += dx

    # Cambia el fondo de la superficie
    gameDisplay.fill(white)

    # Actualiza la posicion de la imagen
    car(xo, yo)

    # Update display (Actualiza _todo el surface)
    pygame.display.update()

    # Parametro serian la cantidad de frames en un segundo (fps)
    clock.tick(100)

# Deja de correr Pygame
pygame.quit()
