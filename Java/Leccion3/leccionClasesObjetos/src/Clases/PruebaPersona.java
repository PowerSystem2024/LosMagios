
package Clases;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1; //Le asignamos un tipo CLASE(Persona)a la variable persona1
        persona1 = new Persona(); //Llamamos al cosntructor
        persona1.nombre = "Ariadna";
        persona1.apellido = "Coronel";
        persona1.obtenerInformacion();
        
        //Instancia y objeto es lo mismo
        //Cada objeto es distinto
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        
        persona2.obtenerInformacion(); 
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordnini";
        persona2.obtenerInformacion();
        
    }
}
