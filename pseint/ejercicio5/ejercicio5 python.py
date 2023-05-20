# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# area de descripcion:
	# enunciado : Calcular el salarario de un empleado en base a las horas trabajadas semanalmente, tarifa, horas extras e impustos aplicados
	# desarrollado por: Juan Fernando Parra
	# version:1.0
	# fecha:3/3/2023
	# area de declararacion de variables
	v_nomemp = str()
	v_hortrasem = int()
	v_valhoremp = int()
	v_numhordiur = int()
	v_valhordiur = int()
	v_numhornoct = int()
	v_valhornoct = int()
	v_valpagimp = float()
	v_valsalbrut = float()
	v_valsalnet = float()
	# area de inicializacion de variables
	v_nomemp = ""
	v_hortrasem = 0
	v_valhoremp = 0
	v_numhordiur = 0
	v_valhordiur = 0
	v_numhornoct = 0
	v_valhornoct = 0
	v_valpagimp = 0.0
	v_valsalbrut = 0.0
	v_valsalnet = 0.0
	# area de lectura
	print("Nombre del trabajador")
	v_nomemp = input()
	print("Horas trabajadas diurnas")
	v_numhordiur = int(input())
	print("Horas trabajadas nocturnas")
	v_numhornoct = int(input())
	print("Valor de la hora del trabajador")
	v_valhoremp = int(input())
	# area de procesos
	v_hortrasem = v_numhordiur+v_numhornoct
	v_valhordiur = v_numhordiur*v_valhoremp
	v_valhornoct = v_numhornoct*((v_valhoremp*0.40)+v_valhoremp)
	v_valsalbrut = v_valhordiur+v_valhornoct
	v_valpagimp = v_valsalbrut*0.19
	v_valsalnet = v_valsalbrut-v_valpagimp
	print("Nombre del trabajador ",v_nomemp)
	print("Horas trabajadas semanalmente ",v_hortrasem)
	print("Salario sin aplicacion de impuestos: ",v_valsalbrut)
	print("Valor total de los impuestos ",v_valpagimp)
	print(" Salario neto del trabajador ",v_valsalnet)

