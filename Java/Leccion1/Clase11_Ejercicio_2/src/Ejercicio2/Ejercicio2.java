
package Ejercicio2;
//CLASE 11- EJERCICIO 2
import java.util.Scanner;


public class Ejercicio2 {
    public static void main(String[] args) {
         Scanner entrada = new Scanner(System.in);
         System.out.println("Digite la cantidad a pagar: ");
         var compra = Double.parseDouble(entrada.nextLine());
         var descuento = 0D;
         if(compra > 100){
             descuento = compra * 0.2;
         }
         else{
             descuento = 0;   
         }
         var precioFinal = compra - descuento;
         System.out.println("El monto a pagar es = " + precioFinal);
    }
}
