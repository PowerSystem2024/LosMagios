
package Ejercicio1;
//CLASE 11 - EJERCICIO 1
import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
         Scanner entrada = new Scanner(System.in);
         System.out.println("Digite la primer nota: ");
         var nota1 = Integer.parseInt(entrada.nextLine());
         System.out.println("Digite la segunda nota: ");
         var nota2 = Integer.parseInt(entrada.nextLine());
         System.out.println("Digite la tercer nota: ");
         var nota3 = Integer.parseInt(entrada.nextLine());
         
         var promedio = (nota1 + nota2 + nota3) / 3;
         
         if(promedio >= 70){
             System.out.println("El alumno esta aprobado con : " + promedio);
         }
         else{
             System.out.println("El alumno desaprobó con: " + promedio);
         }
         
    }
}
