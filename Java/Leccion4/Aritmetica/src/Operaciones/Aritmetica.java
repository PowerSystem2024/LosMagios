
package Operaciones;

public class Aritmetica {
    //Atributos de la clase
    int a;
    int b;
    
    // El constructor es un metodo especial
    public Aritmetica(){//Constructor 1
        System.out.println("Se esta ejecutando este constructor numero uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){//Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero dos");
    }
    
    //Metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado "+ resultado);
    }
    
    public int sumarConRetorno(){
        //int resultado = a + b; //podemos poner una variable como utilizamos o una expresion
        return a + b;
    }
    
    public int sumarConArgumentos(int a, int b){
        this.a = a; //El argumento a se asigna al atributo this.a
        this.b = b; //El argumento b se asigna al atributo this.b
        //return a + b;
        return sumarConRetorno();
    }
}
