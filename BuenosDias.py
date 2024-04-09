import random

import pygame

pygame.init()


def escribir(fuente, tam, text, color):
    font = pygame.font.SysFont(fuente, tam)
    texto = font.render(text, True, color)
    text_width, text_height = texto.get_size()
    return texto, text_width, text_height


screen = pygame.display.set_mode((800, 600))
heightScreen = screen.get_height()
widthScreen = screen.get_width()
pygame.display.set_caption('Buenos días amor')
pos_x = widthScreen
inicio = True
lvl_amor = 0
max_amor = False
direction = 1
speed = 4
coord_list = []
for i in range(100):
    x = random.randint(0, widthScreen)
    y = random.randint(0, heightScreen)

    coord_list.append([x, y])

clock = pygame.time.Clock()
running = True

# COLORS
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

boton = escribir("Arial", 32, 'Sí bb, mucho', black)
boton_box = pygame.Rect((widthScreen - boton[1]) / 2, (heightScreen - boton[2]) / 2, boton[1], boton[2])
boton_rect = boton[0].get_rect(center=boton_box.center)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION and inicio:
            mouse_pos = pygame.mouse.get_pos()
            if boton_box.collidepoint(mouse_pos):
                boton_box.x = random.randint(0, 800 - boton_box.width)
                boton_box.y = random.randint(0, 600 - boton_box.height)
                boton_rect.center = boton_box.center
                lvl_amor += 1
                if lvl_amor > 9:
                    boton_box.x = widthScreen / 2 - boton_box.width / 2
                    boton_box.y = heightScreen / 2 + boton_box.height / 2
                    boton_rect.center = boton_box.center
                    inicio = False

        if event.type == pygame.MOUSEBUTTONDOWN and boton_box.collidepoint(pygame.mouse.get_pos()) and not inicio:
            max_amor = True

    screen.fill(white)

    frase = escribir('Arial', 64, 'Buenos días amor <3', black)

    screen.blit(frase[0], (pos_x, (heightScreen - frase[2]) / 2, frase[1], frase[2]))
    pos_x += -direction * speed

    for coord in coord_list:
        pygame.draw.circle(screen, (255, 0, 0), coord, 2)
        coord[1] += 1

        if coord[1] >= heightScreen:
            coord[1] = 0

        if pos_x < -frase[1]:
            screen.fill(white)
            pregunta = escribir("Arial", 32, '¿Me Amas?', black)
            screen.blit(pregunta[0],
                        ((widthScreen - pregunta[1]) / 2, (heightScreen - pregunta[2]) / 9, pregunta[1], pregunta[2]))

            pygame.draw.rect(screen, (0, 255, 0), boton_box)
            pygame.draw.rect(screen, (0, 0, 0), boton_box, width=2)
            screen.blit(boton[0], boton_rect)
        if max_amor:
            respuesta = escribir("Arial", 64, "Yo te amo más bb", black)
            screen.blit(respuesta[0],
                        ((widthScreen - respuesta[1]) / 2, heightScreen - respuesta[2] - 3, respuesta[1], respuesta[2]))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
