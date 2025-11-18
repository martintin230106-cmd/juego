import pygame


pygame.init()

#definimos las dimensiones de las pantallas
pantalla = pygame.display.set_mode((500, 400))
pygame.display.set_caption("menu")


ancho = pantalla.get_width()
alto = pantalla.get_height()

# colores de los botones
color_light = (227, 62, 30)
color_dark = (156, 50, 30)
blanco =(255,255,255)



fuente = pygame.font.SysFont('Comic Sans MS',30)
salir_texto = fuente.render('SALIR', True, blanco)
jugar_texto = fuente.render('JUGAR', True, blanco )
estado = True

while estado:
    imagen = pygame.image.load('pixil-frame-0.png').convert()
    imagen = pygame.transform.scale(imagen,(500,400))

    for evento in pygame.event.get():
        if evento.type ==pygame.QUIT:
            estado = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if ancho/6 <=mouse[0] <=ancho/6+140 and alto-100 <= mouse[1] <= alto-60:
                pygame.quit()
            if ancho/2 <=mouse[0] <=ancho/2+140 and alto-100 <= mouse[1] <= alto-60:
                estado = False

    mouse = pygame.mouse.get_pos()
    pantalla.blit(imagen, [0, 0])

    if ancho/6 <=mouse[0] <=ancho/6+140 and alto-100 <= mouse[1] <= alto-60:
        pygame.draw.rect(pantalla,color_light,[ancho/6,alto-100,140,40] )

    else:
        pygame.draw.rect(pantalla,color_dark,[ancho/6,alto-100,140,40])

    pantalla.blit(salir_texto, (ancho/6+20, alto-100))

    if ancho/2 <=mouse[0] <=ancho/2+140 and alto-100 <= mouse[1] <= alto-60:
        pygame.draw.rect(pantalla,color_light,[ancho/2,alto-100,140,40] )

    else:
        pygame.draw.rect(pantalla,color_dark,[ancho/2,alto-100,140,40])

    pantalla.blit(jugar_texto, (ancho/2+20, alto-100))
    pygame.display.update()







