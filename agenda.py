import json
print("AGENDA TELEFONICA")

#////****Se crea agenda de prueba\\\\\*****

#agendaprueba={"debi":"786","gon":"897","panchi":"675","nachi":"900"}
#agendaprueba={}


#////****Se pide por pantalla opcion para menu, con '5' se sale \\\\\*****

def leerarchivo():
	
	archivo=open("archivo.txt","r")#abro archivo.txt, "r" para leer y lo guardo en la variable archivo
	linea=archivo.readlines()#guardo en variable linea lo que leede archivo
	#print(linea)
	
	#print(type(cadena))
	nuevodicc=linea[0].replace("\'","\"")
	#print(nuevodicc)

	conversion=json.loads(nuevodicc)
	archivo.close()

	#print (conversion)
	#print(type(conversion))
	return conversion


def escribirarchivo(agendamodificada): 
	with open('archivo.txt', 'w') as archivo:
	    archivo.write(str(agendamodificada))
	    archivo.close()



#print (leerarchivo())
menu=input("INTRODUCE NUMERO OPCION: \n1-ver agenda,\n2-modificar agenda,\n3-añadir contacto,\n4-buscador,\n5-SALIR \nOPCION: ")
while menu!=str(5):

	#////****Opcion ver agenda, si no existen datos, muestra agenda vaia, sino, te muestra la agenda entera\\\\\*****

	if menu==str(1):
		len(leerarchivo())
		if len(leerarchivo())==0:
			print("Agenda vacía")

		else:

			print(leerarchivo()) 

	#///***OPCION CREAR AGENDA, NOMBRE Y TELEFONO***\\\
	#menu=input("introduce nueva opcion: ")	
	if menu==str(3):
		print("PARA SALIR ESCRIBE S")
		nombre=(input("INTRODUCE NOMBRE: ")).lower()

		while (nombre !="s"):
		
			telefono=str(input("INTRODUCE TELEFONO: "))
			agendamodificada=leerarchivo()
			agendamodificada[nombre]=telefono
			escribirarchivo(agendamodificada)

		
			
			#mi_agenda={nombre:telefono}

			nombre=(input("INTRODUCE NOMBRE: ")).lower()
	#///***OPCION MODIFICAR AGENDA***\\\

	if menu==str(2):
			#///***RECORRE LA AGENDA PARA SABER SI TIENE DATOS, SI NO TIENE CONTACTOS DEVUELE Q ESTÁ VACÍA***\\\		 
			len(leerarchivo())
			if len(leerarchivo())==0:
				print("Agenda vacía")

			else:
				print(leerarchivo())
				print("PARA SALIR PULSE S")
				cambio=(input("INTRODUCE CONTACTO A MODIFICAR O BORRAR: ")).lower()

				while cambio!= "s":


					print(cambio in leerarchivo())

					if (cambio in leerarchivo())==False:
						print("no existe")
					else:
						eleccion=(input("QUE QUIERES MODIFICAR: \n1-NOMBRE,\n2-TELEFONO,\n3-BORRAR,\nOPCION: "))
						if eleccion==str(1):
							nuevo_nombre=(input("INTRODUCE NUEVO NOMBRE: ")).lower()
							agendamodificada=leerarchivo()
							agendamodificada[nuevo_nombre]=agendamodificada.pop(cambio)
							escribirarchivo(agendamodificada)
											
							
						if eleccion==str(2):
							nuevo_telefono=(input("INTRODUCE NUEVO TELEFONO: "))
							agendamodificada=leerarchivo()
							agendamodificada[cambio]=nuevo_telefono
							escribirarchivo(agendamodificada)
							#leerarchivo()[cambio]=nuevo_telefono
						if eleccion==str(3):
							agendamodificada=leerarchivo()
							del(agendamodificada[cambio])
							escribirarchivo(agendamodificada)
							print("SE HA BORRADO EL CONTACTO",cambio)
					print(leerarchivo())

					cambio=(input("INTRODUCE NOMBRE A MODIFICAR O BORRAR: ")).lower()	
	if menu==str(4):
		#busca un contacto o telefono de mi agenda
		len(leerarchivo())
		if len(leerarchivo())==0:
			print("Agenda vacía")
		else:
			print("PARA SALIR PULSE S")
			dato_buscado=(input("INTRODUCE DATO A BUSCAR: ")).lower()
			if dato_buscado=="s":
				menu=input("INTRODUCE NUMERO OPCION: \n1-ver agenda,\n2-modificar agenda,\n3-crear agenda,\n4-buscador,\n5-SALIR \nOPCION: ")
			if (dato_buscado in leerarchivo())==False:
				print("ESE CONTACTO NO EXISTE")
			else:
				print("CONTACTO: ",dato_buscado ,"--> ",leerarchivo().get(dato_buscado))




					



	menu=input("INTRODUCE NUMERO OPCION: \n1-ver agenda,\n2-modificar agenda,\n3-crear agenda,\n4-buscador,\n5-SALIR \nOPCION: ")
	






print("fin")


