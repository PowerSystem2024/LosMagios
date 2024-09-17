package Leccion_2;

import java.util.Scanner;

public class Leccion2 {
    public static void main(String[] args) {
        //CLASE 10
        var condicion = true;
        if(condicion){
                System.out.println("La condicion es verdadera");
        }else{
                System.out.println("La condicion es falsa");
        }
        
        var numero = 4;
        var numeroTexto = "Numero desconocido";
        if (numero == 1){
            numeroTexto = "Numero uno";
        }else if(numero == 2){
            numeroTexto = "Numero dos";
        }else if(numero == 3){
            numeroTexto = "Numero tres";
        }else if (numero == 4){
            numeroTexto = "Numero cuatro";
        }else{
            numeroTexto = "Numero no encontrado";
        }
        System.out.println("numeroTexto = " + numeroTexto);

       Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero del 1 al 4");
       numero = Integer.parseInt(entrada.nextLine());
       numeroTexto = "Valor desconocido";
       switch(numero){
           case 1:
               numeroTexto = "Numero uno";
               break;
           case 2:
               numeroTexto = "Numero dos";
               break;
           case 3:
               numeroTexto = "Numero tres";
               break;
           case 4: 
               numeroTexto = "Numero 4";
               break;
           default:
               numeroTexto = "Caso no encontrado";
            
       }
       
        System.out.println("numeroTexto = " + numeroTexto);
    }
}
