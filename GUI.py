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

# Surface principal
initialWindow = pygame.display.set_mode((displayWidth, displayHeight))

# Titulo de la Ventana
pygame.display.set_caption("MotorTherapy")

# Colores en RGB (R,G,B)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Reloj que controla el tiempo para animaciones y logica, fps
clock = pygame.time.Clock()

# Frames per Second para Clock
fps = 60

# Variables de Raqueta Globo
rg_alt = 2
rg_lat = 4
rg_cantidad = 5
#def Balloon
#def Inc
#def Dec

# Variables de Usando los Pies
up_colores = ["", "", "", "", "", "", "", "", "", ""]
up_puntaje = ["", "", "", "", "", "", "", "", "", ""]
up_tiempo = 60
up_cantidad = 3
#def Random
#def Inc
#def Dec

# Variables de Telaraña
ta_mi_arreglo = ["", "", "", "", ""]
ta_mi_puntaje = ["", "", "", "", ""]
ta_mi_fila = 5
ta_mi_col = 5

# Variables de Alcanzando el Objetivo
ao_altura = 2
ao_distancias = [2, 5, 1, 7, 1]
ao_tiempo = 25
#def Object

# Muestra los rectangulos de las opciones en menu principal
def show_rects():
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


# Verifica en que seccion se encuentra posicionado para seleccionarlo
# @param m_x : Posicion en x
# @param m_y : Posicion en y
def in_selection(m_x, m_y):

    in_place = False

    if xUL <= m_x <= (xUL + selectionWidth) and yUL <= m_y <= (yUL + selectionHeight):
        in_place = True
        print("UL: Raqueta Globo")
        run_ul()

    elif xUR <= m_x <= (xUR + selectionWidth) and yUR <= m_y <= (yUR + selectionHeight):
        in_place = True
        print("UR: Usando los Pies")
        run_ur()

    elif xDL <= m_x <= (xDL + selectionWidth) and yDL <= m_y <= (yDL + selectionHeight):
        in_place = True
        print("DL: Telaraña")
        run_dl()

    elif xDR <= m_x <= (xDR + selectionWidth) and yDR <= m_y <= (yDR + selectionHeight):
        in_place = True
        print("DR: Alcanzando el Objetivo")
        run_dr()

    elif xS <= m_x <= (xS + settingsWidth) and yS <= m_y <= (yS + settingsHeight):
        in_place = True
        print("S")
        run_s()

    else:
        print("Not an option")

    return in_place


# Raqueta Globo
# Corre la seleccion de Up Left
def run_ul():  # alt, _lat):

    print("Raqueta Globo")

    # Altura del Globo
    # alt = _alt
    # lat = _lat

    # create a new Surface
    ul_surface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    ul_surface.fill((55, 155, 255))

    # blit ul_surface onto the main screen at the position (0, 0)
    initialWindow.blit(ul_surface, (0, 0))

    pygame.font.init()  # you have to call this at the start,
    # if you want to use this module.
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    textsurface = myfont.render('Some Text', False, (0, 0, 0))

    ul_surface.blit(textsurface, (50,50))

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


        Balloon(rg_alt,rg_cantidad)



        # Update display (Actualiza _todo el surface)
        pygame.display.update()


def Balloon(altura, latitud):

    # Show Balloon en (alt,lat)

    hit = False

    while not hit:

        hit = True

        # Check and record hits

        # if hitted
            # + puntaje
            # hit = True






# Corre la seleccion de Up Right: Usando los Pies
def run_ur():

    print("Usando los Pies")

    # create a new Surface
    ur_surface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    ur_surface.fill((255, 122, 172))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(ur_surface, (0, 0))

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
def run_dl():

    print("Telaraña")

    # create a new Surface
    dl_surface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    dl_surface.fill((85, 255, 150))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(dl_surface, (0, 0))

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
def run_dr():

    print("Alcanzando el Objetivo")

    # create a new Surface
    dr_surface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    dr_surface.fill((85, 255, 150))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(dr_surface, (0, 0))

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
def run_s():

    print("Settings")

    # create a new Surface
    s_surface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    s_surface.fill((0, 0, 255))

    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(s_surface, (0, 0))

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
playing = True

# Loop
while playing:

    # Cambia el fondo de la superficie
    initialWindow.fill(black)

    # Muestra las posibles cuadros de las opciones de los juegos
    show_rects()

    # Pygame verifica todos los events
    for event in pygame.event.get():

        # Si se cierra la ventana
        if event.type == pygame.QUIT:
            # Va a salir del while
            playing = False
            print("QUIT")

        # Al presionar el mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtiene las posiciones actuales del mouse
            mousex, mousey = pygame.mouse.get_pos()
            # Verifica si puede ingresar a una opcion
            in_selection(mousex, mousey)

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
