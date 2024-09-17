/*
Pedir numeros hasta que se teclee uno negativo,
y mostrar cuantos numeros se han introducido
Lo hacemos primero con la clase Scanner
Luego con la clase JOptionPane
*/
package Ciclos04;

import java.util.Scanner;

public class Ciclos04 {
    public static void main(String[] args) {
        int numero, contador;
        contador = 0;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){
            System.out.println("El numero " + numero + " es POSITIVO");
            contador++;
            System.out.println("Ingrese otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("Ha ingresado " + contador + " numero que no son negativos");
    }

    
}
