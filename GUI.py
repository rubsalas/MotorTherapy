import pygame

# Inicializa Pygame y todos sus modulos
pygame.init()

# Medidas de la ventana
displayWidth = 1000
displayHeight = 650
displaySeparation = 16

# Medidas de cuadro de seleccion de menu principal
selectionWidth = (displayWidth - 75 - displaySeparation * 3) // 2
selectionHeight = (displayHeight - displaySeparation * 3) // 2

# Medidas de cuadro de settings de menu principal
settingsWidth = 100 - displaySeparation * 2.5
settingsHeight = displayHeight - displaySeparation * 2

# Posiciones de cuadros de seleccion de menu principal
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

# Medidas de cuadros en Menu por Juego
game_window_separation = displayHeight // 8
game_title_width = displayWidth - (game_window_separation * 2)
game_title_height = game_window_separation * 3
game_option_width = (game_title_width - game_window_separation) // 2
game_option_height = game_window_separation * 2

# Posiciones de cuadros en Menu por Juego
xTitulo = game_window_separation
yTitulo = game_window_separation

xOption_left = game_window_separation
yOption_left = game_window_separation * 5

xOption_right = game_window_separation * 2 + game_option_width
yOption_right = game_window_separation * 5

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


# Muestra los rectangulos de las opciones en menu principal
def show_main_options():
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
def main_selection(m_x, m_y):
    in_place = False

    if xUL <= m_x <= (xUL + selectionWidth) and yUL <= m_y <= (yUL + selectionHeight):
        in_place = True
        print("UL: Raqueta Globo")
        show_game_menu("rg")
        # show_rg_menu()
        # run_ul()

    elif xUR <= m_x <= (xUR + selectionWidth) and yUR <= m_y <= (yUR + selectionHeight):
        in_place = True
        print("UR: Usando los Pies")
        show_game_menu("up")
        # show_up_menu()
        # run_up()

    elif xDL <= m_x <= (xDL + selectionWidth) and yDL <= m_y <= (yDL + selectionHeight):
        in_place = True
        print("DL: Telaraña")
        show_game_menu("ta")
        # show_ta_menu()
        # run_dl()

    elif xDR <= m_x <= (xDR + selectionWidth) and yDR <= m_y <= (yDR + selectionHeight):
        in_place = True
        print("DR: Alcanzando el Objetivo")
        show_game_menu("ao")
        # show_ao_menu()
        # run_dr()

    elif xS <= m_x <= (xS + settingsWidth) and yS <= m_y <= (yS + settingsHeight):
        in_place = True
        print("S")
        run_s()

    else:
        print("Not an option")

    return in_place


# Muestra el menu de cada juego
def show_game_menu(game):

    print(game + ": Menu")

    # Superficie del menu
    game_menu_surface = pygame.Surface((displayWidth, displayHeight))

    # Flag para mantener el menu del juego corriendo
    running_game_menu = True

    while running_game_menu:

        # Background Color
        game_menu_surface.fill((255, 155, 55))

        # Muestra la superficie encima de initialWindow
        initialWindow.blit(game_menu_surface, (0, 0))

        # Muestra las opciones del menu
        show_game_menu_options(game)

        # Pygame verifica todos los events
        for event in pygame.event.get():

            # Si se cierra la ventana
            if event.type == pygame.QUIT:
                # Va a salir del while
                running_game_menu = False
                print("QUIT")

            # Al presionar el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtiene las posiciones actuales del mouse
                mousex, mousey = pygame.mouse.get_pos()
                # Verifica si puede ingresar a una opcion
                running_game_menu = game_menu_selection(mousex, mousey, game)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Muestra los cuadros de seleccion del menu del juego XXX xx XXX
def show_game_menu_options(game):

    # Dependiendo del juego mostrara diferentes titulos y layouts de las opciones
    if game == "rg":
        # print("rg")
        True
    elif game == "up":
        # print("up")
        True
    elif game == "ta":
        # print("ta")
        True
    elif game == "ao":
        # print("ao")
        True
    else:
        print("Error in show_game_menu_options(game)")

    # Dibuja un rectangulo -> Titulo
    pygame.draw.rect(initialWindow, (255, 49, 31),
                     (xTitulo, yTitulo, game_title_width, game_title_height))

    # Dibuja un rectangulo -> Start (Izquierda)
    pygame.draw.rect(initialWindow, (67, 255, 52),
                     (xOption_left, yOption_left, game_option_width, game_option_height))

    # Dibuja un rectangulo -> Main Menu (Derecha)
    pygame.draw.rect(initialWindow, (165, 77, 255),
                     (xOption_right, yOption_right, game_option_width, game_option_height))


# Verifica la seleccion en el menu del juego cuando se selecciona
def game_menu_selection(m_x, m_y, game):

    selection = True

    if xOption_left <= m_x <= (xOption_left + game_option_width) and yOption_left <= m_y <= (
            yOption_left + game_option_height):
        # Opcion izquierda
        # Opcion Start

        # Corre el juego al que le pertenece el menu
        if game == "rg":
            run_ul()
        elif game == "up":
            run_up()
        elif game == "ta":
            run_dl()
        elif game == "ao":
            run_dr()
        else:
            print("Error in game_menu_selection(m_x, m_y, game)")

        # Mantiene True el Flag para que al salirse de la ventana del juego vuelva al menu del juego
        selection = True

    elif xOption_right <= m_x <= (xOption_right + game_option_width) and yOption_right <= m_y <= (
            yOption_right + game_option_height):
        # Opcion derecha
        # Opcion Back

        # Hace selection False para retornar al menu principal
        selection = False

    else:
        print("Not an option")

    return selection


###############################################################################
#                                                                             #
#                               RAQUETA GLOBO                                 #
#                                                                             #
###############################################################################


# Variables de Raqueta Globo
rg_alt = 100 * 4
rg_lat = 100 * 2
rg_cantidad = 5
# def balloon
# def Inc
# def Dec

# Largo de balloon
balloon_width = 62 // 1
# Ancho de balloon
balloon_height = 120 // 1


# Corre la seleccion de Raqueta Globo
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

    # Para el sprite del globo
    n = 1

    # Flag del juego
    running = True

    while running:

        # change its background color
        ul_surface.fill((55, 155, 255))

        # blit uLSurface onto the main screen at the position (0, 0)
        initialWindow.blit(ul_surface, (0, 0))

        # Muestra el globo
        place_balloon(rg_alt, rg_lat, n)

        # Para cambiar el sprite del globo
        if n < 2:
            n += 1
        else:
            n = 1

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

        # Parametro serian la cantidad de frames en un segundo (fps)
        clock.tick(6)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Posiciona el globo y muestra el sprite que se necesite
# @param x
# @param y
# @param n: sprite de la bandera
def place_balloon(x, y, n):

    # Directorio de la imagen por mostrar actual
    directory = "Resources/Balloon/balloon" + str(n) + ".png"

    # Imagen cargada
    balloon_n = pygame.image.load(directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    balloon_n = pygame.transform.scale(balloon_n, (balloon_width, balloon_height))  # Escala la imagen al size deseado

    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(balloon_n, (x, y))


def balloon(altura, latitud):
    # Show balloon en (alt,lat)

    n = 1

    hit = False

    while not hit:

        hit = False

        # Check and record hits

        # if hitted
        # + puntaje
        # hit = True


def inc():
    print("Inc")


def dec():
    print("Dec")


###############################################################################
#                                                                             #
#                             USANDO LOS PIES                                 #
#                                                                             #
###############################################################################


# Variables de Usando los Pies
up_colores = ["blanco", "rosado", "rojo", "anaranjado", "amarillo", "verde_claro", "verde_oscuro", "celeste", "azul", "morado"]
up_puntaje = ["", "", "", "", "", "", "", "", "", ""]
up_tiempo = 60
up_cantidad = 3
# def Random
# def Inc
# def Dec


# Largo del sosten de las banderas (cambiar multiplier para cambiar el largo solamente)
stick_width = displayWidth * 0.8
# Altura del sosten de las banderas
stick_y = displayHeight // 2 - 50

# Largo de bandera
flag_width = 80 // 2
# Ancho de bandera
flag_height = 200 // 2
# Largo del espacio por bandera en espacio del sosten
space_per_flag = stick_width // 10


# Corre la seleccion de Up Right: Usando los Pies
def run_up():
    print("Usando los Pies")

    # create a new Surface
    ur_surface = pygame.Surface((displayWidth, displayHeight))

    n = 0

    running = True

    while running:

        # change its background color
        ur_surface.fill((255, 122, 172))

        # blit uLSurface onto the main screen at the position (0, 0)
        initialWindow.blit(ur_surface, (0, 0))

        # Muestra y pone las banderas en pantalla
        place_flags(initialWindow, 10, n)

        # Para iniciar a contar los segundos para seleccionar una opcion con la mano
        if n < 5:
            n += 1
        else:
            n = 0

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
        # pygame.display.update()

        # Parametro serian la cantidad de frames en un segundo (fps)
        clock.tick(10)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Posiciona las banderas en pantalla segun la cantidad que hayan y el tamaño
# de donde estaran posicionadas
# @param display: donde se mostraran las banderas
# @param flag_cant: cantidad de banderas
# @param n: sprite de la bandera
def place_flags(display, flag_cant, n):
    # Posicion en x de la bandera:
    #   (Mitad del espacio que sobra del display )
    #    + (Mitad del espacio donde estaran las banderas)
    #    - (Mitad del space_per_flag por bandera que exista)
    #    + (Espacio sobrante en space_per_flag con la bandera, solo de un lado)
    flag_x = ((displayWidth - stick_width) // 2) + (stick_width // 2) - ((space_per_flag * flag_cant) // 2) + (
                (space_per_flag - flag_width) // 2)

    while flag_cant > 0:
        # Directorio de la imagen por mostrar actual
        directory = "Resources/Flags/Flag" + str(flag_cant - 1) + "/F" + str(flag_cant - 1) + str(n) + ".png"

        # Imagen cargada
        flag_n = pygame.image.load(directory)  # Carga la imagen de la carpeta
        # Imagen escalada
        flag_n = pygame.transform.scale(flag_n, (flag_width, flag_height))  # Escala la imagen al size deseado

        # Muestra la imagen en pantalla con las coordenadas preestablecidas
        display.blit(flag_n, (flag_x, stick_y))

        # Aumenta flag_x para la posicion de la siguiente bandera
        flag_x = flag_x + space_per_flag

        # Cantidad de banderas restantes por mostrar
        flag_cant = flag_cant - 1


###############################################################################
#                                                                             #
#                                  TELARAÑA                                   #
#                                                                             #
###############################################################################


# Variables de Telaraña
ta_mi_arreglo = ["", "", "", "", ""]
ta_mi_puntaje = ["", "", "", "", ""]
ta_mi_fila = 5
ta_mi_col = 5


# Corre la seleccion de Down Left
def run_dl():
    print("Telaraña")

    # create a new Surface
    dl_surface = pygame.Surface((displayWidth, displayHeight))

    running = True

    while running:

        # change its background color
        dl_surface.fill((85, 255, 150))

        # blit uLSurface onto the main screen at the position (0, 0)
        initialWindow.blit(dl_surface, (0, 0))

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





###############################################################################
#                                                                             #
#                           Alcanzando el Objetivo                            #
#                                                                             #
###############################################################################

#Variables de Alcanzando el Objetivo
ao_object_x = 400
ao_object_y = 200

# Corre la seleccion de Down Right
def run_dr():
    print("Alcanzando el Objetivo")

    # create a new Surface
    dr_surface = pygame.Surface((displayWidth, displayHeight))

    # Para el sprite del object
    n = 1

    running = True

    while running:

        # change its background color
        dr_surface.fill((85, 255, 0))

        # blit uLSurface onto the main screen at the position (0, 0)
        initialWindow.blit(dr_surface, (0, 0))

        # Muestra el globo
        place_object(ao_object_x, ao_object_y, n)

        # Para cambiar el sprite del globo
        if n < 2:
            n += 1
        else:
            n = 1

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

        # Parametro serian la cantidad de frames en un segundo (fps)
        clock.tick(6)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Posiciona el objeto y muestra el sprite que se necesite
# @param x
# @param y
# @param n: sprite del objeto
def place_object(x, y, n):

    # Directorio de la imagen por mostrar actual
    directory = "Resources/Balloon/balloon" + str(n) + ".png"

    # Imagen cargada
    balloon_n = pygame.image.load(directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    balloon_n = pygame.transform.scale(balloon_n, (balloon_width, balloon_height))  # Escala la imagen al size deseado

    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(balloon_n, (x, y))


# Corre la seleccion de Settings
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


# n = 1

# Flag
playing = True

# Loop
while playing:

    # Cambia el fondo de la superficie
    initialWindow.fill(black)

    # Muestra las posibles cuadros de las opciones de los juegos
    show_main_options()

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
            main_selection(mousex, mousey)

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
