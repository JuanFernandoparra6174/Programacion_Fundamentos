/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "SIN_TITULO.java."

import java.io.*;

public class sin_titulo {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_i;
		int v_numfin;
		int v_numini;
		int v_valsum;
		// area de descripcion
		// enunciado:Programa que calcula la suma de los numero pares comprendidos entre 2 y 100
		// desarrollado por: Juan Fernando Parra
		// version: 1.0
		// fecha: 2/24/2023
		// area de declaracion de variables
		// area de inicializacion de variables
		v_numini = 0;
		v_numfin = 0;
		v_i = 0;
		v_valsum = 0;
		// Area de lectura
		System.out.println(" Escribir desde que numero se iniciara la suma");
		v_numini = Integer.parseInt(bufEntrada.readLine());
		System.out.println(" Escrbir hasta que numero se sumara");
		v_numfin = Integer.parseInt(bufEntrada.readLine());
		// area procesos
		for (v_i=v_numini;v_i<=v_numfin;v_i+=2) {
			v_valsum = v_valsum+v_i;
		}
		System.out.println("La suma total de los numeros es: "+v_valsum);
	}


}

