
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona  persona1;
        persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Erwin"; //El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Citadino";
        persona1.ObtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = "+persona2);
        System.out.println("persona2 = " + persona1);
        persona2.ObtenerInformacion();
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.ObtenerInformacion();
    }
}
