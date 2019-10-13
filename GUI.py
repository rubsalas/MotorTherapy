import pygame

# Inicializa Pygame y todos sus modulos
pygame.init()

# Medidas de la ventana
displayWidth = 1000
displayHeight = 650
displaySeparation = 16

# Medidas de cuadro de seleccion
selectionWidth = (displayWidth - 75 - displaySeparation * 3) // 2
selectionHeight = (displayHeight - displaySeparation * 3) // 2

# Medidas de cuadro de settings
settingsWidth = 100 - displaySeparation * 2.5
settingsHeight = displayHeight - displaySeparation * 2

# Posiciones de cuadros de seleccion
xUL = displaySeparation
yUL = displaySeparation

xUR = displaySeparation * 2 + selectionWidth
yUR = displaySeparation

xDL = displaySeparation
yDL = displaySeparation * 2 + selectionHeight

xDR = displaySeparation * 2 + selectionWidth
yDR = displaySeparation * 2 + selectionHeight

xS = displaySeparation * 3 + selectionWidth * 2
yS = displaySeparation

# Frames per Second para Clock
fps = 60


# Verifica en que seccion se encuentra posicionado para seleccionarlo
def inSelection(mX, mY):

    inPlace = False

    if xUL <= mX <= (xUL + selectionWidth) and yUL <= mY <= (yUL + selectionHeight):
        inPlace = True
        print("UL: Raqueta Globo")
        runUL()

    elif xUR <= mX <= (xUR + selectionWidth) and yUR <= mY <= (yUR + selectionHeight):
        inPlace = True
        print("UR: Usando los Pies")
        runUR()

    elif xDL <= mX <= (xDL + selectionWidth) and yDL <= mY <= (yDL + selectionHeight):
        inPlace = True
        print("DL: Telaraña")
        runDL()

    elif xDR <= mX <= (xDR + selectionWidth) and yDR <= mY <= (yDR + selectionHeight):
        inPlace = True
        print("DR: Alcanzando el Objetivo")
        runDR()

    elif xS <= mX <= (xS + settingsWidth) and yS <= mY <= (yS + settingsHeight):
        inPlace = True
        print("S")
        runS()

    else:
        print("Not an option")

    return inPlace


# Colores en RGB (R,G,B)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Surface principal
initialWindow = pygame.display.set_mode((displayWidth, displayHeight))

# Titulo de la Ventana
pygame.display.set_caption("MotorTherapy")

# Reloj que controla el tiempo para animaciones y logica, fps
clock = pygame.time.Clock()


# Muestra los rectangulos de las opciones en menu principal
def showRects():
    # Dibuja un rectangulo -> Arriba izquierda [UL]
    pygame.draw.rect(initialWindow, (255, 49, 31),
                     (xUL, yUL, selectionWidth, selectionHeight))

    # Dibuja un rectangulo -> Arriba derecha [UR]
    pygame.draw.rect(initialWindow, (67, 255, 52),
                     (xUR, yUR, selectionWidth, selectionHeight))

    # Dibuja un rectangulo -> Abajo izquierda [DL]
    pygame.draw.rect(initialWindow, (165, 77, 255),
                     (xDL, yDL, selectionWidth, selectionHeight))

    # Dibuja un rectangulo -> Abajo derecha [DR]
    pygame.draw.rect(initialWindow, (52, 181, 255),
                     (xDR, yDR, selectionWidth, selectionHeight))

    # Dibuja un rectangulo -> Settings [S]
    pygame.draw.rect(initialWindow, (255, 255, 0),
                     (xS, yS, settingsWidth, settingsHeight))


# Corre la seleccion de Up Left: Raqueta Globo
def runUL(): #_alt, _lat):

    print("Raqueta Globo")

    # Altura del Globo
   # alt = _alt
   # lat = _lat

    # create a new Surface
    uLSurface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    uLSurface.fill((55, 155, 255))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(uLSurface, (0, 0))

    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    textsurface = myfont.render('Some Text', False, (0, 0, 0))

    uLSurface.blit(textsurface, (50,50))

    running = True

    while running:

        # Pygame verifica todos los events
        for event in pygame.event.get():

            # Si se cierra la ventana
            if event.type == pygame.QUIT:
                # Va a salir del while
                running = False
                print("QUIT")

            # Al presionar el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Corre la seleccion de Up Right: Usando los Pies
def runUR():

    print("Usando los Pies")

    # create a new Surface
    uRSurface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    uRSurface.fill((255, 122, 172))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(uRSurface, (0, 0))

    running = True

    while running:

        # Pygame verifica todos los events
        for event in pygame.event.get():

            # Si se cierra la ventana
            if event.type == pygame.QUIT:
                # Va a salir del while
                running = False
                print("QUIT")

            # Al presionar el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Corre la seleccion de Down Left
def runDL():

    print("Telaraña")

    # create a new Surface
    dLSurface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    dLSurface.fill((85, 255, 150))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(dLSurface, (0, 0))

    running = True

    while running:

        # Pygame verifica todos los events
        for event in pygame.event.get():

            # Si se cierra la ventana
            if event.type == pygame.QUIT:
                # Va a salir del while
                running = False
                print("QUIT")

            # Al presionar el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Corre la seleccion de Down Right
def runDR():

    print("Alcanzando el Objetivo")

    # create a new Surface
    dRSurface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    dRSurface.fill((85, 255, 150))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(dRSurface, (0, 0))

    running = True

    while running:

        # Pygame verifica todos los events
        for event in pygame.event.get():

            # Si se cierra la ventana
            if event.type == pygame.QUIT:
                # Va a salir del while
                running = False
                print("QUIT")

            # Al presionar el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Corre la seleccion de Down Right
def runS():

    print("Settings")

    # create a new Surface
    sSurface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    sSurface.fill((0, 0, 255))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(sSurface, (0, 0))

    running = True

    while running:

        # Pygame verifica todos los events
        for event in pygame.event.get():

            # Si se cierra la ventana
            if event.type == pygame.QUIT:
                # Va a salir del while
                running = False
                print("QUIT")

            # Al presionar el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = False

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


n = 1

# Flag
crashed = False

# Loop
while not crashed:

    # Cambia el fondo de la superficie
    initialWindow.fill(black)

    # Muestra las posibles cuadros de las opciones de los juegos
    showRects()

    # Pygame verifica todos los events
    for event in pygame.event.get():

        # Si se cierra la ventana
        if event.type == pygame.QUIT:
            # Va a salir del while
            crashed = True
            print("QUIT")

        # Al presionar el mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtiene las posiciones actuales del mouse
            mousex, mousey = pygame.mouse.get_pos()
            # Verifica si puede ingresar a una opcion
            inSelection(mousex, mousey)

    # Update display (Actualiza _todo el surface)
    pygame.display.update()

   # Para iniciar a contar los segundos para seleccionar una opcion con la mano
   # if n < fps:
   #     n += 1
   # else:
   #     n = 0
   # print(str(n))

    # Parametro serian la cantidad de frames en un segundo (fps)
    clock.tick(fps)


# Deja de correr Pygame
pygame.quit()
