# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Programa: Fundamentos de programacion
	# Nombre del archivo: ejercicio 2
	# Descripcion : Programa que captura la aceleracion
	# Autor: Juan Fernando Parra Rincon
	# Fecha: 2/22/2023
	# Version: 1.0
	# Un formula 1 que parte del reposo alcanza una velocidad de 216 km/h en 10 s. Calcula su aceleracion.
	velocidad_inicial = float()
	velocidad_final = float()
	tiempo = float()
	aceleracion = float()
	conversor = float()
	# m/s
	velocidad_inicial = 0
	# k/h
	velocidad_final = 216
	# seg
	tiempo = 10
	conversor = (velocidad_final*1000)/3600
	aceleracion = (conversor-velocidad_inicial)/tiempo
	print("la aceleracion ",aceleracion)

