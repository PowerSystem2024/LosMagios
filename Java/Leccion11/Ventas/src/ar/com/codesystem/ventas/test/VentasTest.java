package ar.com.codesystem.ventas.test;

import ar.com.codesystem.Orden;
import ar.com.codesystem.Producto;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Camisa", 5500.00);
        Producto producto4 = new Producto("Zapatos", 12000.00);
        Producto producto5 = new Producto("Cinturon", 2500.00);
        Producto producto6 = new Producto("Bufanda", 3200.00);
        Producto producto7 = new Producto("Gorra", 1500.00);
        Producto producto8 = new Producto("Guantes", 1800.00);
        
        Orden orden1 = new Orden();
        // Agregamos productos a la orden
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto5);

        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto6);
        orden2.agregarProducto(producto7);
        orden2.agregarProducto(producto8);
        orden2.mostrarOrden();

    }
}
