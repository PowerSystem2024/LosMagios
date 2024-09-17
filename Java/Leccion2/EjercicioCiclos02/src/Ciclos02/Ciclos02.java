
package Ciclos02;
/*Ejercicio 2: Leer un numero indicar si es negativo o positivo. El proceso se va a repetir hasta que el numero ingresado sea 0 
Hacer este ejercicio con la clase JOptionePane
*/
import javax.swing.JOptionPane;
public class Ciclos02 {
    public static void main(String[] args) {
        
        int numero =  Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es POSITIVO");
            }else{
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es NEGATIVO");
            }
            numero =  Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        JOptionPane.showMessageDialog(null, "El numero " + numero + " finalizó el programa.");
    }
}

