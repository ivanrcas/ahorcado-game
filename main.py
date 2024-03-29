'''
* Nombre: Proyecto Pygame | Juego del Ahorcado
* Modulo: main
* Descripcion: Juego desarrollado con pygame basado en el juego del ahorcado con tres niveles dificultad
  con elementos visuales de botones, imagenes y formas geometricas.
* Modulo dependiente: button
* Desarrollado por: Ivan Castillo
* Fecha: Marzo de 2024
'''

# Impportar librerias y modulo de botón
import pygame
import math
import random
import button

# Configurar display
pygame.init()
WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ahorcado The Game | Kodland")

# Configurar musica de fondo
pygame.mixer.init()
pygame.mixer.music.load('ahorcado\\music\\music_backgroud_ocarina.mp3')
pygame.mixer.music.play(loops = -1)

# Definicion de Configuracion fuentes y tamanos de texto
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)
font = pygame.font.SysFont('comicsans', 22)

# Definicion de variables globales de juego
AHORCADO_ATTEMPS = 0
WORDS = ['KODLAND', 'PYTHON', 'IDE', 'PYGAME', 'BUCLE', 'CONDICION']
WORD = random.choice(WORDS)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0,128,0)
RADIUS = 20
GAP = 15

# Funcion para generar lista de las 27 letras del abecedario sin la ñ con sus respectivas coordenadas en display
def letters_list():
    letters = []
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
    starty = 400
    A = 65
    for i in range(26):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(A + i), True])
    return letters

# Funcion para generar lista de imagenes de formato .png que incluye seis partes de un cuerpo animado
def images_list():
    images = []
    for i in range(7):
        image = pygame.image.load("ahorcado\\images\\ahorcado" + str(i) + '.png')
        images.append(image)
    return images

# MENU PRINCIPAL
# Funcion para dibujar menu principal. Contiene lógica de los niveles de dificultad-
def draw_main_menu():
    WIN.fill(WHITE)

    # Titulo del juego y subtitulo
    text_title = TITLE_FONT.render("EL AHORCADO", 1, GREEN)
    WIN.blit(text_title, (WIDTH / 2 - text_title.get_width() / 2, 5))
    text_subtitle = LETTER_FONT.render("Juego Prueba de Kodland", 1, BLACK)
    WIN.blit(text_subtitle, (WIDTH / 2 - text_subtitle.get_width() / 2, 90))

    # Boton Nivel facil
    menu_btn_easy = button.Button('Nivel Bajo', ((WIDTH / 2.7), 200), WIN, font)
    menu_btn_easy.draw()
    clicked_menu_btn_easy = menu_btn_easy.check_clicked()

    # Boton nivel medio
    menu_btn_medium = button.Button('Nivel Medio', ((WIDTH / 2.7), 250), WIN, font)
    menu_btn_medium.draw()
    clicked_menu_btn_medium = menu_btn_medium.check_clicked()

    # Boton nivel alto
    menu_btn_hard = button.Button('Nivel Alto', ((WIDTH / 2.7), 300), WIN, font)
    menu_btn_hard.draw()
    clicked_menu_btn_hard = menu_btn_hard.check_clicked()
    
    # Texto de Creditos
    text_credits = font.render("Desarrollado por Ivan Castillo", 1, BLACK)
    WIN.blit(text_credits, (WIDTH / 2 - text_credits.get_width() / 2 - 30, 500))
    
    # Lógica de niveles de dificultad
    # Validar evento de click en los botones y definir numero de intentos en variable _attemps_ con su respectivo flag _menu_
    menu = False
    attemps = 6
    if clicked_menu_btn_easy:
        menu = clicked_menu_btn_easy
        attemps = 18
    if clicked_menu_btn_medium:
        menu = clicked_menu_btn_medium
        attemps = 12
    if clicked_menu_btn_hard:
        menu = clicked_menu_btn_hard
        attemps = 6
    return menu, attemps    

# SCREEN DE VIDEOJUEGO
# Funcion de dibujo de componentes en screen con parámetros de: letters, images.
def draw(letters, images, attemps):
    WIN.fill(WHITE)
    # draw title
    text = TITLE_FONT.render("EL AHORCADO", 1, GREEN)
    WIN.blit(text, (WIDTH / 2 - text.get_width() / 2, 5))
    # draw WORD
    display_word = ""
    for letter in WORD:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    WIN.blit(text, (400, 200))
    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(WIN, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            WIN.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    # Print y blint de screen del visual los intentos fallidos en imagenes y texto segun el valor de AHORCADO_ATTEMPS (del 1 al 6).
    WIN.blit(images[AHORCADO_ATTEMPS%6], (150, 100))
    status_failed = f"Intentos Fallidos: {AHORCADO_ATTEMPS} de {attemps}"
    text = font.render(status_failed, 1, BLACK)
    WIN.blit(text, (900, 20))

    # Boton de reiniciar juego ubicado en la parte inferior. A partir del flag _command_ se determina el estado del evento click
    command = -1
    menu = button.Button('Reiniciar Juego', (120, 500), WIN, font)
    menu.draw()
    if menu.check_clicked():
        command = 0
    pygame.display.update()
    return command

# Función de mostrar mensaje de finalización de juego: victoria o perdida
def display_message(message):
    pygame.time.delay(1000)
    WIN.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    WIN.blit(text, ((WIDTH / 2 - text.get_width() / 2), (HEIGHT / 2 - text.get_height() / 2)))
    pygame.display.update()
    pygame.time.delay(3000)

# Funcion Main: Contiene la lógica iterativa del juego mediante estructura while y el flag Run
def main(letters, images, attemps):
    global AHORCADO_ATTEMPS
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    command = draw(letters, images, attemps)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Validar posicion del cursor cuando se activa el evento MOUSEBUTTONDOWN y validar visibilidad de los botones en forma de circulo existenten en el screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in WORD:
                                AHORCADO_ATTEMPS += 1
                                
        # Validar si la letra no se encuentra en la lista de letras a adivinar. Si cumple condicion, se finaliza la interaccion
        won = True
        for letter in WORD:
            if letter not in guessed:
                won = False
                break
        
        # Validar si el flag _won_ es verdadero, imprimir mensaje de victoria y finalizar iteracción
        if won:
            display_message('GANASTE  :D')
            run = False
            command = 0
            AHORCADO_ATTEMPS = 0
            won = False
            break

        # Validar si el flag _ahorcado_status_ alcanza el tope de intentos y  y finalizar iteracción  
        if AHORCADO_ATTEMPS == attemps:
            display_message('PERDISTE  :(')
            run = False
            command = 0
            AHORCADO_ATTEMPS = 0
            won = False
            break
        return command

# Ejecutar juego definiendole al interprete en el modulo __main__
if __name__ == '__main__':
    
    main_menu = False
    runing = True
    while runing:
        # Ejecutar mientras que variable flag main_menu sea verdadero. Si es falsa la variable de la flag, generar menu principal/
        if main_menu:
            # Invocar funcion main con los parametros inicial de configuracion
            menu_command = main(letters, images, attemps)
            if menu_command != -1:
                main_menu = False
        else:
            # reset de variables de ejecucion
            AHORCADO_ATTEMPS = 0
            letters = letters_list()
            images = images_list()
            guessed = []
            main_menu, attemps = draw_main_menu()

        # Ciclo de obtener evento para validar cierre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False
                break
        # actualizar screen
        pygame.display.update()
    pygame.quit()