# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# area de descripcion
	# enunciado:Programa que calcula la suma de los numero pares comprendidos entre 2 y 100
	# desarrollado por: Juan Fernando Parra
	# version: 1.0
	# fecha: 2/24/2023
	# area de declaracion de variables
	v_numini = int()
	v_numfin = int()
	v_i = int()
	v_valsum = int()
	# area de inicializacion de variables
	v_numini = 0
	v_numfin = 0
	v_i = 0
	v_valsum = 0
	# Area de lectura
	print(" Escribir desde que numero se iniciara la suma")
	v_numini = int(input())
	print(" Escrbir hasta que numero se sumara")
	v_numfin = int(input())
	# area procesos
	for v_i in range(v_numini,v_numfin+1,2):
		v_valsum = v_valsum+v_i
	print("La suma total de los numeros es: ",v_valsum)

