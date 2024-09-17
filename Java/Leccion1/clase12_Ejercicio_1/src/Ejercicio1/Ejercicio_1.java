
package Ejercicio1;
//  CLASE 12 - EJERCICIO 1
import java.util.Scanner;

public class Ejercicio_1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero de horas: ");
        var horas = Integer.parseInt(entrada.nextLine());
        int dias, semanas;
        semanas = horas / 168;
        horas %= 168;
        dias = horas / 24;
        System.out.println("dias = " + dias);
        horas %= 24;
        
        System.out.println(semanas + " Semanas, " + dias + " dias y " + horas + " horas.");
        
        
        
    }
    
}
