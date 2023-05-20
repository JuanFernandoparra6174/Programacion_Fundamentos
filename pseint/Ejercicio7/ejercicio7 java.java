/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO7.java."

import java.io.*;

public class ejercicio7 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double v_contdor;
		double v_valnum;
		double v_valprom;
		double v_valsum;
		// area de descripcion:
		// enunciado: Calcular la media de una serie de numeros positivos, suponiendo que los datos
		// se leen desde un terminal. Un valor de cero como entrada indicara que se ha alcanzado el final de la serie de numeros positivos.
		// desarrolado por: Juan Fernando Parra
		// version:1.0
		// fecha:3/03/2023
		// area de declaracion de variables
		// area de inicializacion de variables
		v_valnum = 0.0;
		v_contdor = 0.0;
		v_valsum = 0.0;
		v_valprom = 0.0;
		// area de lectura
		System.out.println(" Escribir serie de numeros, cuando se escriba 0, el promedio se calcula automaticamente");
		// area de procesos 
		do {
			v_valnum = Double.parseDouble(bufEntrada.readLine());
			if (v_valnum>0) {
				v_valsum = v_valsum+v_valnum;
				v_contdor = v_contdor+1;
			} else {
				v_valprom = v_valsum/v_contdor;
			}
		} while (v_valnum!=0);
		System.out.println("la suma de los numeros es de: "+v_valsum);
		System.out.println(" La cantida de numeros es: "+v_contdor);
		System.out.println("el promedio de los numeros es: "+v_valprom);
	}


}

