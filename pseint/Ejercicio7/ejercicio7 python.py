# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# area de descripcion:
	# enunciado: Calcular la media de una serie de numeros positivos, suponiendo que los datos
	# se leen desde un terminal. Un valor de cero como entrada indicara que se ha alcanzado el final de la serie de numeros positivos.
	# desarrolado por: Juan Fernando Parra
	# version:1.0
	# fecha:3/03/2023
	# area de declaracion de variables
	v_valnum = float()
	v_contdor = float()
	v_valsum = float()
	v_valprom = float()
	# area de inicializacion de variables
	v_valnum = 0.0
	v_contdor = 0.0
	v_valsum = 0.0
	v_valprom = 0.0
	# area de lectura
	print(" Escribir serie de numeros, cuando se escriba 0, el promedio se calcula automaticamente")
	# area de procesos 
	while True:# no hay 'repetir' en python
		v_valnum = float(input())
		if v_valnum>0:
			v_valsum = v_valsum+v_valnum
			v_contdor = v_contdor+1
		else:
			v_valprom = v_valsum/v_contdor
		if v_valnum==0: break
	print("la suma de los numeros es de: ",v_valsum)
	print(" La cantida de numeros es: ",v_contdor)
	print("el promedio de los numeros es: ",v_valprom)

