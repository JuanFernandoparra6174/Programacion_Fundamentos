/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_4.java."

import java.io.*;

public class ejercicio_4 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_valacel;
		int v_valtiem;
		int v_valvelfin;
		int v_valvelfinmet;
		int v_valvelini;
		// area de descripcion
		// enunciado: Un cuerpo posee una velocidad inicial de 12 m/s y una aceleracion de 2 m/s2 
		// Cuanto tiempo tardara en adquirir una velocidad de 144 Km/h
		// desarrollado por: Juan Fernando Parra
		// version: 1.0
		// fecha: 2/22/2023
		// area de delcaracion de variables
		// area de inicializacion de variables
		v_valvelini = 0;
		v_valvelfin = 0;
		v_valvelfinmet = 0;
		v_valacel = 0;
		v_valtiem = 0;
		// area de lectura
		System.out.println("escribir la velocidad inicial");
		v_valvelini = Integer.parseInt(bufEntrada.readLine());
		System.out.println("escribir la velocidad final");
		v_valvelfin = Integer.parseInt(bufEntrada.readLine());
		System.out.println("escribir la aceleracion");
		v_valacel = Integer.parseInt(bufEntrada.readLine());
		// area de procesos
		v_valvelfinmet = (v_valvelfin*1000)/(3600);
		v_valtiem = (v_valvelfinmet-v_valvelini)/(v_valacel);
		System.out.println("el tiempo en segundos que tardara en alcanzar la velocidad final es de  : "+v_valtiem);
	}


}

