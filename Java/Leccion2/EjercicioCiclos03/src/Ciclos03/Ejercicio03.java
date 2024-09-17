
/* 
Ejercicio 3: Leer numeros hasta que se introduzca un numero 0
Para cada uno indicar si es par o impar
Primero lo haremos con la clase scanner
Luego con la clase JOptionPlane
*/
package Ciclos03;

import javax.swing.JOptionPane;

public class Ejercicio03 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero"));
        while(numero != 0){
            if(numero %2 == 0){
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es PAR");
            }else{
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese otro numero"));
        }
        JOptionPane.showMessageDialog(null, "El numero " + numero + " finalizó el programa.");
    }
}
