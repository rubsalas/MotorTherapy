import pygame
import random
import time
import socket

# Inicializa Pygame y todos sus modulos
pygame.init()

# Medidas de la ventana
displayWidth = 1000
displayHeight = 650
displaySeparation = 16

# Medidas de cuadro de seleccion de menu principal
selectionWidth = (displayWidth - 75 - displaySeparation * 3) // 2  # 439 px
selectionHeight = (displayHeight - displaySeparation * 3) // 2  # 301 px

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
initial_window = pygame.display.set_mode((displayWidth, displayHeight))

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
    # Raqueta Globo
    # Directorio de la imagen por mostrar actual
    rg_directory = "Resources/Menu/Raqueta_Globo_small.png"
    # Imagen cargada
    rg_title = pygame.image.load(rg_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    rg_title = pygame.transform.scale(rg_title, (selectionWidth, selectionHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(rg_title, (xUL, yUL))

    # Usando Los Pies
    # Directorio de la imagen por mostrar actual
    up_directory = "Resources/Menu/Usando_Los_Pies_small.png"
    # Imagen cargada
    up_title = pygame.image.load(up_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    up_title = pygame.transform.scale(up_title, (selectionWidth, selectionHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(up_title, (xUR, yUR))

    # Telarana
    # Directorio de la imagen por mostrar actual
    ta_directory = "Resources/Menu/Telarana_small.png"
    # Imagen cargada
    ta_title = pygame.image.load(ta_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    ta_title = pygame.transform.scale(ta_title, (selectionWidth, selectionHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(ta_title, (xDL, yDL))

    # Alcanzando el Objetivo
    # Directorio de la imagen por mostrar actual
    ao_directory = "Resources/Menu/Alcanzando_El_Objetivo_small.png"
    # Imagen cargada
    ao_title = pygame.image.load(ao_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    ao_title = pygame.transform.scale(ao_title, (selectionWidth, selectionHeight))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(ao_title, (xDR, yDR))

    # Dibuja un rectangulo -> Settings [S]
    pygame.draw.rect(initial_window, (255, 255, 255),
                     (xS, yS, settingsWidth, settingsHeight))


# Variables de seleccion
waiting_time = 20
on_selection_timer = 0
# Menu Principal
on_ul = False
on_ur = False
on_dl = False
on_dr = False
on_s = False
# Menu de Juego
on_start = False
on_back = False
# Final del Juego
on_ending_back = False


# Verificara la seleccion de la mano en la pantalla principal
def check_hand_main_options_selection():
    in_place = False

    global on_ul
    global on_ur
    global on_dl
    global on_dr
    global on_s
    global on_selection_timer

    if xUL <= rhx <= (xUL + selectionWidth) and xUL <= rhx + hdw <= (xUL + selectionWidth) \
            and yUL <= rhy <= (yUL + selectionHeight) and yUL <= rhy + hdh <= (yUL + selectionHeight):

        if not on_ul:  # Si estaba en otra seleccion que no haya sido UL
            on_ul = True
            on_ur = False
            on_dl = False
            on_dr = False
            on_s = False
            on_selection_timer = 0
        else:  # Si ya estaba en UL
            if on_selection_timer < waiting_time:  # Si no se ha completado el tiempo de espera
                on_selection_timer += 1
                print("UL Time: " + str(on_selection_timer))
            else:  # Cuando se cumple el tiempo de espera
                # Reset al timer
                on_selection_timer = 0
                # Se muestra el menu del juego
                print("UL: Raqueta Globo")
                in_place = True
                show_game_menu("rg")

    elif xUR <= rhx <= (xUR + selectionWidth) and xUR <= rhx + hdw <= (xUR + selectionWidth) \
            and yUR <= rhy <= (yUR + selectionHeight) and yUR <= rhy + hdh <= (yUR + selectionHeight):

        if not on_ur:  # Si estaba en otra seleccion que no haya sido UR
            on_ul = False
            on_ur = True
            on_dl = False
            on_dr = False
            on_s = False
            on_selection_timer = 0
        else:  # Si ya estaba en UR
            if on_selection_timer < waiting_time:  # Si no se ha completado el tiempo de espera
                on_selection_timer += 1
                print("UR Time: " + str(on_selection_timer))
            else:  # Cuando se cumple el tiempo de espera
                # Reset al timer
                on_selection_timer = 0
                # Se muestra el menu del juego
                print("UR: Usando los Pies")
                in_place = True
                show_game_menu("up")

    elif xDL <= rhx <= (xDL + selectionWidth) and xDL <= rhx + hdw <= (xDL + selectionWidth) \
            and yDL <= rhy <= (yDL + selectionHeight) and yDL <= rhy + hdh <= (yDL + selectionHeight):

        if not on_dl:  # Si estaba en otra seleccion que no haya sido DL
            on_ul = False
            on_ur = False
            on_dl = True
            on_dr = False
            on_s = False
            on_selection_timer = 0
        else:  # Si ya estaba en DL
            if on_selection_timer < waiting_time:  # Si no se ha completado el tiempo de espera
                on_selection_timer += 1
                print("DL Time: " + str(on_selection_timer))
            else:  # Cuando se cumple el tiempo de espera
                # Reset al timer
                on_selection_timer = 0
                # Se muestra el menu del juego
                print("DL: Telaraña")
                in_place = True
                show_game_menu("ta")

    elif xDR <= rhx <= (xDR + selectionWidth) and xDR <= rhx + hdw <= (xDR + selectionWidth) \
            and yDR <= rhy <= (yDR + selectionHeight) and yDR <= rhy + hdh <= (yDR + selectionHeight):

        if not on_dr:  # Si estaba en otra seleccion que no haya sido DR
            on_ul = False
            on_ur = False
            on_dl = False
            on_dr = True
            on_s = False
            on_selection_timer = 0
        else:  # Si ya estaba en DR
            if on_selection_timer < waiting_time:  # Si no se ha completado el tiempo de espera
                on_selection_timer += 1
                print("DR Time: " + str(on_selection_timer))
            else:  # Cuando se cumple el tiempo de espera
                # Reset al timer
                on_selection_timer = 0
                # Se muestra el menu del juego
                print("DR: Alcanzando el Objetivo")
                in_place = True
                show_game_menu("ao")

    elif xS <= rhx <= (xS + settingsWidth) and xS <= rhx + hdw <= (xS + settingsWidth) \
            and yS <= rhy <= (yS + settingsHeight) and yS <= rhy + hdh <= (yS + settingsHeight):

        if not on_s:  # Si estaba en otra seleccion que no haya sido S
            on_ul = False
            on_ur = False
            on_dl = False
            on_dr = False
            on_s = True
            on_selection_timer = 0
        else:  # Si ya estaba en S
            if on_selection_timer < waiting_time:  # Si no se ha completado el tiempo de espera
                on_selection_timer += 1
                print("S Time: " + str(on_selection_timer))
            else:  # Cuando se cumple el tiempo de espera
                # Reset al timer
                on_selection_timer = 0
                # Se muestra el menu del juego
                print("S: Settings")
                in_place = True
                run_s()

    else:
        on_ul = False
        on_ur = False
        on_dl = False
        on_dr = False
        on_s = False
        on_selection_timer = 0
        # print("Not an option")

    return in_place


# Verifica en que seccion se encuentra posicionado para seleccionarlo
# @param m_x : Posicion en x
# @param m_y : Posicion en y
def mouse_click_main_selection(m_x, m_y):
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
    game_menu_second_surface = pygame.Surface(
        ((displayWidth - displaySeparation * 2), (displayHeight - displaySeparation * 2)))

    # Flag para mantener el menu del juego corriendo
    running_game_menu = True
    running_game_menu_test = True

    while running_game_menu and running_game_menu_test:

        # Background Color
        game_menu_surface.fill((0, 0, 0))
        game_menu_second_surface.fill((255, 255, 255))

        # Muestra la superficie encima de initialWindow
        initial_window.blit(game_menu_surface, (0, 0))
        initial_window.blit(game_menu_second_surface, (displaySeparation, displaySeparation))

        # Muestra las opciones del menu
        show_game_menu_options(game)

        # Obtiene las coordenadas del Kinect
        get_coordinates_from_kinect()
        # Muestra la mano derecha para seleccionar una opcion
        show_hand_selection()

        # Pygame verifica todos los events
        for game_menu_event in pygame.event.get():

            # Si se cierra la ventana
            if game_menu_event.type == pygame.QUIT:
                # Va a salir del while
                running_game_menu = False
                print("QUIT")

            # Al presionar el mouse
            if game_menu_event.type == pygame.MOUSEBUTTONDOWN:
                # Obtiene las posiciones actuales del mouse
                game_menu_mousex, game_menu_mousey = pygame.mouse.get_pos()
                # Verifica si puede ingresar a una opcion
                running_game_menu_test = game_menu_selection(game_menu_mousex, game_menu_mousey, game)

        running_game_menu = check_hand_game_menu_options_selection(game)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Muestra los cuadros de seleccion del menu del juego seleccionado
def show_game_menu_options(game):
    # Dibuja un rectangulo -> Titulo
    pygame.draw.rect(initial_window, (0, 0, 0),
                     (xTitulo, yTitulo, game_title_width, game_title_height))

    # START BUTTON
    # Directorio de la imagen por mostrar actual
    start_button_directory = "Resources/Menu/" + game + "_Start_Button.png"
    # Imagen cargada
    start_button = pygame.image.load(start_button_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    start_button = pygame.transform.scale(start_button,
                                          (game_option_width, game_option_height))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(start_button, (xOption_left, yOption_left))

    # BACK BUTTON
    # Directorio de la imagen por mostrar actual
    back_button_directory = "Resources/Menu/" + game + "_Back_Button.png"
    # Imagen cargada
    back_button = pygame.image.load(back_button_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    back_button = pygame.transform.scale(back_button,
                                         (game_option_width, game_option_height))  # Escala la imagen al size deseado
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(back_button, (xOption_right, yOption_right))


# Verificara la seleccion de la mano en la pantalla del menu del juego
def check_hand_game_menu_options_selection(game):
    selection = True

    global on_start
    global on_back
    global on_selection_timer

    if xOption_left <= rhx <= (xOption_left + game_option_width) \
            and xOption_left <= rhx + hdw <= (xOption_left + game_option_width) \
            and yOption_left <= rhy <= (yOption_left + game_option_height) \
            and yOption_left <= rhy + hdw <= (yOption_left + game_option_height):
        # Opcion Start (Izquierda)

        if not on_start:  # Si estaba en otra seleccion que no haya sido Start
            on_start = True
            on_back = False
            on_selection_timer = 0
        else:  # Si ya estaba en Start
            if on_selection_timer < waiting_time:  # Si no se ha completado el tiempo de espera
                on_selection_timer += 1
                # print("Start Time: " + str(on_selection_timer))
            else:  # Cuando se cumple el tiempo de espera
                # Reset al timer
                on_selection_timer = 0

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
                    print("Error in check_hand_game_menu_options_selection(game)")

                # Mantiene True el Flag para que al salirse de la ventana del juego vuelva al menu del juego
                selection = True

    elif xOption_right <= rhx <= (xOption_right + game_option_width) \
            and xOption_right <= rhx + hdw <= (xOption_right + game_option_width) \
            and yOption_right <= rhy <= (yOption_right + game_option_height) \
            and yOption_right <= rhy + hdh <= (yOption_right + game_option_height):
        # Opcion Back (Derecha)

        if not on_back:  # Si estaba en otra seleccion que no haya sido Back
            on_start = False
            on_back = True
            on_selection_timer = 0
        else:  # Si ya estaba en Back
            if on_selection_timer < waiting_time:  # Si no se ha completado el tiempo de espera
                on_selection_timer += 1
                # print("Back Time: " + str(on_selection_timer))
            else:  # Cuando se cumple el tiempo de espera
                # Reset al timer
                on_selection_timer = 0
                # Hace selection False para retornar al menu principal
                selection = False

    else:
        # print("Game: Not an option")
        on_start = False
        on_back = False
        on_selection_timer = 0

    return selection


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
    initial_window.blit(background, (0, 0))


# Crea un objeto de texto
def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


###############################################################################
#                                                                             #
#                               RAQUETA GLOBO                                 #
#                                                                             #
###############################################################################


# Variables de Raqueta Globo
rg_alt_inicial = 100 * 2
rg_lat_inicial = 100 * 0.5

rg_alt = rg_alt_inicial
rg_lat = rg_lat_inicial
rg_cantidad = 15

# Puntaje por Golpear el Globo
rg_balloon_points = 1000
# Puntaje Actual de Raqueta Globo
rg_score = 0
# Cantidad Actual de hits recibidos al globo
rg_hit_count = 0


# Corre la seleccion de Raqueta Globo
# Corre la seleccion de Up Left
def run_ul():

    print("Raqueta Globo")

    # Para el sprite del globo
    n = 1

    # Flag del juego
    running = True

    while running:

        # Muestra el background
        show_backroom()

        # Muestra la informacion del juego
        show_info("rg")

        # Muestra el globo
        place_balloon(rg_lat, rg_alt, (n % 2 + 1))

        # Para cambiar el sprite del globo
        n += 1

        # Obtiene las coordenadas del Kinect
        get_coordinates_from_kinect()
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
        # check_ballon_hit() envia false cuando se terminan los intentos
        # check_ballon_hit() envia true ya que no ha terminado
        if not check_balloon_hit():
            # Interfaz para terminar el juego
            running = end_game("rg")


# Largo de balloon
balloon_width = 62 // 1
# Ancho de balloon
balloon_height = 120 // 1


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
    initial_window.blit(balloon_n, (x, y))


# Verifica si el personaje ha impactado al globo
def check_balloon_hit():
    hasnt_finished = True

    # Verifica si ha sido golpeado con la mano derecha
    if rhy < rg_alt + balloon_height and rhy > rg_alt or rhy + hdh < rg_alt + balloon_height and rhy + hdh > rg_alt:
        if rhx > rg_lat and rhx < rg_lat + balloon_width or rhx + hdw > rg_lat and rhx + hdw < rg_lat + balloon_width:
            print("Right Hand Collision")
            hasnt_finished = has_hit_balloon()

    # Verifica si ha sido golpeado con la mano izquierda
    elif lhy < rg_alt + balloon_height and lhy > rg_alt or lhy + hdh < rg_alt + balloon_height and lhy + hdh > rg_alt:
        if lhx > rg_lat and lhx < rg_lat + balloon_width or lhx + hdw > rg_lat and lhx + hdw < rg_lat + balloon_width:
            print("Left Hand Collision")
            hasnt_finished = has_hit_balloon()

    return hasnt_finished


# Actualiza el juego cuando el jugador ha golpeado el globo
def has_hit_balloon():
    global rg_alt
    global rg_lat
    global rg_hit_count
    global rg_score

    mx = balloon_width
    my = displayWidth // 2

    # Actualiza la cantidad de golpes que se han logrado
    rg_hit_count += 1

    # Actualiza el puntaje del juego
    rg_score += rg_balloon_points

    if (rg_cantidad - rg_hit_count) > 0:
        # Actualiza la posicion del globo
        rg_lat = random.randrange(0, displayWidth - mx, 1)
        rg_alt = random.randrange(0, displayHeight - my, 1)

        return True


# Muestra la información necesaria del juego Raqueta Globo
def show_info(game):
    n = 0
    font_size = 20
    text_list = []
    # y_center = displayHeight//2

    if game == "rg":
        str_score_rg = "Puntaje: " + str(rg_score)
        str_hits_left_rg = "Golpes Restantes: " + str(rg_cantidad - rg_hit_count)
        str_actual_position_rg = "Posición Actual del Globo: (" + str(rg_lat) + "," + str(rg_alt) + ")"

        text_list = [str_score_rg, str_hits_left_rg, str_actual_position_rg]

    elif game == "up":

        str_score_up = "Puntaje: " + str(up_score)
        str_time_left_up = "Tiempo Restante: " + str(int(up_actual_iteration_time_left))
        str_actual_iteration_up = "Secuencia Actual: " + str(up_actual_iteration)
        str_iterations_left_up = "Secuencias Restantes: " + str(up_iterations - up_actual_iteration)
        str_fail_hits_up = "Fallos de Secuencia: " + str(up_failed_sequences)

        text_list = [str_score_up, str_time_left_up, str_actual_iteration_up, str_iterations_left_up, str_fail_hits_up]

        print("Showing UP info")

    elif game == "ta":
        str_score_ta = "Puntaje: " + str(ta_score)
        str_words_left_ta = "Palabras Restantes: " + str(len(ta_words_list) - len(ta_owned_words_list))
        str_found_words_ta = "Palabras Encontradas: " + str(len(ta_owned_words_list))

        text_list = [str_score_ta, str_words_left_ta, str_found_words_ta]

    elif game == "ao":
        str_distances_left_ao = "Distancias Restantes: " + str(ao_cantidad - ao_actual_iteration)
        str_time_left = "Tiempo Restante por Distancia: " + str(
            ao_seconds_left - ((ao_cantidad - ao_actual_iteration) * ao_seconds))
        str_thrown_hits = "Golpes Dados: "  # + str(ao_thrown_hits)

        text_list = [str_distances_left_ao, str_time_left, str_thrown_hits]

    else:
        print("Error en show_info(game)")

    # Muestra en pantalla el texto
    for words in text_list:
        # Cantidad de Golpes Restantes
        text = pygame.font.Font("freesansbold.ttf", font_size)  # Font
        text_surface, text_rectangle = text_objects(words, text, (0, 0, 0))
        text_rectangle.center = (displayWidth // 2, (font_size // 2) + font_size * 2 * n)
        initial_window.blit(text_surface, text_rectangle)
        n += 1


# Termina el juego que se indique
def end_game(game):
    # Variable para volver al menu del juego
    stay_in_game = True

    stay_in_game_test = True

    while stay_in_game and stay_in_game_test:

        # Muestra el background
        show_backroom()

        # Muestra las estadisticas finales
        show_ending_statistics(game)

        # Muestra el boton para volver al menu del juego
        show_ending_button(game)

        # Obtiene las coordenadas del Kinect
        get_coordinates_from_kinect()
        # Muestra la mano derecha para seleccionar una opcion
        show_hand_selection()

        # Pygame verifica todos los events
        for event in pygame.event.get():

            # Al presionar el mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Obtiene las posiciones actuales del mouse
                mousex, mousey = pygame.mouse.get_pos()
                # Verifica si puede ingresar a una opcion
                stay_in_game_test = back_to_game_menu(mousex, mousey, game)

        stay_in_game = check_hand_back_to_game_menu_selection(game)

        # Parametro serian la cantidad de frames en un segundo (fps)
        clock.tick(fps)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()

    return stay_in_game


back_button_width = game_option_width // 3
back_button_height = game_option_height // 3

back_ending_button_x = displayWidth // 2 - back_button_width // 2
back_ending_button_y = 450


# Muestra las estadisticas finales
def show_ending_statistics(game):
    n = 0
    font_size = 30  # Ch
    text_list = []

    if game == "rg":

        str_score_rg = "Puntaje: " + str(rg_score)
        str_hits_left_rg = "Golpes Acertados: " + str(rg_hit_count)  # Ch

        text_list = [str_score_rg, str_hits_left_rg]

    elif game == "up":
        print("show_ending_statistics(up)")

        str_ = "show_ending_statistics(up)"

        text_list = [str_]

    elif game == "ta":
        str_score_ta = "Puntaje: " + str(ta_score)
        str_question = "¿Qué concepto agrupa todas las palabras?"

        text_list = [str_score_ta, str_question]

    elif game == "ao":
        str_score_ao = "Puntaje : " + str(ao_score)
        str_distances_left_ao = "Distancias Restantes: " + str(ao_cantidad - ao_actual_iteration)
        str_time_left_ao = "Tiempo Total Restante: " + str(ao_seconds_left)

        text_list = [str_score_ao, str_distances_left_ao, str_time_left_ao]

    for words in text_list:
        # Cantidad de Golpes Restantes
        text = pygame.font.Font("freesansbold.ttf", font_size)  # Font
        text_surface, text_rectangle = text_objects(words, text, (0, 0, 0))
        text_rectangle.center = (displayWidth // 2, back_ending_button_y - 100 - font_size * 3.5 * n)  # Ch
        initial_window.blit(text_surface, text_rectangle)
        n += 1


# Muestra el boton para volver
def show_ending_button(game):
    # START BUTTON
    # Directorio de la imagen por mostrar actual
    back_button_directory = "Resources/Menu/" + game + "_Back_Button.png"
    # Imagen cargada
    ending_back_button = pygame.image.load(back_button_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    ending_back_button = pygame.transform.scale(ending_back_button,
                                               (back_button_width, back_button_height))
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(ending_back_button, (back_ending_button_x, back_ending_button_y))


# Verifica la seleccion de la mano cuando termina el juego
def check_hand_back_to_game_menu_selection(game):
    # Flag
    stay_in_game = True

    global on_ending_back
    global on_selection_timer

    if back_ending_button_x <= rhx <= (back_ending_button_x + back_button_width) \
            and back_ending_button_x <= rhx + hdw <= (back_ending_button_x + back_button_width) \
            and back_ending_button_y <= rhy <= (back_ending_button_y + back_button_height) \
            and back_ending_button_y <= rhy + hdh <= (back_ending_button_y + back_button_height):

        if not on_ending_back:  # Si estaba en otra seleccion que no haya sido Back
            on_ending_back = True
            on_selection_timer = 0
        else:  # Si ya estaba en Back
            if on_selection_timer < waiting_time:  # Si no se ha completado el tiempo de espera
                on_selection_timer += 1
                print("Ending_Back Time: " + str(on_selection_timer))
            else:  # Cuando se cumple el tiempo de espera
                # Reset al timer
                on_selection_timer = 0
                # Se retorna al menu del juego
                print("Back to Game Menu")
                # Restaura las variables del juego
                restore_game(game)
                # Cambia el Flag para salir al menu del juego
                stay_in_game = False

    return stay_in_game


# Verifica si se ha presionado el boton de Back
def back_to_game_menu(m_x, m_y, game):
    # Flag
    stay_in_game = True

    if back_ending_button_x <= m_x <= (back_ending_button_x + back_button_width) and back_ending_button_y <= m_y <= (
            back_ending_button_y + back_button_height):
        # Restaura las variables del juego
        restore_game(game)
        # Cambia el Flag para salir al menu del juego
        stay_in_game = False

    return stay_in_game


# Restaura las variables del juego una vez terminado
def restore_game(game):
    if game == "rg":
        global rg_alt
        global rg_lat
        global rg_score
        global rg_hit_count

        rg_alt = rg_alt_inicial
        rg_lat = rg_lat_inicial
        rg_score = 0
        rg_hit_count = 0

    elif game == "up":
        print("restore_game(\"up\") -> FALTA")

    elif game == "ta":
        print("restore_game(\"ta\") -> FALTA")

    elif game == "ao":
        global ao_seconds_left
        global ao_actual_iteration

        ao_seconds_left = ao_seconds * ao_cantidad
        ao_actual_iteration = 1

    else:
        print("Error en restore_game(game)")


def inc():
    print("Inc")


def dec():
    print("Dec")


###############################################################################
#                                                                             #
###############################################################################


###############################################################################
#                                                                             #
#                             USANDO LOS PIES                                 #
#                                                                             #
###############################################################################


# Variables de Usando los Pies

# Lista de todos los colores posibles de las banderas
up_colores = ["rosado", "rojo", "anaranjado", "amarillo", "verde_claro", "verde_oscuro", "turqueza", "celeste", "azul",
              "morado"]
# Lista de los puntajes de las banderas existentes con su color respectivo
up_puntaje = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
# Cantidad de tiempo que tendra el jugador para completar la secuencia
up_tiempo = 20
# Cantidad maxima de indices del arreglo de banderas para ingresar en el orden por completar
up_cantidad = 4

# Cantidad de iteraciones que se correra el juego
up_iterations = 5

# Iteracion en la que se encuentra el juego actualmente
up_actual_iteration = 1

# Lista con los index de las banderas ordenadas
flag_index_order = []

# Lista en orden de flag_index_order
flag_index_order_in_order = []

# Lista con el orden de banderas por completar
up_ordered_flags = []

# Lista de todos los colores disponibles con su respectivo indice de sprite
up_flag_color_list = [["rosado", 0], ["rojo", 1], ["anaranjado", 2], ["amarillo", 3], ["verde_claro", 4],
                      ["verde_oscuro", 5], ["turqueza", 6], ["celeste", 7], ["azul", 8], ["morado", 9]]

up_actual_hitten_flags = []

# Hora exacta de terminar la iteracion actual
up_end_time = 0

# Tiempo restante de la iteracion actual
up_actual_iteration_time_left = up_tiempo

# Fallos de Secuencia
up_failed_sequences = 0

# Cambio en tiempo
up_dtime = -3
# Cambio en up_cantidad
up_dcantidad = 1

# Puntaje total
up_score = 0
up_actual_iteration_score = 0


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

# Posiciones de la bandera
flag_x = 0


# Corre la seleccion de Up Right: Usando los Pies
def run_up():
    print("Usando los Pies")

    global up_end_time
    up_end_time = time.time() + up_tiempo

    set_flag_order()

    n = 0

    running = True

    # while running:
    while running:

        # Muestra el background
        show_backroom()

        # Muestra la informacion del juego
        #show_info("up")

        # Muestra el sosten de las banderas
        place_rope()

        # Muestra y pone las banderas en pantalla
        place_flags(n)

        # n para seleccionar el tipo de sprite
        if n < 5:
            n += 1
        else:
            n = 0

        # Muestra el orden de la secuencia actual por seguir
        show_actual_sequence()

        # Obtiene las coordenadas del Kinect
        get_coordinates_from_kinect()
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
        clock.tick(10)

        # Update display (Actualiza _todo el surface)
        pygame.display.update()

        if not check_correct_order():
            # Interfaz para terminar el juego
            running = end_game("up")


# Muestra lo que sostendra las banderas
def place_rope():
    # Directorio de la imagen por mostrar actual
    rope_directory = "Resources/Flags/rope_small.png"

    # Imagen cargada
    rope = pygame.image.load(rope_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    rope = pygame.transform.scale(rope, (int(stick_width), 20))  # Escala la imagen al size deseado

    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(rope, (stick_x, stick_y))


# Posiciona las banderas en pantalla segun la cantidad que hayan y el tamaño
# de donde estaran posicionadas
# @param display: donde se mostraran las banderas
# @param flag_cant: cantidad de banderas
# @param n: sprite de la bandera
def place_flags(n):

    global flag_x

    # Posicion en x de la bandera:
    #   (Mitad del espacio que sobra del display )
    #    + (Mitad del espacio donde estaran las banderas)
    #    - (Mitad del space_per_flag por bandera que exista)
    #    + (Espacio sobrante en space_per_flag con la bandera, solo de un lado)
    flag_x = ((displayWidth - stick_width) // 2) + (stick_width // 2) - ((space_per_flag * up_cantidad) // 2) + (
            (space_per_flag - flag_width) // 2)

    for i in flag_index_order_in_order:

        str_sprite_index = str(get_sprite_index(up_colores[i]))

        # Directorio de la imagen por mostrar actual
        directory = "Resources/Flags/Flag" + str_sprite_index + "/F" + str_sprite_index + str(n) + ".png"

        # Imagen cargada
        flag_n = pygame.image.load(directory)  # Carga la imagen de la carpeta
        # Imagen escalada
        flag_n = pygame.transform.scale(flag_n, (flag_width, flag_height))  # Escala la imagen al size deseado

        # Muestra la imagen en pantalla con las coordenadas preestablecidas
        initial_window.blit(flag_n, (flag_x, stick_y))

        # Aumenta flag_x para la posicion de la siguiente bandera
        flag_x = flag_x + space_per_flag

        # Cantidad de banderas restantes por mostrar
        # flag_cant = flag_cant - 1


# Retorna el indice del color donde estan guardados sus sprites
def get_sprite_index(color):

    for i in up_flag_color_list:
        if color == i[0]:
            return i[1]

    return -1


# Genera el orden de las banderas por ser
# Utiliza array de COLOR para escoger una CANTIDAD maxima de banderas por golpear
def set_flag_order():

    global flag_index_order
    global up_ordered_flags
    global flag_index_order_in_order

    playable = True

    print("up_cantidad", up_cantidad)
    print("len(up_colores)", len(up_colores))

    if up_cantidad <= len(up_colores):

        # De 0 al maximo index del total de banderas se escogeran solo la CANTIDAD necesaria
        flag_index_order = random.sample(range(0, len(up_colores)), up_cantidad)
        print("flag_index_order", flag_index_order)

        # Cambia el orden de los indices de la lista de banderas por patear
        flag_index_order_in_order = random.sample(flag_index_order, len(flag_index_order))
        flag_index_order_in_order.sort()

        # Vacia la lista
        up_ordered_flags = []
        for i in flag_index_order:
            up_ordered_flags.append([up_colores[i], up_puntaje[i]])

        print("up_ordered_flags", up_ordered_flags)

    else:
        # Error!
        playable = False
        print("ERROR: Indice fuera de rango!")

    return playable


# Muestra el orden de las banderas en pantalla
def show_actual_sequence():
    n = 0
    font_size = 20

    # Muestra en pantalla el texto
    for flag in up_ordered_flags:
        # Cantidad de Golpes Restantes
        text = pygame.font.Font("freesansbold.ttf", font_size)  # Font
        text_surface, text_rectangle = text_objects(flag[0], text, (0, 0, 0))
        text_rectangle.center = (70, 115 + font_size * 2 * n)
        initial_window.blit(text_surface, text_rectangle)
        n += 1


# Verifica el correcto orden del juego, sus colisiones, su iteracion y el tiempo restante
def check_correct_order():

    global up_actual_iteration
    global up_actual_iteration_time_left

    still_kicking = True

    # Se actualiza el tiempo restante por iteracion
    up_actual_iteration_time_left = up_end_time - time.time()

    if up_actual_iteration_time_left > 0:
        # Aun queda tiempo en la iteracion actual

        if check_flag_hit():
            # Se ha impactado una bandera correctamente

            if len(up_actual_hitten_flags) == len(up_ordered_flags):
                # Se ha completado la secuencia

                if up_actual_iteration == up_iterations:
                    # Es la ultima secuencia
                    still_kicking = False

                else:
                    # Si quedan iteraciones
                    up_actual_iteration += 1
                    # Actualizar la cantidad de banderas y el tiempo de la siguiente iteracion
                    update_flag_arrangement()
                    print("New Sequence")
        '''
            else:
                # No se ha completado la secuencia
                # print("Nice, keep going")
                True

        else:
            # No se ha impactado correctamente la bandera siguiente en la secuencia
            #print("Not hit and still time left")
            True
        '''
    else:
        # Se acabo el tiempo en la iteracion
        if up_actual_iteration < up_iterations:
            # Si quedan iteraciones
            up_actual_iteration += 1
            # Actualizar la cantidad de banderas y el tiempo de la siguiente iteracion
            update_flag_arrangement()
        else:
            still_kicking = False

    return still_kicking


# Verifica si el personaje ha impactado alguna bandera
# Retorna True si es asi, False si no
def check_flag_hit():

    global flag_x

    has_hit = False

    dflag_x = flag_x

    for i in flag_index_order_in_order:

        # Verifica si ha sido golpeado con la mano derecha
        if rfy < stick_y + flag_height and rfy > stick_y \
                or rfy + fh < stick_y + flag_height and rfy + fh > stick_y:
            if rfx > (dflag_x + space_per_flag*i) and rfx < (dflag_x + space_per_flag*i) + flag_width \
                    or rfx + fw > (dflag_x + space_per_flag*i) and rfx + fw < (dflag_x + space_per_flag*i) + flag_width:
                print("Right Feet Collision")
                has_hit = True
                # hasnt_finished = has_hit_balloon()


        '''
        # ESTE ES IGUAL AL DE ARRIBA (Usa el pie derecho),
        # CAMBIAR POR IZQUIERDO -> lfx y lfy
        
        # Verifica si ha sido golpeado con la mano derecha
        if rfy < stick_y + flag_height and rfy > stick_y \
                or rfy + fh < stick_y + flag_height and rfy + fh > stick_y:
            if rfx > (dflag_x + space_per_flag * i) and rfx < (dflag_x + space_per_flag * i) + flag_width \
                    or rfx + fw > (dflag_x + space_per_flag * i) and rfx + fw < (
                    dflag_x + space_per_flag * i) + flag_width:
                print("Right Feet Collision")
                has_hit = True
                # hasnt_finished = has_hit_balloon()
        '''

    return has_hit










'''
        str_sprite_index = str(get_sprite_index(up_colores[i]))

        # Directorio de la imagen por mostrar actual
        directory = "Resources/Flags/Flag" + str_sprite_index + "/F" + str_sprite_index + str(n) + ".png"

        # Imagen cargada
        flag_n = pygame.image.load(directory)  # Carga la imagen de la carpeta
        # Imagen escalada
        flag_n = pygame.transform.scale(flag_n, (flag_width, flag_height))  # Escala la imagen al size deseado

        # Muestra la imagen en pantalla con las coordenadas preestablecidas
        initial_window.blit(flag_n, (flag_x, stick_y))

        # Aumenta flag_x para la posicion de la siguiente bandera
        flag_x = flag_x + space_per_flag
    




    if correctly hit flag:
        add this flag to hit_flag list
        # up_actual_hitten_flags += hit_flag
        sum score to iteration score
        return True
    elif incorrectly hit flag:
        send error
        +1 to up_failed_sequences
        fail sign
    else:
        send error
        +1 to failed_sequences
        fail sign
        return False
'''



'''
    #RAQUETA GLOBO

    hasnt_finished = True

    # Verifica si ha sido golpeado con la mano derecha
    if rhy < rg_alt + balloon_height and rhy > rg_alt or rhy + hdh < rg_alt + balloon_height and rhy + hdh > rg_alt:
        if rhx > rg_lat and rhx < rg_lat + balloon_width or rhx + hdw > rg_lat and rhx + hdw < rg_lat + balloon_width:
            print("Right Hand Collision")
            hasnt_finished = has_hit_balloon()

    # Verifica si ha sido golpeado con la mano izquierda
    elif lhy < rg_alt + balloon_height and lhy > rg_alt or lhy + hdh < rg_alt + balloon_height and lhy + hdh > rg_alt:
        if lhx > rg_lat and lhx < rg_lat + balloon_width or lhx + hdw > rg_lat and lhx + hdw < rg_lat + balloon_width:
            print("Left Hand Collision")
            hasnt_finished = has_hit_balloon()

    return hasnt_finished
'''









# Actualiza el juego cuando el jugador ha golpeado algun globo
def has_hit_flag():


















    # RAQUETA GLOBO
    global rg_alt
    global rg_lat
    global rg_hit_count
    global rg_score

    mx = balloon_width
    my = displayWidth // 2

    # Actualiza la cantidad de golpes que se han logrado
    rg_hit_count += 1

    # Actualiza el puntaje del juego
    rg_score += rg_balloon_points

    if (rg_cantidad - rg_hit_count) > 0:
        # Actualiza la posicion del globo
        rg_lat = random.randrange(0, displayWidth - mx, 1)
        rg_alt = random.randrange(0, displayHeight - my, 1)

        return True


# Actualiza la cantidad de banderas por utilzar en la secuencia
# Actualiza la cantidad de tiempo por iteracion
def update_flag_arrangement():

    global up_tiempo
    global up_cantidad
    global up_end_time
    global up_actual_iteration_time_left

    up_tiempo += up_dtime
    # No agrega mas banderas si se va a pasar del limite
    if up_cantidad < len(up_flag_color_list):
        up_cantidad += up_dcantidad

    # Modifica las variables de tiempo
    up_end_time = time.time() + up_tiempo
    up_actual_iteration_time_left = up_end_time

    # Modifica la secuencia de banderas
    set_flag_order()


###############################################################################
#                                                                             #
###############################################################################


###############################################################################
#                                                                             #
#                                  TELARAÑA                                   #
#                                                                             #
###############################################################################


# Variables de Telaraña
ta_mi_arreglo = ["Azul", "Rojo", "Naranja"]  #, "Verde", "Amarillo"]
ta_mi_puntaje = [1000, 2000, 3000]  #, 4000, 5000]
ta_mi_fila = 2
ta_mi_col = 2

# Lista de las palabras, con su puntaje y posicion en la web
ta_words_list = []

# Lista de palabras por la cuales el usuario ya ha pasado
ta_owned_words_list = []

# Puntaje
ta_score = 0

# Cambios de posicion
dn = displayWidth // 4  # 97 * 4
dx = 0
dy = 0


# Corre la seleccion de Down Left
def run_dl():
    print("Telaraña")

    # Acomoda las palabras, con su puntaje y genera su posicion en la web
    for_asign_word_initial()

    # Definicion de las variables globales que se necesitan modificar
    global dx
    global dy
    global web_x
    global web_y

    # Crea una superficie
    dl_surface = pygame.Surface((displayWidth, displayHeight))

    # Verifica las posiciones iniciales de la red
    set_starting_point(ta_mi_fila, ta_mi_col)

    # Define las coordenadas viejas
    # redefine_old_coordinates()



    running = True

    while running:

        # change its background color
        dl_surface.fill((255, 255, 255))

        # blit uLSurface onto the main screen at the position (0, 0)
        initial_window.blit(dl_surface, (0, 0))

        # Mostrara la telaraña en pantalla
        place_web(ta_mi_fila, ta_mi_col)

        # Muestra la informacion del juego
        show_info("ta")

        # Muestra las palabras ya encontradas
        show_owned_words()

        # Ingresa las palabras
        for_asign_word()

        # Muestra los pies del niño
        place_feet()

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

            # Si se presiona una tecla
            if event.type == pygame.KEYDOWN:
                # Cambia la direccion del movimiento
                if event.key == pygame.K_LEFT:  # T. Izquierda
                    move_left(dl_surface)
                    # Recoge las palabras cuando se pasa sobre una
                    pick_up_word()
                    # dx = 25
                if event.key == pygame.K_RIGHT:  # T. Derecha
                    move_right(dl_surface)
                    # Recoge las palabras cuando se pasa sobre una
                    pick_up_word()
                    # dx = -25
                if event.key == pygame.K_UP:  # T. Izquierda
                    move_front(dl_surface)
                    # Recoge las palabras cuando se pasa sobre una
                    pick_up_word()
                    # dy = 25
                if event.key == pygame.K_DOWN:  # T. Derecha
                    move_back(dl_surface)
                    # Recoge las palabras cuando se pasa sobre una
                    pick_up_word()
                    # dy = -25
                continue

            # Si se suelta una tecla
            if event.type == pygame.KEYUP:
                # Retorna el movimiento a 0, lo hace estatico de nuevo
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # T. Izquierda o T. Derecha
                    print("RESTORE")
                    #restore_change()
                    # dx = 0
                    # dy = 0

        # Verifica los gestos con las coordenadas del Kinect
        check_gesture(dl_surface)

        # Actualiza la posicion de la web
        web_x += dx
        web_y += dy

        # Reestablece el cambio si se necesito al graficar los pies
        restore_change()

        # Verifica si se han recogido todas las palabras
        if not check_words_completed():
            running = end_game("ta")

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
        pygame.draw.rect(initial_window, (0, 0, 0),
                         (web_x * multiplier, (web_y + web_separation * (x + 0)) * multiplier,
                          (web_separation + web_separation * (columns - 2) + web_width) * multiplier,
                          web_width * multiplier))

    for y in range(0, columns):
        # Dibuja rect(posX, posY, ancho, height)
        pygame.draw.rect(initial_window, (0, 0, 0),
                         ((web_x + web_separation * (y + 0)) * multiplier, web_y * multiplier,
                          web_width * multiplier, (web_separation + web_separation * (rows - 2)) * multiplier))


# Define el punto de inicio de la web
def set_starting_point(rows, columns):
    global web_x
    global web_y

    web_x = 0
    web_y = 0

    global ta_sx
    global ta_sy

    ta_sx = - ((web_separation + web_separation * (columns - 2)) // 2 - web_separation // 2 + web_width // 2) * multiplier
    ta_sy = - (web_separation + web_separation * (rows - 2) - web_separation // 4 - web_width) * multiplier

    web_x += ta_sx
    web_y += ta_sy


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
    shoe_l = pygame.transform.scale(shoe_l, (int(shoe_width * multiplier), int(shoe_height * multiplier)))
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(shoe_l, (shoe_l_x, shoe_l_y))

    # Directorio de la imagen por mostrar actual
    shoe_r_directory = "Resources/Character/topShoeRsmall.png"
    # Imagen cargada
    shoe_r = pygame.image.load(shoe_r_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    shoe_r = pygame.transform.scale(shoe_r, (int(shoe_width * multiplier), int(shoe_height * multiplier)))
    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(shoe_r, (shoe_r_x, shoe_r_y))


# Asigna las palabras, con su respectivo puntaje, las posiciones en la web
def for_asign_word_initial():
    global ta_words_list

    # INGRESO DE PALABRAS
    n = 0
    # Crea una lista de elementos con un lista para la palabra en la lista de palabras
    for i in ta_mi_arreglo:
        # Agrega una lista solo con la palabra, a esta luego se le ingresan parametros
        ta_words_list.append([i])
        n += 1

    # INGRESO DE PUNTAJE
    m = 0
    # Ingresa el puntaje en la lista propia de la palabra
    for j in ta_mi_puntaje:
        ta_words_list[m].append(j)
        m += 1

    # INGRESO DE COORDENADA DE FILA
    # Lista de filas para mostrar la palabra
    row_list = []

    # Se verifica que row_list siempre tenga suficientes filas para la cantidad de palabras
    if ta_mi_fila < len(ta_mi_arreglo):
        while len(row_list) < len(ta_mi_arreglo):
            dlist = random.sample(range(0, ta_mi_fila), ta_mi_fila)
            row_list += dlist
    else:
        row_list = random.sample(range(0, ta_mi_fila), ta_mi_fila)

    f = 0
    # Ingresa la fila en la lista propia de la palabra
    while f < len(ta_words_list):
        ta_words_list[f].append(row_list[f])
        f += 1

    # INGRESO DE COORDENADA DE COLUMNA
    # Lista de columnas para mostrar la palabra
    column_list = []

    # Se verifica que column_list siempre tenga suficientes columnas para la cantidad de palabras
    if ta_mi_col < len(ta_mi_arreglo):
        while len(column_list) < len(ta_mi_arreglo):
            dlist = random.sample(range(0, ta_mi_col), ta_mi_col)
            column_list += dlist
    else:
        column_list = random.sample(range(0, ta_mi_col), ta_mi_col)

    c = 0
    # Ingresa la columna en la lista propia de la palabra
    while c < len(ta_words_list):
        ta_words_list[c].append(column_list[c])
        c += 1

    print(ta_words_list)


# Toma la lista de palabras ya lista para mostrarlas en pantalla
def for_asign_word():
    # PARA INGRESAR EN LA WEB
    for i in range(len(ta_words_list)):
        # show_word(str(ta_words_list[i][0]), str(ta_words_list[i][1]), ta_words_list[i][2], ta_words_list[i][3])
        show_word(ta_words_list[i][2], ta_words_list[i][3], str(ta_words_list[i][0]), ta_words_list[i][1])


# Dimensiones de las palabras por mostrar en la web
word_width = 250
word_height = 150


# Muestra el cuadro de la palabra en la web
# def show_word(word, score, row, column):
def show_word(row, column, word, score):
    # print("row: " + str(row) + "\ncolumn: " + str(column) + "\nword: " + word + "\nscore: " + str(score))

    word_x = (web_x + web_separation * column - word_width // 2 + web_width // 2) * multiplier
    word_y = (web_y + web_separation * row - word_height // 2 + web_width // 2) * multiplier

    word_separation = 10

    # Dibuja rect(posX, posY, ancho, height)
    pygame.draw.rect(initial_window, (0, 0, 0),
                     (word_x - word_separation, word_y - word_separation,
                      (word_width + word_separation * 2) * multiplier,
                      (word_height + word_separation * 2) * multiplier))

    # Dibuja rect(posX, posY, ancho, height)
    pygame.draw.rect(initial_window, (255, 127, 127),
                     (word_x, word_y, word_width * multiplier, word_height * multiplier))

    # Para mostrar la palabra
    text = pygame.font.Font("freesansbold.ttf", int(50 * multiplier))  # Font
    text_surface, text_rectangle = text_objects(word, text, (255, 255, 255))
    text_rectangle.center = ((word_x + word_width // 2), (word_y + word_height // 2))
    initial_window.blit(text_surface, text_rectangle)


'''
# Shoe Dimensions
shoe_width = 774 // 8
shoe_height = 1920 // 8
shoe_l_x = (displayWidth // 2) - (shoe_width) - 50
shoe_l_y = displayHeight - (displayWidth * 3 // 7)
shoe_r_x = (displayWidth // 2) + 50  # + (shoe_width)
shoe_r_y = shoe_l_y
'''

# Tiempo inicial para comparar los gestos
time_o = time.time()

wait_time_min = 0.8
wait_time_max = 2

gesture_change = 25


# Verifica el gesto para mover al personaje
def check_gesture(surface):

    # print("UNCOMMENT check_gesture(surface)")

    global time_o

    # print("NOTTime change: " + str(time.time() - time_o))
    # print("NOTold_lhy: " + str(old_lhy) + "\nlhy: " + str(lhy))

    if wait_time_min < (time.time() - time_o): # < wait_time_max:

        print("Time change: " + str(time.time() - time_o))
        print("old_lhy: " + str(old_lhy) + "\nlhy: " + str(lhy))

        # Cambia la direccion del movimiento
        if old_lhy - gesture_change > lhy:  # T. Izquierda
            move_left(surface)
            print("move_left(surface)")

        elif old_rhy - gesture_change > rhy:  # T. Derecha
            move_right(surface)
            print("move_right(surface)")

        elif old_lfy - gesture_change > lfy:  # T. Izquierda
            move_front(surface)
            print("move_front(surface)")

        elif old_rfy - gesture_change > rfy:  # T. Derecha
            move_back(surface)
            print("move_back(surface)")

        # Verifica si llega a recoger una palabra
        pick_up_word()

        time_o = time.time()

        redefine_old_coordinates()


# Redefine las coordenadas viejas para compararse en la telarana
def redefine_old_coordinates():
    global old_lhx
    global old_lhy
    global old_rhx
    global old_rhy
    global old_lfx
    global old_lfy
    global old_rfx
    global old_rfy

    old_lhx = lhx
    old_lhy = lhy
    old_rhx = rhx
    old_rhy = rhy
    old_lfx = lfx
    old_lfy = lfy
    old_rfx = rfx
    old_rfy = rfy


# Mueve el personaje hacia delante
def move_front(surface):

    global ta_sr
    ta_sr -= 0.25

    global dy
    dy = dn

    global shoe_r_y
    global shoe_l_y

    shoe_r_y -= dy

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initial_window.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)

    # Muestra la informacion del juego
    show_info("ta")

    # Muestra las palabras ya encontradas
    show_owned_words()

    # Ingresa las palabras
    for_asign_word()

    # Ingresa una palabra
    '''show_word(1, 1, "Word3", 5000)
    show_word(0, 3, "Word1", 5000)
    show_word(1, 2, "Word4", 5000)
    show_word(2, 3, "Word2", 5000)
    show_word(3, 3, "Word5", 5000)
    show_word(1, 0, "Word6", 5000)
    show_word(4, 9, "Word7", 5000)
    show_word(5, 9, "Word8", 5000)'''

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
    initial_window.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)

    # Muestra la informacion del juego
    show_info("ta")

    # Muestra las palabras ya encontradas
    show_owned_words()

    # Ingresa las palabras
    for_asign_word()

    # Ingresa una palabra
    '''show_word(1, 1, "Word3", 5000)
    show_word(0, 3, "Word1", 5000)
    show_word(1, 2, "Word4", 5000)
    show_word(2, 3, "Word2", 5000)
    show_word(3, 3, "Word5", 5000)
    show_word(1, 0, "Word6", 5000)
    show_word(4, 9, "Word7", 5000)
    show_word(5, 9, "Word8", 5000)'''

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

    global ta_sr
    ta_sr += 0.25

    global dy
    dy = -dn

    global shoe_r_y
    global shoe_l_y

    shoe_r_y -= dy

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initial_window.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)

    # Muestra la informacion del juego
    show_info("ta")

    # Muestra las palabras ya encontradas
    show_owned_words()

    # Ingresa las palabras
    for_asign_word()

    # Ingresa una palabra
    '''show_word(1, 1, "Word3", 5000)
    show_word(0, 3, "Word1", 5000)
    show_word(1, 2, "Word4", 5000)
    show_word(2, 3, "Word2", 5000)
    show_word(3, 3, "Word5", 5000)
    show_word(1, 0, "Word6", 5000)
    show_word(4, 9, "Word7", 5000)
    show_word(5, 9, "Word8", 5000)'''

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
    initial_window.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)

    # Muestra la informacion del juego
    show_info("ta")

    # Muestra las palabras ya encontradas
    show_owned_words()

    # Ingresa las palabras
    for_asign_word()

    # Ingresa una palabra
    '''show_word(1, 1, "Word3", 5000)
    show_word(0, 3, "Word1", 5000)
    show_word(1, 2, "Word4", 5000)
    show_word(2, 3, "Word2", 5000)
    show_word(3, 3, "Word5", 5000)
    show_word(1, 0, "Word6", 5000)
    show_word(4, 9, "Word7", 5000)
    show_word(5, 9, "Word8", 5000)'''

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
def move_right(surface):

    global ta_sc
    ta_sc += 0.25

    global dx
    dx = -dn

    global shoe_r_x
    global shoe_l_x

    shoe_r_x -= dx

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initial_window.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)

    # Muestra la informacion del juego
    show_info("ta")

    # Muestra las palabras ya encontradas
    show_owned_words()

    # Ingresa las palabras
    for_asign_word()

    # Ingresa una palabra
    '''show_word(1, 1, "Word3", 5000)
    show_word(0, 3, "Word1", 5000)
    show_word(1, 2, "Word4", 5000)
    show_word(2, 3, "Word2", 5000)
    show_word(3, 3, "Word5", 5000)
    show_word(1, 0, "Word6", 5000)
    show_word(4, 9, "Word7", 5000)
    show_word(5, 9, "Word8", 5000)'''

    # Muestra los pies del niño
    place_feet()
    # Update display (Actualiza _todo el surface)
    pygame.display.update()
    # Da tiempo para que se grafiquen
    time.sleep(0.3)

    # Segundo Movimiento

    shoe_l_x -= dx

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initial_window.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)

    # Muestra la informacion del juego
    show_info("ta")

    # Muestra las palabras ya encontradas
    show_owned_words()

    # Ingresa las palabras
    for_asign_word()

    # Ingresa una palabra
    '''show_word(1, 1, "Word3", 5000)
    show_word(0, 3, "Word1", 5000)
    show_word(1, 2, "Word4", 5000)
    show_word(2, 3, "Word2", 5000)
    show_word(3, 3, "Word5", 5000)
    show_word(1, 0, "Word6", 5000)
    show_word(4, 9, "Word7", 5000)
    show_word(5, 9, "Word8", 5000)'''

    # Muestra los pies del niño
    place_feet()
    # Update display (Actualiza _todo el surface)
    pygame.display.update()
    # Da tiempo para que se grafiquen
    time.sleep(0.3)

    shoe_r_x += dx
    shoe_l_x += dx

    time.sleep(0.3)


# Mueve el personaje hacia la izquierda
def move_left(surface):

    global ta_sc
    ta_sc -= 0.25

    global dx
    dx = dn

    global shoe_r_x
    global shoe_l_x

    shoe_l_x -= dx

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initial_window.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)

    # Muestra la informacion del juego
    show_info("ta")

    # Muestra las palabras ya encontradas
    show_owned_words()

    # Ingresa las palabras
    for_asign_word()

    # Ingresa una palabra
    '''show_word(1, 1, "Word3", 5000)
    show_word(0, 3, "Word1", 5000)
    show_word(1, 2, "Word4", 5000)
    show_word(2, 3, "Word2", 5000)
    show_word(3, 3, "Word5", 5000)
    show_word(1, 0, "Word6", 5000)
    show_word(4, 9, "Word7", 5000)
    show_word(5, 9, "Word8", 5000)'''

    # Muestra los pies del niño
    place_feet()
    # Update display (Actualiza _todo el surface)
    pygame.display.update()
    # Da tiempo para que se grafiquen
    time.sleep(0.3)

    # Segundo Movimiento

    shoe_r_x -= dx

    # change its background color
    surface.fill((255, 255, 255))
    # blit uLSurface onto the main screen at the position (0, 0)
    initial_window.blit(surface, (0, 0))
    # Mostrara la telaraña en pantalla
    place_web(ta_mi_fila, ta_mi_col)

    # Muestra la informacion del juego
    show_info("ta")

    # Muestra las palabras ya encontradas
    show_owned_words()

    # Ingresa las palabras
    for_asign_word()

    # Ingresa una palabra
    '''show_word(1, 1, "Word3", 5000)
    show_word(0, 3, "Word1", 5000)
    show_word(1, 2, "Word4", 5000)
    show_word(2, 3, "Word2", 5000)
    show_word(3, 3, "Word5", 5000)
    show_word(1, 0, "Word6", 5000)
    show_word(4, 9, "Word7", 5000)
    show_word(5, 9, "Word8", 5000)'''

    # Muestra los pies del niño
    place_feet()
    # Update display (Actualiza _todo el surface)
    pygame.display.update()
    # Da tiempo para que se grafiquen
    time.sleep(0.3)

    shoe_r_x += dx
    shoe_l_x += dx

    time.sleep(0.3)


# Reestablece el cambio de los zapatos a cero cuando no esta presionado la tecla
def restore_change():
    global dx
    global dy
    dx = 0
    dy = 0


ta_sx = 0
ta_sy = 0
ta_sr = ta_mi_fila - 1
ta_sc = ta_mi_col / 2 - 0.5


# Dependiendo de la posicion del usuario, recoge las palabras por las cuales ya ha pasado
def pick_up_word():

    global ta_score

    # Verifica las coordenadas por fila y columna ta_sr y ta_sc
    # para ver si son iguales a la posicion de alguna palabra en la web
    for word in ta_words_list:
        check_rows = word[2] == ta_sr
        check_columns = word[3] == ta_sc
        if check_rows & check_columns:

            already_picked = False

            for found in ta_owned_words_list:
                if found[0] == word[0]:
                    already_picked = True

            if not already_picked:
                print("Picked up: " + word[0])
                # Ingresa la palabra y sus atributos a la lista de palabras encontradas
                ta_owned_words_list.append(word)
                # Actualiza el puntaje
                ta_score += word[1]

            # Verifica si se han completado todas las palabras


# Muestra las palabras en pantalla
def show_owned_words():
    n = 0
    font_size = 20

    # Muestra en pantalla el texto
    for words in ta_owned_words_list:
        # Cantidad de Golpes Restantes
        text = pygame.font.Font("freesansbold.ttf", font_size)  # Font
        text_surface, text_rectangle = text_objects(words[0], text, (0, 0, 0))
        text_rectangle.center = (70, 50 + font_size * 2 * n)
        initial_window.blit(text_surface, text_rectangle)
        n += 1


# Verifica que se hayan recogido todas las palabras
def check_words_completed():
    incomplete_words = True

    if len(ta_owned_words_list) == len(ta_words_list):
        incomplete_words = False

    return incomplete_words


###############################################################################
#                                                                             #
###############################################################################


###############################################################################
#                                                                             #
#                           Alcanzando el Objetivo                            #
#                                                                             #
###############################################################################


# Variables de Alcanzando el Objetivo
ao_object_longitud = 200  # Fija
ao_object_altura = 500  # Fija

ao_object_x = displayWidth - ao_object_longitud  # Actualizable
ao_object_y = displayHeight - ao_object_altura  # Actualizable

# Lista de distancias
ao_distances = [2, 5, 1, 7, 1]  # 4, 9, 6, 3,

# Cantidad de iteraciones es igual a la cantidad de distancias
ao_cantidad = len(ao_distances)

# Time
ao_seconds = 4  # Fija
ao_seconds_left = ao_seconds * ao_cantidad  # Actualizable

# Iteracion actual
ao_actual_iteration = 1

# Tiempo total del juego
ao_total_seconds = ao_seconds * ao_cantidad

# Score
ao_score = 0
ao_max_score = 10000


# Corre la seleccion de Down Right
def run_dr():
    print("Alcanzando el Objetivo")

    global ao_seconds_left

    # Para el sprite del object
    n = 1

    # Flag
    running = True

    t_end = time.time() + ao_total_seconds

    # while running:
    while time.time() < t_end and running:

        ao_seconds_left = int(t_end - time.time())

        # Muestra el background
        show_backroom()

        # Muestra el objeto
        place_object((n % 2) + 1)

        # Para cambiar el sprite del globo
        n += 1

        # Obtiene las coordenadas del Kinect
        get_coordinates_from_kinect()
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

        # Verifica si se impacta al objeto y termina el juego
        if not check_object_hit():
            running = end_game("ao")

        # Muestra la informacion del juego
        show_info("ao")

        # Update display (Actualiza _todo el surface)
        pygame.display.update()


# Dimensiones del objeto
ao_object_width = balloon_width
ao_object_height = balloon_height


# Posiciona el objeto y muestra el sprite que se necesite
# @param x
# @param y
# @param n: sprite del objeto
def place_object(n):
    # Directorio de la imagen por mostrar actual
    ao_object_directory = "Resources/Balloon/balloon" + str(n) + ".png"
    # Imagen cargada
    ao_object = pygame.image.load(ao_object_directory)  # Carga la imagen de la carpeta
    # Imagen escalada
    ao_object = pygame.transform.scale(ao_object,
                                       (ao_object_width, ao_object_height))  # Escala la imagen al size deseado

    # Muestra la imagen en pantalla con las coordenadas preestablecidas
    initial_window.blit(ao_object, (ao_object_x, ao_object_y))


# Verifica si el personaje ha impactado al objeto
# Si lo impacta envia un False para acabar el juego
def check_object_hit():
    # Flag para saber si este juego ha terminado
    hasnt_finished = True

    if rhy < ao_object_y + ao_object_height and rhy > ao_object_y \
            or rhy + hdh < ao_object_y + ao_object_height and rhy + hdh > ao_object_y:

        if rhx > ao_object_x and rhx < ao_object_x + ao_object_width \
                or rhx + hdw > ao_object_x and rhx + hdw < ao_object_x + ao_object_width:
            print("Rigth Hand Collision")
            hasnt_finished = False
            set_object_score()

    elif lhy < ao_object_y + ao_object_height and lhy > ao_object_y \
            or lhy + hdh < ao_object_y + ao_object_height and lhy + hdh > ao_object_y:

        if lhx > ao_object_x and lhx < ao_object_x + ao_object_width \
                or lhx + hdw > ao_object_x and lhx + hdw < ao_object_x + ao_object_width:
            print("Left Hand Collision")
            hasnt_finished = False
            set_object_score()

    else:
        # Al no ser golpeado
        hasnt_finished = set_object_state()

    return hasnt_finished


# Define la posicion del objeto y el tiempo restante por posicion
def set_object_state():
    continue_setting = True

    global ao_actual_iteration

    # Tiempo al cual se tiene que cambiar de iteracion
    iteration_change_time = (ao_cantidad - ao_actual_iteration) * ao_seconds

    # Si falta tiempo
    if ao_seconds_left > 0:

        print("Iteration: " + str(ao_actual_iteration))
        print("Iteration Change Time: " + str(iteration_change_time))

        # Si es tiempo de cambiar de iteracion
        if ao_seconds_left < iteration_change_time:
            # Cambia de iteracion
            ao_actual_iteration += 1
            # Cambia la posicion del objeto
            change_object_position()

    else:
        # Tiempo se ha acabado, se terminara el juego
        continue_setting = False

    return continue_setting


ao_highest = max(ao_distances)
ao_distance_multiplier = displayHeight // ao_highest


# Cambia la posicion del objeto por la siguiente en la lista
# Promedia la distancia mas alta para que ninguna se salga de la ventana
def change_object_position():
    global ao_object_x
    global ao_object_y

    # Toma la siguiente posicion de la lista de posiciones brindada por el usuario
    new_y = ao_distances[ao_actual_iteration - 1]

    # Cambia las posiciones del objeto
    ao_object_y = ao_distance_multiplier * new_y
    ao_object_x = random.randrange(0, displayWidth - ao_object_width, 1)


# Define el puntaje del Juego AO
def set_object_score():
    global ao_score

    ao_score = int((ao_max_score // ao_total_seconds + 0.000001) * (ao_seconds_left + 0.000001))


###############################################################################
#                                                                             #
###############################################################################


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
        initial_window.blit(s_surface, (0, 0))

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

'''bx = displayWidth // 2 - 40
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
rfy = lfy'''

bx = -200
by = -200
hx = -200
hy = -200
lhx = -200
lhy = -200
rhx = -200
rhy = -200
lfx = -200
lfy = -200
rfx = -200
rfy = -200

character_coordinates = [bx, by, lhx, lhy, rhx, rhy, lfx, lfy, rfx, rfy]

old_lhx = lhx
old_lhy = lhy
old_rhx = rhx
old_rhy = rhy
old_lfx = lfx
old_lfy = lfy
old_rfx = rfx
old_rfy = rfy


# Muestra el personaje en pantalla
def show_character():
    # Directorio de la cabeza
    head_directory = "Resources/Character/headsmall.png"
    head = pygame.image.load(head_directory)
    # head = pygame.transform.scale(head, (hw, hh))
    initial_window.blit(head, (hx, hy))

    # Directorio del cuerpo
    body_directory = "Resources/Character/bodysmall.png"
    body = pygame.image.load(body_directory)
    # body = pygame.transform.scale(body, (bw, bh))
    initial_window.blit(body, (bx, by))

    # Directorio de la mano izquierda
    hand_l_directory = "Resources/Character/handLsmall.png"
    hand_l = pygame.image.load(hand_l_directory)
    # hand_l = pygame.transform.scale(hand_l, (hdw, hdh))
    initial_window.blit(hand_l, (lhx, lhy))

    # Directorio de la mano derecha
    hand_r_directory = "Resources/Character/handRsmall.png"
    hand_r = pygame.image.load(hand_r_directory)
    # hand_r = pygame.transform.scale(hand_r, (hdw, hdh))
    initial_window.blit(hand_r, (rhx, rhy))

    # Directorio del pie izquierdo
    shoe_l_directory = "Resources/Character/shoeLsmall.png"
    shoe_l = pygame.image.load(shoe_l_directory)
    # shoe_l = pygame.transform.scale(shoe_l, (fw, fh))
    initial_window.blit(shoe_l, (lfx, lfy))

    # Directorio del pie derecho
    shoe_r_directory = "Resources/Character/shoeRsmall.png"
    shoe_r = pygame.image.load(shoe_r_directory)
    # shoe_r = pygame.transform.scale(shoe_r, (fw, fh))
    initial_window.blit(shoe_r, (rfx, rfy))


# Muestra solo la mano derecha, que sera utilizada para seleccionar
def show_hand_selection():
    global rhx
    global rhy

    # Modificar la posicion de la mano para escoger mas facilmente si cambiar la mano de cuadrante
    rhx = (rhx - displayWidth // 2) * 4 - 200
    rhy = rhy * 2 - 100

    # Directorio de la mano derecha
    hand_r_directory = "Resources/Character/handRsmall.png"
    hand_r = pygame.image.load(hand_r_directory)
    hand_r = pygame.transform.scale(hand_r, (hdw, hdh))
    initial_window.blit(hand_r, (rhx, rhy))


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

    multx = 1.5625
    multy = 1.3541

    '''
    bx = dbx * multx - bw // 2
    by = dby * multy - 100
    hx = bx - 20 - hdw // 2
    hy = by - hh - 10
    lhx = dlhx * multx
    lhy = dlhy * multy
    rhx = drhx * multx
    rhy = drhy * multy
    lfx = dlfx * multx
    lfy = dlfy * multy
    rfx = drfx * multx
    rfy = drfy * multy
    '''

    # Coordenada x del cuerpo
    if -5 < dbx < 5:
        bx = -200
        hx = 0
    else:
        bx = dbx * multx - bw // 2
        hx = bx - 20 - hdw // 2
    # Coordenada y del cuerpo
    if -5 < dby < 5:
        by = -200
        hy = -200
    else:
        by = dby * multy - 100
        hy = by - hh - 10

    # Coordenada x de la mano izquierda
    if -5 < dlhx < 5:
        lhx = -200
    else:
        lhx = dlhx * multx
    # Coordenada y de la mano izquierda
    if -5 < dlhy < 5:
        lhy = -200
    else:
        lhy = dlhy * multy

    # Coordenada x de la mano derecha
    if -5 < drhx < 5:
        rhx = -200
    else:
        rhx = drhx * multx
    # Coordenada y de la mano derecha
    if -5 < drhy < 5:
        rhy = -200
    else:
        rhy = drhy * multy

    # Coordenada x del pie izquierdo
    if -5 < dlfx < 5:
        lfx = -200
    else:
        lfx = dlfx * multx
    # Coordenada y del pie izquierdo
    if -5 < dlfy < 5:
        lfy = -200
    else:
        lfy = dlfy * multy

    # Coordenada x del pie derecho
    if -5 < drfx < 5:
        rfx = -200
    else:
        rfx = drfx * multx
    # Coordenada y del pie derecho
    if -5 < drfy < 5:
        rfy = -200
    else:
        rfy = drfy * multy


'''
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
'''

# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.100.80', 5555))


# Abre una conexion con Processing para obtener las coordenadas del Kinect
def get_coordinates_from_kinect():

    '''
    # For testing w/o Kinect
    get_coordinates()
    print("UNCOMMENT check_gesture(surface)") # AND CLIENT UPWARDS'''

    client.send(b"I am CLIENT\n")

    data = client.recv(1024).decode('UTF-8')

    if not data:
        print("No Data")
    else:
        # print('Received:' + repr(data))
        n = 0
        coord = ""
        coords = []
        # data = data[1:]
        while data != "":
            if data[0] != ",":
                coord += data[0]
            else:
                # print("->", coord)
                n += 1
                coords.append(int(coord))
                coord = ""
            data = data[1:]
        # print("->", coord)
        coords.append(int(coord))

        # Actualiza las coordenadas de las posiciones del cuerpo por graficar
        update_character_coordinates(coords[0], coords[1], coords[2], coords[3], coords[4],
                                     coords[5], coords[6], coords[7], coords[8], coords[9])


# Flag
playing = True

# Main Loop
while playing:

    # Cambia el fondo de la superficie
    initial_window.fill(black)

    # Muestra las posibles cuadros de las opciones de los juegos
    show_main_options()

    # Obtiene las coordenadas del Kinect
    get_coordinates_from_kinect()
    # Muestra la mano derecha para seleccionar una opcion
    show_hand_selection()

    # Pygame verifica todos los events
    for event in pygame.event.get():

        # Si se cierra la ventana
        if event.type == pygame.QUIT:
            # Va a salir del while
            playing = False
            print("QUIT")

        # Al presionar el mouse [NO SE USARA]
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Obtiene las posiciones actuales del mouse
            mousex, mousey = pygame.mouse.get_pos()
            # Verifica si puede ingresar a una opcion
            mouse_click_main_selection(mousex, mousey)

    # Verifica la seleccion de la mano
    check_hand_main_options_selection()

    # Update display (Actualiza _todo el surface)
    pygame.display.update()

    # Parametro serian la cantidad de frames en un segundo (fps)
    clock.tick(fps)

# Cierra el cliente
client.close()

# Deja de correr Pygame
pygame.quit()
