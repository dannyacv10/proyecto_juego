import pygame 


def funcion():
	
	pygame.init() #Inicializa todos los modulos en pygame
	ventana=pygame.display.set_mode([700,400])
	pygame.display.set_caption("Blue Ball") #Mensaje en la ventana 
	salir=False  
	reloj=pygame.time.Clock()
	blanco=(255,255,255)
	negro=(200,2,2)
	
	
	while salir !=True: #Ciclo principal
		 
		for event in pygame.event.get(): #Recorre todos los eventos 
			
			if event.type== pygame.QUIT:
				salir=True 
		reloj.tick(15)		#La ventana se actualiza cada 15 fps
		ventana.fill(blanco
		pygame.draw.circle(ventana,negro,(20,20)
	
		
		pygame.display.update()
		
	pygame.quit()	
	
funcion()	
