
package Ejercicio3;
//CLASE 12 - EJERICICIO 3

import java.util.Scanner;

public class Ejercicio3 {
         public static void main(String[] args) {
         Scanner entrada = new Scanner(System.in);
         System.out.println("Digite la calificacion de participacion: ");
         double participacion = Double.parseDouble(entrada.nextLine());
         participacion *= 0.1;
         
         System.out.println("Digite la calificacion del primer examen parcial: ");
         double examen1 = Double.parseDouble(entrada.nextLine());
         examen1 *= 0.25;
         
         System.out.println("Digite la calificacion del segundo examen parcil: ");
         double examen2 = Double.parseDouble(entrada.nextLine());
         examen2 *= 0.25;
         
         System.out.println("Digite la calificacion del examen final: ");
         double examenFinal = Double.parseDouble(entrada.nextLine());
         examenFinal *= 0.4;
         
         double notaFinal = participacion + examen1 + examen2 + examenFinal;
             System.out.println("La nota final del alumno es: " + notaFinal);
         
    }
}
