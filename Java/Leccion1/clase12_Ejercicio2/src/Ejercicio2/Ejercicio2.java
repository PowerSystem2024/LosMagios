
package Ejercicio2;
//  CLASE 12 - EJERCICIO 2 

import java.util.Scanner;


public class Ejercicio2 {
    public static void main(String[] args) {
         Scanner entrada = new Scanner(System.in);
         System.out.println("Digite el valor de a: ");
         double a = Double.parseDouble(entrada.nextLine());
         System.out.println("Digite el valor de b: ");
         double b = Double.parseDouble(entrada.nextLine());
         double resultado = Math.pow(a, 2) + Math.pow(b, 2) + 2 * a * b;
         
         System.out.println("resultado = " + resultado);
         
         
    }
}
