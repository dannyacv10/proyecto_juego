import pprint

comandospro1= """
avanzar
retroceder
subir
bajar
"""


##Espacio


esp= []
for i in range(12):
	esp.append([0]*24)
	
esp[6][22]=99	

pp = pprint.PrettyPrinter()
pp.pprint(esp)

## Fin espacio
##Funcion espacio y programa

def jugar (esp,pro):
	#0: avanzar 
	#1: retroceder 
	#2: subir 
	#3: bajar
	dire=raw_input("indique la direccion de la bola entre 0 hasta 3: ")
	print dire  
	
	dire=(dire)
	
	pos=raw_input("indique la posicion de la bola entre (0,0) hasta (12,0): ")
	print pos  
	
	pos=(pos)
	
	l= pro.split("/n")
	print(l)
	for comando in l:
		print(comando)
		if comando == "avanzar":
			if dire==0:
				pos=((pos)[0]+1,(pos)[1])
			


jugar(esp,comandospro1)


