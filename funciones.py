
import pprint


prg ="""
avanzar
avanzar
avanzar
avanzar
avanzar
avanzar
avanzar

"""


##Espacio

esp = []
for i in range(12):
	esp.append([0]*24)


#Barreras

#Barrera1

esp[2][5]=9
esp[3][5]=9	
esp[4][5]=9
esp[5][5]=9
esp[6][5]=9
esp[7][5]=9
esp[8][5]=9
esp[9][5]=9	

#Barrera2
esp[4][9]=9
esp[5][9]=9	
esp[6][9]=9
esp[7][9]=9
esp[8][9]=9
esp[9][9]=9
esp[10][9]=9
esp[11][9]=9	

##Barrera3
esp[0][13]=9
esp[1][13]=9	
esp[2][13]=9
esp[3][13]=9
esp[7][13]=9
esp[8][13]=9
esp[9][13]=9
esp[10][13]=9	

#Barrera4
esp[0][16]=9
esp[1][16]=9	
esp[2][16]=9
esp[3][16]=9
esp[4][16]=9
esp[5][16]=9
esp[6][16]=9
esp[7][16]=9	

#Barrera5
esp[4][21]=9
esp[5][21]=9	
esp[6][21]=9
esp[7][21]=9
esp[8][21]=9
esp[9][21]=9
esp[10][21]=9
esp[11][21]=9	

#meta
esp[6][23]=88

pp = pprint.PrettyPrinter()
pp.pprint(esp)


## Fin espacio
##Funcion espacio y programa

def jugar (esp,programa):
	print("la bola mira de frente")
	pos=input("posicion en que comienza la bola debe ser entre (0,0) hasta (12,0):" )
	pos=(pos)
	print("comienza en la posicion",pos)	
	
	lineas= programa.split("\n")
	for cmd in lineas:
		print(cmd)
		if cmd == "avanzar":
			if esp[pos[0]][pos[1]]==0: #no hay barrera
				r=input("cuantas veces repetir accion:")
				print(r)
				if r==1:
					pos=((pos)[0],(pos)[1]+1)
				if esp[pos[0]][pos[1]]==0 and r==2:
					pos=((pos)[0],(pos)[1]+1*r-1)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==2:	
					pos=((pos)[0],(pos)[1]+1*r-1)
			else:
				if esp[pos[0]][pos[1]]==9:
						print("hay barrera NO se puede avanzar, cambia el comando!")	    			
			print("nueva posicion bola",pos)
							
		if cmd=="retroceder":
			if esp[pos[0]][pos[1]]==0: #no hay barrera
				pos=((pos)[0],(pos)[1]-1)
			else:
				if esp[pos[0]][pos[1]]==9:
					print("hay barrera NO se puede retroceder, cambia el comando!")		
			print("nueva posicion bola",pos)
			
		if cmd=="subir":
			if esp[pos[0]][pos[1]]==0: #no hay barrera
				pos=((pos)[0]-1,(pos)[1])
			else:
				if esp[pos[0]][pos[1]]==9:
					print("hay barrera NO se puede subir, cambia el comando!")	
			print("nueva pos",pos)
			
		if cmd=="bajar":
			if esp[pos[0]][pos[1]]==0: #no hay barrera
				pos=((pos)[0]+1,(pos)[1])
			else:
				if esp[pos[0]][pos[1]]==9:
					print("hay barrera NO se puede bajar, cambia el comando!")	
			print("nueva posicion bola",pos)	
			
		if 	esp[pos[0]][pos[1]]==88:
			print("ganaste")
			
jugar(esp,prg)



