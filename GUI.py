
import pygame
import random
import time
import threading
import socket


# Inicializa Pygame y todos sus modulos
pygame.init()

# Medidas de la ventana
displayWidth = 1000
displayHeight = 650
displaySeparation = 16

# Medidas de cuadro de seleccion de menu principal
selectionWidth = (displayWidth - 75 - displaySeparation * 3) // 2    # 439 px
selectionHeight = (displayHeight - displaySeparation * 3) // 2       # 301 px

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
    # pygame.draw.rect(initialWindow, (255, 49, 31),
    #                 (xUL, yUL, selectionWidth, selectionHeight))

    # Directorio de la imagen por mostrar actual
    rg_directory = "Resources/Menu/Raqueta_Globo_small.png"
    # Imagen cargada
    rg_title = pygame.image.load(rg_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    rg_title = pygame.transform.scale(rg_title, (selectionWidth, selectionHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(rg_title, (xUL, yUL))

    # Dibuja un rectangulo -> Arriba derecha [UR]
    # pygame.draw.rect(initialWindow, (67, 255, 52),
    #                 (xUR, yUR, selectionWidth, selectionHeight))

    # Directorio de la imagen por mostrar actual
    up_directory = "Resources/Menu/Usando_Los_Pies_small.png"
    # Imagen cargada
    up_title = pygame.image.load(up_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    up_title = pygame.transform.scale(up_title, (selectionWidth, selectionHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(up_title, (xUR, yUR))

    # Dibuja un rectangulo -> Abajo izquierda [DL]
    # pygame.draw.rect(initialWindow, (165, 77, 255),
    #                 (xDL, yDL, selectionWidth, selectionHeight))

    # Directorio de la imagen por mostrar actual
    ta_directory = "Resources/Menu/Telarana_small.png"
    # Imagen cargada
    ta_title = pygame.image.load(ta_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    ta_title = pygame.transform.scale(ta_title, (selectionWidth, selectionHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(ta_title, (xDL, yDL))

    # Dibuja un rectangulo -> Abajo derecha [DR]
    # pygame.draw.rect(initialWindow, (52, 181, 255),
    #                 (xDR, yDR, selectionWidth, selectionHeight))

    # Directorio de la imagen por mostrar actual
    ao_directory = "Resources/Menu/Alcanzando_El_Objetivo_small.png"
    # Imagen cargada
    ao_title = pygame.image.load(ao_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    ao_title = pygame.transform.scale(ao_title, (selectionWidth, selectionHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(ao_title, (xDR, yDR))

    # Dibuja un rectangulo -> Settings [S]
    pygame.draw.rect(initialWindow, (255, 255, 255),
                     (xS, yS, settingsWidth, settingsHeight))


# Verifica en que seccion se encuentra posicionado para seleccionarlo
# @param m_x : Posicion en x
# @param m_y : Posicion en y
def main_selection(m_x, m_y):
    in_place = False

    if xUL <= m_x <= (xUL + selectionWidth) and yUL <= m_y <= (yUL + selectionHeight):
        in_place = True
        # print("UL: Raqueta Globo")
        show_game_menu("rg")

    elif xUR <= m_x <= (xUR + selectionWidth) and yUR <= m_y <= (yUR + selectionHeight):
        in_place = True
        # print("UR: Usando los Pies")
        show_game_menu("up")

    elif xDL <= m_x <= (xDL + selectionWidth) and yDL <= m_y <= (yDL + selectionHeight):
        in_place = True
        # print("DL: Telaraña")
        show_game_menu("ta")

    elif xDR <= m_x <= (xDR + selectionWidth) and yDR <= m_y <= (yDR + selectionHeight):
        in_place = True
        # print("DR: Alcanzando el Objetivo")
        show_game_menu("ao")

    elif xS <= m_x <= (xS + settingsWidth) and yS <= m_y <= (yS + settingsHeight):
        in_place = True
        run_s()

    else:
        print("Not an option")

    return in_place


# Muestra el menu de cada juego
def show_game_menu(game):
    print(game + ": Menu")

    # Superficie del menu
    game_menu_surface = pygame.Surface((displayWidth, displayHeight))

    # Second Surface
    game_menu_second_surface = pygame.Surface(((displayWidth - displaySeparation*2), (displayHeight - displaySeparation*2)))

    # Flag para mantener el menu del juego corriendo
    running_game_menu = True

    while running_game_menu:

        # Background Color
        game_menu_surface.fill((0, 0, 0))
        game_menu_second_surface.fill((255, 255, 255))

        # Muestra la superficie encima de initialWindow
        initialWindow.blit(game_menu_surface, (0, 0))
        initialWindow.blit(game_menu_second_surface, (displaySeparation, displaySeparation))

        # Muestra las opciones del menu
        show_game_menu_options(game)

        # Muestra la mano derecha para seleccionar una opcion
        show_hand_selection()
        # Obtiene las nuevas coordinadas del Kinect
        get_coordinates()

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
    pygame.draw.rect(initialWindow, (0, 0, 0),
                     (xTitulo, yTitulo, game_title_width, game_title_height))

    # Dibuja un rectangulo -> Start (Izquierda)
    # pygame.draw.rect(initialWindow, (67, 255, 52),
    #                 (xOption_left, yOption_left, game_option_width, game_option_height))

    # Directorio de la imagen por mostrar actual
    start_button_directory = "Resources/Menu/" + game + "_Start_Button.png"
    # Imagen cargada
    start_button = pygame.image.load(start_button_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    start_button = pygame.transform.scale(start_button, (game_option_width, game_option_height))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(start_button, (xOption_left, yOption_left))

    # Dibuja un rectangulo -> Main Menu (Derecha)
    # pygame.draw.rect(initialWindow, (165, 77, 255),
    #                 (xOption_right, yOption_right, game_option_width, game_option_height))

    # Directorio de la imagen por mostrar actual
    back_button_directory = "Resources/Menu/" + game + "_Back_Button.png"
    # Imagen cargada
    back_button = pygame.image.load(back_button_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    back_button = pygame.transform.scale(back_button,
                                          (game_option_width, game_option_height))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(back_button, (xOption_right, yOption_right))


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


# Muestra el fondo para cada juego
def show_backroom():
    # Directorio de la imagen por mostrar actual
    background_directory = "Resources/Background/white_room.png"
    # Imagen cargada
    background = pygame.image.load(background_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    background = pygame.transform.scale(background, (displayWidth, displayHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(background, (0, 0))

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

    # Para el sprite del globo
    n = 1

    # Flag del juego
    running = True

    while running:

        # change its background color
        # ul_surface.fill((55, 155, 255))

        # blit ul_surface onto the main screen at the position (0, 0)
        # initialWindow.blit(ul_surface, (0, 0))

        # Muestra el background
        show_backroom()

        # Muestra el globo
        place_balloon(rg_lat, rg_alt, n)

        # Para cambiar el sprite del globo
        if n < 2:
            n += 1
        else:
            n = 1

        # Obtiene las nuevas coordinadas del Kinect
        get_coordinates()
        # Muestra el personaje en pantalla
        show_character()

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
        clock.tick(fps)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()

        # Verificar la colision
        check_balloon_hit()


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


# Verifica si el personaje ha impactado al globo
def check_balloon_hit():

    if rhy < rg_alt + balloon_height and rhy > rg_alt or rhy + hdh < rg_alt + balloon_height and rhy + hdh > rg_alt:

        if rhx > rg_lat and rhx < rg_lat + balloon_width or rhx + hdw > rg_lat and rhx + hdw < rg_lat + balloon_width:
            print("Rigth Hand Collision")
            # time.sleep(8)

    elif lhy < rg_alt + balloon_height and lhy > rg_alt or lhy + hdh < rg_alt + balloon_height and lhy + hdh > rg_alt:

        if lhx > rg_lat and lhx < rg_lat + balloon_width or lhx + hdw > rg_lat and lhx + hdw < rg_lat + balloon_width:
            print("Left Hand Collision")
            # time.sleep(8)


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
up_colores = ["rosado", "rojo", "anaranjado", "amarillo", "verde_claro", "verde_oscuro", "turqueza", "celeste", "azul",
              "morado"]
up_puntaje = ["", "", "", "", "", "", "", "", "", ""]
up_tiempo = 60
up_cantidad = 10
# def Random
# def Inc
# def Dec


# Largo del sosten de las banderas (cambiar multiplier para cambiar el largo solamente)
stick_width = displayWidth * 0.8
# Lugar en la pared donde estara el sosten
stick_x = (displayWidth - stick_width) // 2
# Altura del sosten de las banderas
stick_y = displayHeight // 2 + 130


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
        # ur_surface.fill((255, 122, 172))

        # blit uLSurface onto the main screen at the position (0, 0)
        # initialWindow.blit(ur_surface, (0, 0))

        # Muestra el background
        show_backroom()

        # Muestra el sosten de las banderas
        place_rope()

        # Muestra y pone las banderas en pantalla
        place_flags(up_cantidad, n)

        # n para seleccionar el tipo de sprite
        if n < 5:
            n += 1
        else:
            n = 0

        # Obtiene las nuevas coordinadas del Kinect
        get_coordinates()
        # Muestra el personaje en pantalla
        show_character()

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


# Muestra lo que sostendra las banderas
def place_rope():
    # Directorio de la imagen por mostrar actual
    rope_directory = "Resources/Flags/rope_small.png"

    # Imagen cargada
    rope = pygame.image.load(rope_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    rope = pygame.transform.scale(rope, (int(stick_width), 20))  # Escala la imagen al size deseado

    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(rope, (stick_x, stick_y))


# Posiciona las banderas en pantalla segun la cantidad que hayan y el tamaño
# de donde estaran posicionadas
# @param display: donde se mostraran las banderas
# @param flag_cant: cantidad de banderas
# @param n: sprite de la bandera
def place_flags(flag_cant, n):
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
        initialWindow.blit(flag_n, (flag_x, stick_y))

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
ta_mi_fila = 4
ta_mi_col = 4

# Cambios de posicion
dn = 97 * 2
dx = 0
dy = 0


# Corre la seleccion de Down Left
def run_dl():
    print("Telaraña")

    # Definicion de las variables globales que se necesitan modificar
    global dx
    global dy
    global web_x
    global web_y

    # Crea una superficie
    dl_surface = pygame.Surface((displayWidth, displayHeight))

    # Verifica las posiciones iniciales de la red
    set_starting_point(ta_mi_fila, ta_mi_col)

    running = True

    while running:

        # change its background color
        dl_surface.fill((255, 255, 255))

        # blit uLSurface onto the main screen at the position (0, 0)
        initialWindow.blit(dl_surface, (0, 0))

        # Mostrara la telaraña en pantalla
        place_web(ta_mi_fila, ta_mi_col)

        # Ingresa una palabra
        asign_word(1, 1, "Word3", 5000)
        asign_word(0, 3, "Word1", 5000)
        asign_word(1, 2, "Word4", 5000)
        asign_word(2, 3, "Word2", 5000)
        asign_word(3, 3, "Word5", 5000)
        asign_word(1, 0, "Word6", 5000)
        asign_word(4, 9, "Word7", 5000)
        asign_word(5, 9, "Word8", 5000)

        # Muestra los pies del niño
        place_feet()


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

            # Si se presiona una tecla
            if event.type == pygame.KEYDOWN:
                # Cambia la direccion del movimiento
                if event.key == pygame.K_LEFT:  # T. Izquierda
                    move_left()
                    # dx = 25
                if event.key == pygame.K_RIGHT:  # T. Derecha
                    move_right()
                    # dx = -25
                if event.key == pygame.K_UP:  # T. Izquierda
                    move_front(dl_surface)
                    # dy = 25
                if event.key == pygame.K_DOWN:  # T. Derecha
                    move_back(dl_surface)
                    # dy = -25
                #time.sleep(1)
                break

            # Si se suelta una tecla
            if event.type == pygame.KEYUP:
                # Retorna el movimiento a 0, lo hace estatico de nuevo
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # T. Izquierda o T. Derecha
                    restore_change()
                    # dx = 0
                    # dy = 0

        # Actualiza la posicion de la web
        web_x += dx
        web_y += dy

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


multiplier = 1
web_width = 50
web_separation = displayWidth
web_row_width = displayWidth
web_column_width = displayWidth
web_x = 0
web_y = 0


# Muestra la telaraña en pantalla
def place_web(rows, columns):

    for x in range(0, rows):
        # Dibuja rect(posX, posY, width, ancho)
        pygame.draw.rect(initialWindow, (0, 0, 0),
                         (web_x * multiplier, (web_y + web_separation * (x + 0)) * multiplier,
                          (web_separation + web_separation * (columns - 2) + web_width) * multiplier, web_width * multiplier))

    for y in range(0, columns):
        # Dibuja rect(posX, posY, ancho, height)
        pygame.draw.rect(initialWindow, (0, 0, 0),
                         ((web_x + web_separation * (y + 0)) * multiplier, web_y * multiplier,
                          web_width * multiplier, (web_separation + web_separation * (rows - 2)) * multiplier))


# Define el punto de inicio de la web
def set_starting_point(rows, columns):

    global web_x
    global web_y

    web_x = 0
    web_y = 0

    x = - ((web_separation + web_separation * (columns - 2)) // 2 - web_separation // 2 + web_width // 2) * multiplier
    y = - (web_separation + web_separation * (rows - 2) - web_separation // 4 - web_width) * multiplier

    web_x += x
    web_y += y


# Shoe Dimensions
shoe_width = 774 // 8
shoe_height = 1920 // 8
shoe_l_x = (displayWidth // 2) - (shoe_width) - 50
shoe_l_y = displayHeight - (displayWidth * 3 // 7)
shoe_r_x = (displayWidth // 2) + 50  # + (shoe_width)
shoe_r_y = shoe_l_y


# Muestra los zapatos
def place_feet():
    # Directorio de la imagen por mostrar actual
    shoe_l_directory = "Resources/Character/topShoeLsmall.png"
    # Imagen cargada
    shoe_l = pygame.image.load(shoe_l_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    shoe_l = pygame.transform.scale(shoe_l, (int(shoe_width * multiplier), int(shoe_height * multiplier)))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(shoe_l, (shoe_l_x, shoe_l_y))

    # Directorio de la imagen por mostrar actual
    shoe_r_directory = "Resources/Character/topShoeRsmall.png"
    # Imagen cargada
    shoe_r = pygame.image.load(shoe_r_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    shoe_r = pygame.transform.scale(shoe_r, (int(shoe_width * multiplier), int(shoe_height * multiplier)))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(shoe_r, (shoe_r_x, shoe_r_y))


# Dimensiones de las palabras por mostrar en la web
word_width = 250
word_height = 150


# Muestra el cuadro de la palabra en la web
def asign_word(row, column, word, score):

    # print("row: " + str(row) + "\ncolumn: " + str(column) + "\nword: " + word + "\nscore: " + str(score))

    word_x = (web_x + web_separation * row - word_width // 2 + web_width // 2) * multiplier
    word_y = (web_y + web_separation * column - word_height // 2 + web_width // 2) * multiplier

    word_separation = 10

    # Dibuja rect(posX, posY, ancho, height)
    pygame.draw.rect(initialWindow, (0, 0, 0),
                     ((word_x - word_separation), (word_y - word_separation),
                      (word_width + word_separation*2) * multiplier, (word_height + word_separation*2) * multiplier))

    # Dibuja rect(posX, posY, ancho, height)
    pygame.draw.rect(initialWindow, (255, 127, 127),
                     (word_x, word_y, word_width * multiplier, word_height * multiplier))

    # Para mostrar la palabra
    text = pygame.font.Font("freesansbold.ttf", int(50 * multiplier))  # Font
    text_surface, text_rectangle = text_objects(word, text)
    text_rectangle.center = ((word_x + word_width//2), (word_y + word_height//2))
    initialWindow.blit(text_surface, text_rectangle)


# Crea un objeto de texto
def text_objects(text, font):
    text_surface = font.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()

'''
# Shoe Dimensions
shoe_width = 774 // 8
shoe_height = 1920 // 8
shoe_l_x = (displayWidth // 2) - (shoe_width) - 50
shoe_l_y = displayHeight - (displayWidth * 3 // 7)
shoe_r_x = (displayWidth // 2) + 50  # + (shoe_width)
shoe_r_y = shoe_l_y
'''


# Mueve el personaje hacia delante
def move_front(surface):
    global dy
    dy = dn

    global shoe_r_y
    global shoe_l_y

    shoe_r_y -= dy

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)
    # Ingresa una palabra
    asign_word(1, 1, "Word3", 5000)
    asign_word(0, 3, "Word1", 5000)
    asign_word(1, 2, "Word4", 5000)
    asign_word(2, 3, "Word2", 5000)
    asign_word(3, 3, "Word5", 5000)
    asign_word(1, 0, "Word6", 5000)
    asign_word(4, 9, "Word7", 5000)
    asign_word(5, 9, "Word8", 5000)
    # Muestra los pies del niño
    place_feet()
    # Update display (Actualiza _todo el surface)
    pygame.display.update()
    # Da tiempo para que se grafiquen
    time.sleep(0.3)

    # Segundo Movimiento

    shoe_l_y -= dy

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)
    # Ingresa una palabra
    asign_word(1, 1, "Word3", 5000)
    asign_word(0, 3, "Word1", 5000)
    asign_word(1, 2, "Word4", 5000)
    asign_word(2, 3, "Word2", 5000)
    asign_word(3, 3, "Word5", 5000)
    asign_word(1, 0, "Word6", 5000)
    asign_word(4, 9, "Word7", 5000)
    asign_word(5, 9, "Word8", 5000)
    # Muestra los pies del niño
    place_feet()
    # Update display (Actualiza _todo el surface)
    pygame.display.update()
    # Da tiempo para que se grafiquen
    time.sleep(0.3)

    shoe_r_y += dy
    shoe_l_y += dy

    time.sleep(0.3)



# Mueve el personaje hacia atras
def move_back(surface):

    global dy
    dy = -dn

    global shoe_r_y
    global shoe_l_y

    shoe_r_y -= dy

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)
    # Ingresa una palabra
    asign_word(1, 1, "Word3", 5000)
    asign_word(0, 3, "Word1", 5000)
    asign_word(1, 2, "Word4", 5000)
    asign_word(2, 3, "Word2", 5000)
    asign_word(3, 3, "Word5", 5000)
    asign_word(1, 0, "Word6", 5000)
    asign_word(4, 9, "Word7", 5000)
    asign_word(5, 9, "Word8", 5000)
    # Muestra los pies del niño
    place_feet()
    # Update display (Actualiza _todo el surface)
    pygame.display.update()
    # Da tiempo para que se grafiquen
    time.sleep(0.3)

    # Segundo Movimiento

    shoe_l_y -= dy

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initialWindow.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)
    # Ingresa una palabra
    asign_word(1, 1, "Word3", 5000)
    asign_word(0, 3, "Word1", 5000)
    asign_word(1, 2, "Word4", 5000)
    asign_word(2, 3, "Word2", 5000)
    asign_word(3, 3, "Word5", 5000)
    asign_word(1, 0, "Word6", 5000)
    asign_word(4, 9, "Word7", 5000)
    asign_word(5, 9, "Word8", 5000)
    # Muestra los pies del niño
    place_feet()
    # Update display (Actualiza _todo el surface)
    pygame.display.update()
    # Da tiempo para que se grafiquen
    time.sleep(0.3)

    shoe_r_y += dy
    shoe_l_y += dy

    time.sleep(0.3)




# Mueve el personaje hacia la derecha
def move_right():
    global dx
    dx = -dn


# Mueve el personaje hacia la izquierda
def move_left():
    global dx
    dx = dn


# Reestablece el cambio de los zapatos a cero cuando no esta presionado la tecla
def restore_change():
    global dx
    global dy
    dx = 0
    dy = 0


###############################################################################
#                                                                             #
#                           Alcanzando el Objetivo                            #
#                                                                             #
###############################################################################

# Variables de Alcanzando el Objetivo
ao_object_x = 400
ao_object_y = 200

ao_cant_colisiones = 0


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
        # dr_surface.fill((85, 255, 0))

        # blit uLSurface onto the main screen at the position (0, 0)
        # initialWindow.blit(dr_surface, (0, 0))

        # Muestra el background
        show_backroom()

        # Muestra el globo
        place_object(ao_object_x, ao_object_y, n)

        # Obtiene las nuevas coordinadas del Kinect
        get_coordinates()
        # Muestra el personaje en pantalla
        show_character()


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

        # Verifica las colisiones
        check_object_hit()


ao_object_width = balloon_width
ao_object_height = balloon_height


# Posiciona el objeto y muestra el sprite que se necesite
# @param x
# @param y
# @param n: sprite del objeto
def place_object(x, y, n):
    # Directorio de la imagen por mostrar actual
    ao_object_directory = "Resources/Balloon/balloon" + str(n) + ".png"

    # Imagen cargada
    ao_object = pygame.image.load(ao_object_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    ao_object = pygame.transform.scale(ao_object, (ao_object_width, ao_object_height))  # Escala la imagen al size deseado

    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initialWindow.blit(ao_object, (x, y))


# Verifica si el personaje ha impactado al globo
def check_object_hit():

    global ao_cant_colisiones

    if rhy < ao_object_y + ao_object_height and rhy > ao_object_y \
            or rhy + hdh < ao_object_y + ao_object_height and rhy + hdh > ao_object_y:

        if rhx > ao_object_x and rhx < ao_object_x + ao_object_width \
                or rhx + hdw > ao_object_x and rhx + hdw < ao_object_x + ao_object_width:
            print("Rigth Hand Collision")

            ao_cant_colisiones += 1

            #time.sleep(8)

    elif lhy < ao_object_y + ao_object_height and lhy > ao_object_y \
            or lhy + hdh < ao_object_y + ao_object_height and lhy + hdh > ao_object_y:

        if lhx > ao_object_x and lhx < ao_object_x + ao_object_width \
                or lhx + hdw > ao_object_x and lhx + hdw < ao_object_x + ao_object_width:
            print("Left Hand Collision")

            ao_cant_colisiones += 1

            #time.sleep(8)


# Corre la seleccion de Settings
def run_s():
    print("Settings")

    # create a new Surface
    s_surface = pygame.Surface((displayWidth, displayHeight))

    # change its background color
    s_surface.fill((0, 0, 255))

    running = True

    while running:

        # blit uLSurface onto the main screen at the position (0, 0)
        initialWindow.blit(s_surface, (0, 0))

        # Muestra el personaje en pantalla
        show_character()
        # Obtiene las nuevas coordinadas del Kinect
        # get_coordinates()
        # Obtiene las coordenadas del Kinect
        get_coordinates_from_kinect()

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
        clock.tick(10)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Head Dimensions
hm = 3
hw = 452 // hm
hh = 359 // hm

# Body Dimensions
bm = 3
bw = 319 // bm
bh = 369 // bm

# Hands Dimensions
hdm = 40
hdw = 900 // hdm
hdh = 900 // hdm

# Feet Dimensions
fm = 13
fw = 400 // fm
fh = 460 // fm

bx = displayWidth // 2 - 40
by = (displayHeight - displayHeight * 0.8) + hh + 10
hx = bx - 20
hy = by - hh - 10
lhx = bx - 30
lhy = by + 50
rhx = lhx + bw + 30
rhy = lhy
lfx = bx + 10
lfy = by + 150
rfx = lfx + 50
rfy = lfy
character_coordinates = [bx, by, lhx, lhy, rhx, rhy, lfx, lfy, rfx, rfy]


# Muestra el personaje en pantalla
def show_character():

    body_parts = ["head", "body", "handL", "handR", "shoeL", "shoeR"]

    # Directorio de la cabeza
    head_directory = "Resources/Character/headsmall.png"
    head = pygame.image.load(head_directory)
    #head = pygame.transform.scale(head, (hw, hh))
    initialWindow.blit(head, (hx, hy))

    # Directorio del cuerpo
    body_directory = "Resources/Character/bodysmall.png"
    body = pygame.image.load(body_directory)
    #body = pygame.transform.scale(body, (bw, bh))
    initialWindow.blit(body, (bx, by))

    # Directorio de la mano izquierda
    hand_l_directory = "Resources/Character/handLsmall.png"
    hand_l = pygame.image.load(hand_l_directory)
    #hand_l = pygame.transform.scale(hand_l, (hdw, hdh))
    initialWindow.blit(hand_l, (lhx, lhy))

    # Directorio de la mano derecha
    hand_r_directory = "Resources/Character/handRsmall.png"
    hand_r = pygame.image.load(hand_r_directory)
    #hand_r = pygame.transform.scale(hand_r, (hdw, hdh))
    initialWindow.blit(hand_r, (rhx, rhy))

    # Directorio del pie izquierdo
    shoe_l_directory = "Resources/Character/shoeLsmall.png"
    shoe_l = pygame.image.load(shoe_l_directory)
    #shoe_l = pygame.transform.scale(shoe_l, (fw, fh))
    initialWindow.blit(shoe_l, (lfx, lfy))

    # Directorio del pie derecho
    shoe_r_directory = "Resources/Character/shoeRsmall.png"
    shoe_r = pygame.image.load(shoe_r_directory)
    #shoe_r = pygame.transform.scale(shoe_r, (fw, fh))
    initialWindow.blit(shoe_r, (rfx, rfy))


# Muestra solo la mano derecha, que sera utilizada para seleccionar
def show_hand_selection():
    # Directorio de la mano derecha
    hand_r_directory = "Resources/Character/handRsmall.png"
    hand_r = pygame.image.load(hand_r_directory)
    hand_r = pygame.transform.scale(hand_r, (hdw, hdh))
    initialWindow.blit(hand_r, (rhx, rhy))


# Actualiza las posiciones del Personaje
def update_character_coordinates(dbx, dby, dlhx, dlhy, drhx, drhy, dlfx, dlfy, drfx, drfy):

    global bx
    global by
    global hx
    global hy
    global lhx
    global lhy
    global rhx
    global rhy
    global lfx
    global lfy
    global rfx
    global rfy

    bx = dbx
    by = dby
    hx = dbx - 20
    hy = dby - hh - 10
    lhx = dlhx
    lhy = dlhy
    rhx = drhx
    rhy = drhy
    lfx = dlfx
    lfy = dlfy
    rfx = drfx
    rfy = drfy


# Simulacion de la obtencion de las coordenadas desde el Kinect
def get_coordinates():

    mx = 100
    my = 100

    dbx = random.randrange(0, displayWidth - mx, 1)
    dby = random.randrange(0, displayHeight - my, 1)
    dlhx = random.randrange(0, displayWidth - mx, 1)
    dlhy = random.randrange(0, displayHeight - my, 1)
    drhx = random.randrange(0, displayWidth - mx, 1)
    drhy = random.randrange(0, displayHeight - my, 1)
    dlfx = random.randrange(0, displayWidth - mx, 1)
    dlfy = random.randrange(0, displayHeight - my, 1)
    drfx = random.randrange(0, displayWidth - mx, 1)
    drfy = random.randrange(0, displayHeight - my, 1)

    update_character_coordinates(dbx, dby, dlhx, dlhy, drhx, drhy, dlfx, dlfy, drfx, drfy)


# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.100.80', 5204))


# Abre una conexion con Processing para obtener las coordenadas del Kinect
def get_coordinates_from_kinect():

    client.send(b"I am CLIENT\n")

    #while True:
    data = client.recv(1024).decode('UTF-8')

    if not data:
        print("No Data")
    else:
        print('Received:' + repr(data))  # Paging Python!
        n = 0
        coord = ""
        coords = []
        #data = data[1:]
        while data != "":
            if data[0] != ",":
                coord += data[0]
            else:
                print("->", coord)
                n += 1
                coords.append(int(coord))
                coord = ""
            data = data[1:]
        print("->", coord)
        coords.append(int(coord))

        update_character_coordinates(coords[0], coords[1], coords[2], coords[3], coords[4],
                                     coords[5], coords[6], coords[7], coords[8], coords[9])


# def set_new_coordinate(coord,n)


# Flag
playing = True

# Main Loop
while playing:

    # Cambia el fondo de la superficie
    initialWindow.fill(black)

    # Muestra las posibles cuadros de las opciones de los juegos
    show_main_options()

    # Muestra la mano derecha para seleccionar una opcion
    show_hand_selection()
    # Obtiene las nuevas coordinadas del Kinect
    # get_coordinates()
    # Obtiene las coordenadas del Kinect
    get_coordinates_from_kinect()

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

# Cierra el cliente
client.close()

# Deja de correr Pygame
pygame.quit()
