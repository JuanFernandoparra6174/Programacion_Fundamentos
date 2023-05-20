# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# area de descripcion
	# enunciado: Un cuerpo posee una velocidad inicial de 12 m/s y una aceleracion de 2 m/s2 
	# Cuanto tiempo tardara en adquirir una velocidad de 144 Km/h
	# desarrollado por: Juan Fernando Parra
	# version: 1.0
	# fecha: 2/22/2023
	# area de delcaracion de variables
	v_valvelini = int()
	v_valvelfin = int()
	v_valvelfinmet = int()
	v_valacel = int()
	v_valtiem = int()
	# area de inicializacion de variables
	v_valvelini = 0
	v_valvelfin = 0
	v_valvelfinmet = 0
	v_valacel = 0
	v_valtiem = 0
	# area de lectura
	print("escribir la velocidad inicial")
	v_valvelini = int(input())
	print("escribir la velocidad final")
	v_valvelfin = int(input())
	print("escribir la aceleracion")
	v_valacel = int(input())
	# area de procesos
	v_valvelfinmet = (v_valvelfin*1000)/(3600)
	v_valtiem = (v_valvelfinmet-v_valvelini)/(v_valacel)
	print("el tiempo en segundos que tardara en alcanzar la velocidad final es de  : ",v_valtiem)

