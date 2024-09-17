//Tienda de libros
package Ejercicio1;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el nombre de el libro: ");
        String nombreLibro = entrada.nextLine();
        System.out.println("Digite el id del libro: ");
        int idLibro = Integer.parseInt(entrada.nextLine());
        System.out.println("Ingrese el precio del libro: ");
        double precioLibro = Double.parseDouble(entrada.nextLine());
        System.out.println("Confirme si el envío es gratuito");
        boolean envioGratis = Boolean.parseBoolean(entrada.nextLine());
        System.out.println(nombreLibro + " #" + idLibro);
        System.out.println("Precio del Libro: $" + precioLibro);
        System.out.println("Envio gratis: " + envioGratis);
    }
}
