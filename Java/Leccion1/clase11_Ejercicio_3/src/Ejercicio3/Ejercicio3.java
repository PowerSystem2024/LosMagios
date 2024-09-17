
package Ejercicio3;
//CLASE 11- EJERCICIO 3
import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var numero1 = Integer.parseInt(entrada.nextLine());
        System.out.println("Digite otro numero: ");
        var numero2 = Integer.parseInt(entrada.nextLine());
        int resultado;
        
        if(numero1 > numero2){
            resultado = numero1 - numero2;
        }
        else if(numero1 == numero2){
            resultado = numero1 * numero2;
        }
        else{
            resultado = numero1 + numero2;
        }
        
        System.out.println("resultado = " + resultado);
        
    }
    
}
