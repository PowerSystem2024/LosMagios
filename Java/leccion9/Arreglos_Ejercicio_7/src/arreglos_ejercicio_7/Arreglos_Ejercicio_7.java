/*
Ejercicio 7: Leer por teclado una tabla de 10 elementos numeros enteros
y una posicion(entre 0 y 9). Eliminar el elemento situado en la posicion
dada sin dejar huecos.
*/
package arreglos_ejercicio_7;

import java.util.Scanner;

public class Arreglos_Ejercicio_7 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int arreglo[] = new int[10];
        int posicion,j = 0;
        
        System.out.println("Llenar el arreglo: ");
        for (int i = 0; i < 10; i++) {
            System.out.println(i+". Digite un numero: ");
            arreglo[i] = entrada.nextInt();
        }
        
        System.out.println();
        do{
            System.out.println("Digite una posicion a elimnar entre (0-9): ");
            posicion = entrada.nextInt();
        }while(posicion < 0 || posicion >9);
        
        //Eliminando el elemento de posicion indicada
        for (int i = posicion; i < 9; i++) {
            arreglo[i] = arreglo[i+1];
        }
        
        System.out.println("\nEl arreglo queda: ");
        for (int i = 0; i < 9; i++) {
            System.out.println(arreglo[i]+" - ");
        }
        System.out.println();
    }
}
