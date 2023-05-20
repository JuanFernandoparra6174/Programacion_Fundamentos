# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# area de descripcion
	# enunciado://Una locomotora necesita 10 s. para alcanzar su velocidad normal que es 25m/s.
	# Suponiendo que su movimiento es uniformemente acelerado, Que aceleracion se le ha comunicado y que espacio 
	# ha recorrido antes de alcanzar la velocidad regular?//
	# desarrollado por: Juan Fernando Parra
	# version: 1.0
	# fecha: 2/22/2023
	# area de delcaracion de variables
	v_valvelini = int()
	v_valvelfin = int()
	v_valtiem = int()
	v_valacel = float()
	v_valrec = int()
	# area de inicializacion de variables
	v_valvelini = 0
	v_valvelfin = 0
	v_valtiem = 0
	v_valacel = 0.0
	v_valrec = 0
	# area de lectura
	print("escribir la velocidad inicial")
	v_valvelini = int(input())
	print("escribir la velocidad final")
	v_valvelfin = int(input())
	print("escribir el tiempo transcurrido entre el cambio de velocidad inicial y velocidad final")
	v_valtiem = int(input())
	# area de procesos
	v_valacel = (v_valvelfin-v_valvelini)/(v_valtiem)
	print("La aceleracion en m/s^2 fue de : ",v_valacel)
	v_valrec = (v_valvelini*v_valtiem)+((1/2*v_valacel)*(v_valtiem**2))
	print("El recorrorrido en metros antes de alcanzar la velocidad regular fue de: ",v_valrec)

