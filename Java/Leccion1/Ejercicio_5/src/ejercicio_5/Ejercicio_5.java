 package ejercicio_5;

 import java.util.Scanner;
 
public class Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float nota1, nota2, nota3, suma;
        
        //Guardamos las 3 notas
        System.out.println("Digite la primera calificacion: ");
        nota1 = Float.parseFloat(entrada.nextLine());
        System.out.println("Digite la segunda calificacion: ");
        nota2 = Float.parseFloat(entrada.nextLine());
        System.out.println("Digite la tercera calificacion: ");
        nota3 = Float.parseFloat(entrada.nextLine());
        
        suma = nota1 + nota2 + nota3;
        System.out.println("Suma de calificaciones= " + suma);
    }
    
}
