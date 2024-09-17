package ejercicio_6;

import java.util.Scanner;

public class Ejercicio_6 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float guillermo, luis, juan, total;
        
        System.out.println("Por favor ingrese una cantidad: ");
        guillermo = Float.parseFloat(entrada.nextLine());
        luis = guillermo / 2;
        juan = (guillermo + luis) / 2;
        total = guillermo + luis + juan;
     
        System.out.println("El dinero de Guillermo es: US$" + guillermo);
        System.out.println("El dinero de Luis es: US$" + luis);
        System.out.println("El dinero de juan es: US$" + juan);
        System.out.println("El total de dinero entre los 3 es: US$" + total);
        
        
  
        
        
    }
    
}
