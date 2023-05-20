/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO9.java."

import java.io.*;

public class ejercicio9 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_horsemtra;
		int v_hortraext;
		int v_hortrasinext;
		String v_nomemp;
		double v_valhor;
		double v_valhorext;
		double v_valhorsinext;
		double v_valsal;
		// descripcion: 
		// enunciado: Programa que calcula el salario de los empleados
		// desarrollado por: Juan Fernando Parra
		// version:1,0
		// fecha:/5/2023
		// area de declaracion de variables
		// area de inicializacion de variables
		v_nomemp = "";
		v_horsemtra = 0;
		v_valhor = 0.0;
		v_hortraext = 0;
		v_hortrasinext = 0;
		v_valhorsinext = 0.0;
		v_valhorext = 0.0;
		v_valsal = 0.0;
		// area de lectura
		System.out.println("Nombre del empleado");
		v_nomemp = bufEntrada.readLine();
		System.out.println("Escriba las horas trabajadas semanalmente");
		v_horsemtra = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Valor de la hora del trabajador");
		v_valhor = Double.parseDouble(bufEntrada.readLine());
		// area de procesos
		if (v_horsemtra>40) {
			v_hortraext = v_horsemtra-40;
			v_valhorext = (v_valhor+(v_valhor*1.5))*v_hortraext;
			v_hortrasinext = v_horsemtra-v_hortraext;
			v_valhorsinext = v_valhor*v_hortrasinext;
			v_valsal = (v_valhorsinext+v_valhorext)*4;
			System.out.println("El nombre del empleado es "+v_nomemp);
			System.out.println("El numero de horas extras es de: "+v_hortraext);
			System.out.println(" El salario del empleado es de: "+v_valsal);
		} else {
			v_valsal = v_horsemtra*v_valhor*4;
			System.out.println("El nombre del empleado es"+v_nomemp);
			System.out.println(" El salario del empleado es de: "+v_valsal);
		}
	}


}

