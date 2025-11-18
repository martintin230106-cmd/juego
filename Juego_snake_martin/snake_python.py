#importamos las librerias
import pygame 
import random 
import time 
import menu

# creamos la funcion def main la cual contiene todo nuestro juego en su interior y es la que utilizaremos para poder rejugar
def main():
    menu

    #esta sera la velocidad de nuestra serpiente medida en pixeles/s 
    snake_speed = 13

    #definimos la cantidad de pixeles de ancho y alto de la ventana
    ANCHO = 800
    ALTO = 600

    # Definimos los colores  que vamos a usar 
    ROJO = pygame.Color(255,0,0)
    VERDE = pygame.Color(0,255,0)
    NEGRO =pygame.Color(0,0,0)
    AZUL = pygame.Color(0, 0, 255)
    BLANCO = pygame.Color(255, 255, 255)

    #iniciamos pygame
    pygame.init()
    #nombre de la ventana
    pygame.display.set_caption ('juego snake')

    #creamos la ventana con las dimensiones ANCHO y ALTO
    game_window = pygame.display.set_mode((ANCHO, ALTO))

    fps = pygame.time.Clock()



    # creamos el cuerpo de la serpiente
    cuerpo= [[100, 50],
                [90, 50],
                [80,50],
                [70, 50]]


    #posicion inicial de donde va estar la serpiente
    posicion_serpiente =[100, 50]

    #decimos que las frutas aparescan de forma aleatoria por toda la ventana
    posicion_fruta = [random.randrange(1, (ANCHO//10)) * 10,
                    random.randrange(1, (ALTO//10)) * 10]
    

    #creamos la variable que pregunta si hay alfuna fruta
    aparicion_frutas = True

    #decimos el movimiento inicial de la serpiente
    direccion = 'DERECHA'
    # guatdamos el movimiento inicial en la variable cambio
    cambio = direccion

    #puntuacion inicial
    puntaje= 0

    #creamos la funcion para ver la puntuacion
    def mostrar_puntos( color , fuente, tamano):

        #creamos el tipo de fuente y tamano que va a tener la letra de nuestro puntaje
        fuente_puntaje= pygame.font.SysFont(fuente, tamano)

        #decimos la palabra que queremos que tenga nuestra fuente, ademas de los puntos convertidos a una variable de tipo string
        mostrar_puntaje = fuente_puntaje.render('puntuacion: '+ str(puntaje), True, color)

        # creamos un objeto rectangular para el texto
        puntaje_recto= mostrar_puntaje.get_rect()

        #colocamos nuestro texto de puntaje en una variable rectangular
        game_window.blit(mostrar_puntaje, puntaje_recto)
        

    #creamos la funncion perdiste que usaremos en los casos que queramos que el jugador pierda y deje de jugar
    def perdiste():
        #otra fuente 
        mi_fuente = pygame.font.SysFont('times new roman', 50 )

        #le decimos al final al jugador cuantos puntos hizo
        perdiste_texto = mi_fuente.render('tu puntaje es: '  + str(puntaje),True, ROJO)
        

        #hacemos un rectangulo para la superficie del texto
        perdiste_rectangulo = perdiste_texto.get_rect()

        #colocamos la cordenadas de donde estara nuestro texto
        perdiste_rectangulo.midtop = (ANCHO/2, ALTO/4)


        #con la funcion .blit colocamos nuestro texto en la pantalla dentro del rectangulo
        game_window.blit(perdiste_texto, perdiste_rectangulo  )
        pygame.display.flip()

        #esperamos 2 segundo para que el jugador pueda ver su puntuacion
        time.sleep(2)

        # a partir de aqui creamos la ventana 'Perdiste' que le pregunte al jugador si continuar o salir del juego
        pantalla = pygame.display.set_mode((500, 400))
        pygame.display.set_caption("perdidte")

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
        Seguir_jugando_texto = fuente.render('SEGUIR', True, blanco )
        perdiste = fuente2.render('PERDISTE',True,ROJO)
        estado = True

        #cargamos nuestra imagen y la escalamos a las mismas dimensiones que nuestra ventana
        imagen = pygame.image.load('herido.png').convert()
        imagen = pygame.transform.scale(imagen,(500,400))


        #generamos un bucle while para el evento de los botones
        while estado:
                #si apretamos la x salimos del bucle    
                for evento in pygame.event.get():
                    if evento.type ==pygame.QUIT:
                        estado = False
                    #Usamos la funcion MOUSEBUTTONDOWN para revisar si se a apretado el boton
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        #preguntamos si el boton se a precionado en estas cordenadas
                        #SALIR
                        if ancho/6 <=mouse[0] <=ancho/6+140 and alto-100 <= mouse[1] <= alto-60:
                            pygame.quit()
                        #CONTINUAR
                        if ancho/2 <=mouse[0] <=ancho/2+140 and alto-100 <= mouse[1] <= alto-60:
                            main()
                #guardamos las cordenadas donde esta nuestro mouse en una variable llamada mouse
                mouse = pygame.mouse.get_pos()
                #ponemos de fondo nuestra imagen
                pantalla.blit(imagen, [0, 0])

                #cuando pasamos el cursor por el 'boton' este cambiara de color
                if ancho/6 <=mouse[0] <=ancho/6+140 and alto-100 <= mouse[1] <= alto-60:
                    pygame.draw.rect(pantalla,color_light,[ancho/6,alto-100,140,40] )
                #sino se mantendra en otro color
                else:
                    pygame.draw.rect(pantalla,color_dark,[ancho/6,alto-100,140,40])

                
                #colocamos texto por encima de nuestro boton
                pantalla.blit(salir_texto, (ancho/6+20, alto-100))



                if ancho/2 <=mouse[0] <=ancho/2+140 and alto-100 <= mouse[1] <= alto-60:
                        pygame.draw.rect(pantalla,color_light,[ancho/2,alto-100,140,40] )

                else:
                        pygame.draw.rect(pantalla,color_dark,[ancho/2,alto-100,140,40])

                pantalla.blit(Seguir_jugando_texto, (ancho/2+10, alto-100))
                pantalla.blit(perdiste, (ancho/3, alto/2))
                #refrescamos la ventana
                pygame.display.update()

       
    while True:

        
        #Principales eventos de movimiento
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cambio = 'ARRIBA'
                if event.key == pygame.K_DOWN:
                    cambio = 'ABAJO'
                if event.key == pygame.K_LEFT:
                    cambio = 'IZQUIERDA'
                if event.key == pygame.K_RIGHT:
                    cambio = 'DERECHA'

        #excepciones para que la serpiente no pueda moverse a todas las direcciones
        if cambio == 'ARRIBA' and direccion != 'ABAJO':
            direccion = 'ARRIBA'
        if cambio == 'ABAJO' and direccion != 'ARRIBA':
            direccion = 'ABAJO'
        if cambio == 'IZQUIERDA' and direccion != 'DERECHA':
            direccion ='IZQUIERDA'
        if cambio == 'DERECHA' and direccion != 'IZQUIERDA':
            direccion = 'DERECHA'

        #principales movimientos
        if direccion == 'ARRIBA':
            posicion_serpiente[1] -= 10
        if direccion == 'ABAJO':
            posicion_serpiente[1] += 10
        if direccion == "IZQUIERDA":
            posicion_serpiente[0] -=10
            posicion_serpiente[0] = posicion_serpiente[0]% ANCHO
        if direccion =="DERECHA":
            posicion_serpiente[0] +=10
            posicion_serpiente[0] = posicion_serpiente[0]% ANCHO

        


        #usamos esta funcion para que las tuplas de la serpiente se mantengan unidas ademas de agregarle una mas
        cuerpo.insert(0, list(posicion_serpiente))
        #si la posicion de la cabeza de la serpiente es igual a la fruta el puntaje aumentara 10 y la fruta desaparecera
        if posicion_serpiente[0] == posicion_fruta[0] and posicion_serpiente[1] ==posicion_fruta[1]:
            puntaje += 10
            aparicion_frutas = False
            
        else:
            cuerpo.pop()
        #si no hay frutas agrega 1 en un punto random de la ventana
        if not aparicion_frutas:
            posicion_fruta = [random.randrange(1, (ANCHO//10)) *10, 
                            random.randrange(1, (ALTO//10))* 10]

        aparicion_frutas = True
        game_window.fill(NEGRO)
        #dimensionamos el cuerpo de nuestra serpiente y le definimso un color 
        for pos in  cuerpo:
            pygame.draw.rect(game_window, VERDE,
                            pygame.Rect(pos[0], pos[1],10,10))
        #lo mismo hacemos con las frutas
        pygame.draw.rect(game_window, ROJO, pygame.Rect(
            posicion_fruta[0], posicion_fruta[1], 10, 10))
        
        # si la serpiente supera las dimensones de la ventana se ejeuta la funncion perdiste
        if posicion_serpiente[0] < 0 or posicion_serpiente[0] > ANCHO-10:
            perdiste()
        if posicion_serpiente[1] < 0 or posicion_serpiente[1] > ALTO-10:
            perdiste()

        # si la serpiente se toca a si misma tambien se ejecuta la funcion perdiste
        for bloque in cuerpo[1:]:
            if posicion_serpiente[0] == bloque[0] and posicion_serpiente[1] ==bloque[1]:
                perdiste()

        mostrar_puntos( BLANCO, 'times new roman', 20)


        pygame.display.update()

        fps.tick(snake_speed)
main()           
