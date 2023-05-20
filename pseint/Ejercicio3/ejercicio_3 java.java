/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_3.java."

import java.io.*;
import java.math.*;

public class ejercicio_3 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double v_valacel;
		int v_valrec;
		int v_valtiem;
		int v_valvelfin;
		int v_valvelini;
		// area de descripcion
		// enunciado://Una locomotora necesita 10 s. para alcanzar su velocidad normal que es 25m/s.
		// Suponiendo que su movimiento es uniformemente acelerado, Que aceleracion se le ha comunicado y que espacio 
		// ha recorrido antes de alcanzar la velocidad regular?//
		// desarrollado por: Juan Fernando Parra
		// version: 1.0
		// fecha: 2/22/2023
		// area de delcaracion de variables
		// area de inicializacion de variables
		v_valvelini = 0;
		v_valvelfin = 0;
		v_valtiem = 0;
		v_valacel = 0.0;
		v_valrec = 0;
		// area de lectura
		System.out.println("escribir la velocidad inicial");
		v_valvelini = Integer.parseInt(bufEntrada.readLine());
		System.out.println("escribir la velocidad final");
		v_valvelfin = Integer.parseInt(bufEntrada.readLine());
		System.out.println("escribir el tiempo transcurrido entre el cambio de velocidad inicial y velocidad final");
		v_valtiem = Integer.parseInt(bufEntrada.readLine());
		// area de procesos
		v_valacel = (v_valvelfin-v_valvelini)/(v_valtiem);
		System.out.println("La aceleracion en m/s^2 fue de : "+v_valacel);
		v_valrec = (v_valvelini*v_valtiem)+((1/2*v_valacel)*(Math.pow(v_valtiem,2)));
		System.out.println("El recorrorrido en metros antes de alcanzar la velocidad regular fue de: "+v_valrec);
	}


}

