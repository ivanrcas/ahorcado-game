'''
* Nombre: Proyecto Pygame | Juego del Ahorcado
* Modulo: button
* Descripcion: Clase de boton que permite construir un objeto de boton permitiendo eventos de click en el lienzo de screen.
* Desarrollado por: Ivan Castillo
* Fecha: Marzo de 2024
'''


import pygame

class Button:
    # constructor con texto, posicion, window y fuente
    def __init__(self, txt, pos, win, font):
        self.text = txt
        self.pos = pos
        self.win = win
        self.font = font
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (240, 40))

    def draw(self):
        pygame.draw.rect(self.win, 'light gray', self.button, 0, 5)
        pygame.draw.rect(self.win, 'dark gray', [self.pos[0], self.pos[1], 240, 40], 5, 5)
        text2 = self.font.render(self.text, True, 'black')
        self.win.blit(text2, (self.pos[0] + 50, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False