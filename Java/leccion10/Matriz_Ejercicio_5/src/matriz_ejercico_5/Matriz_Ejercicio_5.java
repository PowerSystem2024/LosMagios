/*
Ejercicio 5: Crear y cargar una matriz de tamaño n x m, mostrar la suma
de cada fila y de cada columna.
 */
package matriz_ejercico_5;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Matriz_Ejercicio_5 {
    public static void main(String[] args) {
            Scanner entrada = new Scanner(System.in);
            int matriz[][],nFilas,nCol,sumaFilas,sumaCol;
            int posFila,posCol;
            
            nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de filas: "));
            nCol = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de columnas: "));
            
            matriz = new int [nFilas] [nCol];
            int filas[] = new int [nFilas];
            int columnas[] = new int [nCol];
            
            System.out.println("Rellenando la matriz: ");
            for(int i=0;i<nFilas;i++){
                    for(int j=0;j<nCol;j++){
                        System.out.println("Matriz ["+i+"]["+j+"]: ");
                        matriz[i][j] = entrada.nextInt();
                    }
            }
            
            System.out.println("\nMatriz Original: ");
    }
}
