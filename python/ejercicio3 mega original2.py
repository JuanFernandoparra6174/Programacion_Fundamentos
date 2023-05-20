# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Programa: Fundamentos de programacion
	# Nombre del archivo: ejercicio 3
	# Descripcion : Programa que captura la aceleracion
	# Autor: Juan Fernando Parra Rincon
	# Fecha: 2/22/2023
	# Version: 1.0
	# Una locomotora necesita 10 s. para alcanzar su velocidad normal que es 25m/s.
	# Suponiendo que su movimiento es uniformemente acelerado, Que aceleracion se le ha comunicado y que espacio ha recorrido antes de alcanzar la velocidad regular?//
	velocidad_final = float()
	velocidad_inicial = float()
	tiempo = float()
	aceleracion = float()
	recorrido = float()
	velocidad_inicial = 0
	velocidad_final = 25
	tiempo = 10
	aceleracion = (velocidad_final-velocidad_inicial)/tiempo
	recorrido = (velocidad_inicial*tiempo)+(1/2*aceleracion)*(100)
	print("resultado aceleracion: ",aceleracion)
	print("resultado recorrido: ",recorrido)

