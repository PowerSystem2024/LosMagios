/*
Ejercicio 1: Leer 5 numeros, guardalos en un arreglos y 
mostralos en el mismo orden introducidos
*/
package arreglos_ejercicio_1;

import java.util.Scanner;

public class Arreglos_Ejercico_1 {
    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float[] arreglos = new float[5];
        
        System.out.println("Guardando los datos en el arreglos");
        for(int i =0 ;i<5;i++){
            System.out.println((i+1)+". Digite un numero: ");
            arreglos[i] = entrada.nextFloat();
        }
        
        System.out.println("\nImprimir los elementos del arreglo");
        for(float i:arreglos){
                System.out.println(i+" ");
        }
        System.out.println("\n");
    }
}
