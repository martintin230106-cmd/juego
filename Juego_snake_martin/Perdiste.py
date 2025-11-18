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
rojo =(255,0,0)

fuente = pygame.font.SysFont('Comic Sans MS',30)
fuente2 = pygame.font.SysFont('None',60)
salir_texto = fuente.render('SALIR', True, blanco)
Seguir_jugando_texto = fuente.render('SEGUIR? ', True, blanco )
perdiste = fuente2.render('PERDISTE',True,rojo)
estado = True


imagen = pygame.image.load('herido.png').convert()
imagen = pygame.transform.scale(imagen,(500,400))



while estado:
        
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

        pantalla.blit(Seguir_jugando_texto, (ancho/2+10, alto-100))
        pantalla.blit(perdiste, (ancho/3, alto/2))
        pygame.display.update()




   





