
import pprint


prg ="""
avanzar
avanzar
bajar
avanzar
subir
"""


##Espacio

esp = []
for i in range(12):
	esp.append([0]*18)


#Barreras

#Barrera1

esp[4][5]=1
esp[5][5]=1	
esp[6][5]=1
esp[7][5]=1
esp[8][5]=1
esp[9][5]=1
esp[10][5]=1
esp[11][5]=1	

#Barrera2
esp[0][10]=1
esp[1][10]=1	
esp[2][10]=1
esp[3][10]=1
esp[4][10]=1
esp[5][10]=1
esp[6][10]=1
esp[7][10]=1	

##Barrera3
esp[0][15]=1
esp[1][15]=1	
esp[2][15]=1
esp[3][15]=1
esp[7][15]=1
esp[8][15]=1
esp[9][15]=1
esp[10][15]=1	



#meta
esp[6][17]="meta"
esp[5][17]="meta"

pp = pprint.PrettyPrinter()
pp.pprint(esp)


## Fin espacio
##Funcion espacio y programa

#archivo = open("ejemplo.py", "rb") 
#prg = archivo.readlines()
#print (prg)
cad="" 
with open('ejemplo.blue') as archivo:
    for prg in archivo:
		print (prg)
		cad=cad+prg

def jugar (esp,programa):
	print("la bola mira de frente")
	pos=input("posicion en que comienza la bola debe ser entre (0,0) hasta (11,0):" )
	pos=(pos)
	print("comienza en la posicion",pos)	
	
	lineas= programa.split("\n")
	for cmd in lineas:
		print(cmd)
		if cmd == "avanzar":
			if esp[pos[0]][pos[1]]==0: #no hay barrera
				r=input("cuantas veces repetir accion, se puede repetir maximo 5 veces :")
				print(r)
				if r==1:
					pos=((pos)[0],(pos)[1]+1)
				if esp[pos[0]][pos[1]]==0 and r==2:
					pos=((pos)[0],(pos)[1]+1*r-1)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==2:	
					pos=((pos)[0],(pos)[1]+1*r-1)
				if esp[pos[0]][pos[1]]==0 and r==3:
					pos=((pos)[0],(pos)[1]+1*r-2)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==3:
					pos=((pos)[0],(pos)[1]+1*r-2)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==3:
					pos=((pos)[0],(pos)[1]+1*r-2)
				if esp[pos[0]][pos[1]]==0 and r==4:
					pos=((pos)[0],(pos)[1]+1*r-3)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==4:
					pos=((pos)[0],(pos)[1]+1*r-3)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==4:
					pos=((pos)[0],(pos)[1]+1*r-3)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==4:
					pos=((pos)[0],(pos)[1]+1*r-3)
				if esp[pos[0]][pos[1]]==0 and r==5:
					pos=((pos)[0],(pos)[1]+1*r-4)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==5:
					pos=((pos)[0],(pos)[1]+1*r-4)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==5:
					pos=((pos)[0],(pos)[1]+1*r-4)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==5:
					pos=((pos)[0],(pos)[1]+1*r-4)
					print("nueva posicion bola",pos)
				if esp[pos[0]][pos[1]]==0 and r==5:
					pos=((pos)[0],(pos)[1]+1*r-4)
					print("nueva posicion bola",pos)	
				if esp[pos[0]][pos[1]]==1:
					print("hay barrera NO se puede avanzar, cambia el comando!")				    			
				print("nueva posicion bola",pos)
			else:
				print("hay barrera NO se puede avanzar, cambia el comando!")
			
			
							
		if cmd=="subir":
			if esp[pos[0]][pos[1]]==0: #No hay barrera
				r=input("cuantas veces repetir accion, se puede repetir maximo 5 veces:")
				print(r)
			if r==1:	 
				pos=((pos)[0]-1,(pos)[1])
			if esp[pos[0]][pos[1]]==0 and r==2:
				pos=((pos)[0]-1*r+1,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==2:	
				pos=((pos)[0]-1*r+1,(pos)[1])
			if esp[pos[0]][pos[1]]==0 and r==3:
				pos=((pos)[0]-1*r+2,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==3:
				pos=((pos)[0]-1*r+2,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==3:
				pos=((pos)[0]-1*r+2,(pos)[1])
			if esp[pos[0]][pos[1]]==0 and r==4:
				pos=((pos)[0]-1*r+3,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==4:
				pos=((pos)[0]-1*r+3,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==4:
				pos=((pos)[0]-1*r+3,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==4:
				pos=((pos)[0]-1*r+3,(pos)[1])
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]-1*r+4,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]-1*r+4,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]-1*r+4,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]-1*r+4,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]-1*r+4,(pos)[1])
			elif esp[pos[0]][pos[1]]==1:
					print("hay barrera NO se puede avanzar, cambia el comando!")		    			
				
			
		if cmd=="bajar":
			if esp[pos[0]][pos[1]]==0: #No hay barrera
				r=input("cuantas veces repetir accion, se puede repetir maximo 5 veces:")
				print(r)
			if r==1:	 
				pos=((pos)[0]+1,(pos)[1])
			if esp[pos[0]][pos[1]]==0 and r==2:
				pos=((pos)[0]+1*r-1,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==2:	
				pos=((pos)[0]+1*r-1,(pos)[1])
			if esp[pos[0]][pos[1]]==0 and r==3:
				pos=((pos)[0]+1*r-2,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==3:
				pos=((pos)[0]+1*r-2,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==3:
				pos=((pos)[0]+1*r-2,(pos)[1])
			if esp[pos[0]][pos[1]]==0 and r==4:
				pos=((pos)[0]+1*r-3,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==4:
				pos=((pos)[0]+1*r-3,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==4:
				pos=((pos)[0]+1*r-3,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==4:
				pos=((pos)[0]+1*r-3,(pos)[1])
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]+1*r-4,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]+1*r-4,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]+1*r-4,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]+1*r-4,(pos)[1])
				print("nueva posicion bola",pos)
			if esp[pos[0]][pos[1]]==0 and r==5:
				pos=((pos)[0]+1*r-4,(pos)[1])
			else:
				print("hay barrera NO se puede avanzar, cambia el comando!")		    			
			
		if 	esp[pos[0]][pos[1]]=="meta":
			print("Felicitaciones Ganaste")
			
jugar(esp,cad)



