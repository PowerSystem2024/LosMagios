
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Gonzalo", 57.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        //Modificamos a taves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Esto tampoco no se puede utilizar mas
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        
        Persona personaTarea = new Persona("Juan Carlos", 90.000, false);
        System.out.println("personaTarea su nombre es: "+personaTarea.getNombre());
        personaTarea.setNombre("Roberto");
        personaTarea.setSueldo(50.000);
        personaTarea.setEliminado(true);
        
        System.out.println("personaTarea con su nombre modificado: "+personaTarea.getNombre());
        System.out.println("personaTarea con su sueldo modificado: "+personaTarea.getSueldo());
        System.out.println("personaTarea para obtener el booleano modificado: "+personaTarea.isEliminado());
        
        //System.out.println("persona1: "+persona1.toString());
        System.out.println("persona1 = " + persona1);
        
    }
}
