
package test;

import domain.Cliente;
import domain.Empleado;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Gonzalo", 57000.00);
        System.out.println("empleado1 = " + empleado1);
        
        Date fecha1 = new Date();
        
        Cliente cliente1 = new Cliente(fecha1, true, "Franco", 'M', 22, "9 de Julio 1413");
        System.out.println("cliente1 = " + cliente1);
    }
}
