import pprint

prg =""" 
avanzar
retroceder
subir
avanzar
avanzar
avanzar
bajar
subir
avanzar
subir
retroceder
"""

##Espacio

esp = []
for i in range(12):
	esp.append([0]*24)
	
esp[6][22]=99	

pp = pprint.PrettyPrinter()
pp.pprint(esp)

## Fin espacio
##Funcion espacio y programa

def jugar (esp,programa):
	dire=0 #mirando de frente
	print("comienza en la direccion",dire)
	pos=input("posicion en que comienza la bola debe ser entre (0,0) hasta (12,0):" )
	pos=(pos)

	print("comienza en la posicion",pos)
	
	lineas= programa.split("\n")
	for cmd in lineas:
		print(cmd)
		if cmd == "avanzar":
			if dire==0: #Mirando de frente 
				pos=((pos)[0],(pos)[1]+1)
			print("nueva posicion bola",pos)
			
		if cmd=="retroceder":
			if dire==0: #Mirando de frente
				pos=((pos)[0],(pos)[1]-1)
			print("nueva posicion bola",pos)
			
		if cmd=="subir":
			if dire==0: 
				pos=((pos)[0]-1,(pos)[1])
			print("nueva pos",pos)
			
		if cmd=="bajar":
			if dire==0:
				pos=((pos)[0]+1,(pos)[1])
			print("nueva posicion bola",pos)	
		

jugar(esp,prg)
pp.pprint(esp)

