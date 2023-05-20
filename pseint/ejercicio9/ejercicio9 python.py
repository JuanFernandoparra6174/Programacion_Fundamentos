# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# descripcion: 
	# enunciado: Programa que calcula el salario de los empleados
	# desarrollado por: Juan Fernando Parra
	# version:1,0
	# fecha:/5/2023
	# area de declaracion de variables
	v_nomemp = str()
	v_horsemtra = int()
	v_valhor = float()
	v_hortraext = int()
	v_hortrasinext = int()
	v_valhorsinext = float()
	v_valhorext = float()
	v_valsal = float()
	# area de inicializacion de variables
	v_nomemp = ""
	v_horsemtra = 0
	v_valhor = 0.0
	v_hortraext = 0
	v_hortrasinext = 0
	v_valhorsinext = 0.0
	v_valhorext = 0.0
	v_valsal = 0.0
	# area de lectura
	print("Nombre del empleado")
	v_nomemp = input()
	print("Escriba las horas trabajadas semanalmente")
	v_horsemtra = int(input())
	print("Valor de la hora del trabajador")
	v_valhor = float(input())
	# area de procesos
	if v_horsemtra>40:
		v_hortraext = v_horsemtra-40
		v_valhorext = (v_valhor+(v_valhor*1.5))*v_hortraext
		v_hortrasinext = v_horsemtra-v_hortraext
		v_valhorsinext = v_valhor*v_hortrasinext
		v_valsal = (v_valhorsinext+v_valhorext)*4
		print("El nombre del empleado es ",v_nomemp)
		print("El numero de horas extras es de: ",v_hortraext)
		print(" El salario del empleado es de: ",v_valsal)
	else:
		v_valsal = v_horsemtra*v_valhor*4
		print("El nombre del empleado es",v_nomemp)
		print(" El salario del empleado es de: ",v_valsal)

