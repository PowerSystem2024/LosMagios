/*
 Ejercicio 7: pedir numeros hasta que se introduzca uno negativo y calcular la media
 */
package Ciclos07;

import javax.swing.JOptionPane;

public class Ejercicio07 {
    public static void main(String[] args) {
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero >= 0){
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        if(conteo == 0){
            JOptionPane.showMessageDialog(null,"\nError, la division entre cero no existe" );
        }else{
            promedio = (float)suma / conteo;
            JOptionPane.showMessageDialog(null,"\nEl promedio es: " + promedio );
            
        }
    }
}
