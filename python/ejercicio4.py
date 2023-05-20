# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Programa: Fundamentos de programacion
	# Nombre del archivo: ejercicio 4
	# Descripcion : Programa que captura el tiempo tardado para obtener la velocidad final
	# Autor: Juan Fernando Parra Rincon
	# Fecha: 2/22/2023
	# Version: 1.0
	# Un cuerpo posee una velocidad inicial de 12 m/s y una aceleracion de 2 m/s2 Cuanto tiempo tardara en adquirir una velocidad de 144 Km/h?
	velocidad_inicial = float()
	velocidad_final = float()
	aceleracion = float()
	conversor = float()
	tiempo = float()
	# m/s
	velocidad_inicial = 12
	# k/h
	velocidad_final = 144
	# m/s
	aceleracion = 2
	conversor = (velocidad_final*1000)/3600
	tiempo = (conversor-velocidad_inicial)/aceleracion
	print("tiempo tardado ",tiempo)

