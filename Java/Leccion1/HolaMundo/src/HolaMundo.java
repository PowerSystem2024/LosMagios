
import java.util.Scanner;

public class HolaMundo {

   /* public static void main(String[] args) {
        System.out.println("Hola Mundo desde Java");

        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);

        //Tipo Strig
        String miVariableCadena = "Bienvenidos!";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos creciendo en programacion";
        System.out.println(miVariableCadena);
        //var inferencia de tipos en JAVA
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        //soutv + tab
        System.out.println("miVariableEntera2 = " + miVariableEntera2);

        //Reglas para definir una variable 
        //se las escribe con camelCase
        //si pueden comenzar con _(pero no es tan comun)
        //tambien se puede usar el signo del dolar
        var miVariableEjemplo = 45;

        var usuario = "Rodrigo";
        var titulo = "Filosofo";
        var union = usuario + " " + titulo;
        System.out.println("union = " + union);*/
 /*
        var usuario = "Rodrigo";

        var a = 8;
        var b = 4;

        System.out.println(a + b);//suma q nos da 12

        //En este caso al ser una cadena la primera variable de la operacion 
        //se realiza una concatenacion y no una suma porque la prioridad es 
        //la primera variable
        System.out.println(usuario + a + b); // Rodrigo84
        //Para cambiar la prioridad podemos hacer esto
        //Al estar entre parentesis a+b y al ser numeros primero se suman 
        //y desp se concatenan
        System.out.println(usuario + (a + b));//Rodrigo12

        System.out.println(a + b + usuario);//12Rodrigo

        //Ejercicio CARACTERES ESPECIALES CON JAVA
        var nombre = "Natalia";

        System.out.println("Nueva linea \n" + nombre);//Salto de linea \n
        System.out.println("Tabulador: \t" + nombre); //Tabulador
        System.out.println("\t\t.:MENU:.");
        System.out.println("Retroceso: \b\b" + nombre);//Retroceso \b borra un caracter hacia atras
        System.out.println("Comillas simples: \'"+nombre+"\'");//Comillas simples
        System.out.println("Comillas dobles: \""+nombre+"\"");//Comillas dobles \"
         */
 /*
        //Clase Scanner
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite su nombre:");
        var usuario2 = entrada.nextLine();//El dato q recibimos es de tipo string
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+titulo2+" "+usuario2);
        
        //Ejercicio: detalles libro
        Scanner scanner = new Scanner(System.in);
        System.out.println("Proporciona el titulo: ");
        String titulo = scanner.nextLine();
        System.out.println("Proporciona el auto: ");
        String autor = scanner.nextLine();
        System.out.println(titulo + " Fue escrito por: " + autor);
         */
 /*
        //CLASE 4 -- Tipos primitivos en JAVA
        byte numEnteroByte = 127;
        System.out.println(numEnteroByte);
        System.out.println("Valor minimo del byte: " + Byte.MIN_VALUE);
        System.out.println("Valor maximo del byte: " + Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println(numEnteroShort);
        System.out.println("Valor minimo del short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del short: " + Short.MAX_VALUE);
        
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: " + Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del long: " + Long.MIN_VALUE);
        System.out.println("Valor maximo del long: " + Long.MAX_VALUE);
         */
 /* 
        float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del float: " + Float.MIN_VALUE);
        System.out.println("Valor maximo del float: " + Float.MAX_VALUE);
        
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor minimo del double: " + Double.MIN_VALUE);
        System.out.println("Valor maximo del double: " + Double.MAX_VALUE);
         */

        //CLASE 5
        //Inferencias de tipos var y tipos primitivos
        /*var numEntero = 20; //Las literales sin puntos automaticamente son de tipo int
        System.out.println("numEntero = " + numEntero);
       
       var numFloat = 15.4F; //Automaticamente con el punto se transforma en tipo double, pero para FLOAT hay q poner F a la par de la literal
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.7; //Automaticamente con el punto se transforma en tipo double
        System.out.println("numDouble = " + numDouble);
         */
        //Tipos primitivos char
        /*
       char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        char varCaracter = '\u0024'; //Indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //Un caractder especial
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 = '\u0024'; //Indicamos a java la asignacion con el codigo unicode
        System.out.println("varCaracter1 = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; //Valor entero y le asigna un tipo int si NO le ponemos el (char)
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; //Un caractder especial
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
        /**
         * **************************************************
         */
        //CLASE 6
        /* 
        //tipos primitivos booleanos
        var varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es verde");
        }else{
            System.out.println("La bandera es roja");
        }
        
        //Algoritmo mayor de edad
        var edad = 30;
        var adulto = edad >= 18; //valor booleano
        if(adulto){
            System.out.println("Eres mayor de edad");
        }else{
            System.out.println("Eres menor de edad");
        }
        
        
       //Conversion de tipos primitivos
       
       var edad = "20";
        System.out.println("edad = " + (edad + 1));
       var edad2 = Integer.parseInt("20");
        System.out.println("edad2 = " + (edad2 + 1));
       var valorPi = Double.parseDouble("3.1416");
        System.out.println("valorPi = " + valorPi);
       
       //Pedir un Valor
       // A entrada se la declara una sola vez para hacer muchas entradas
       var entrada = new Scanner(System.in);
        //System.out.println("Digite su edad: ");
       //edad2 = Integer.parseInt(entrada.nextLine());
        //System.out.println("edad2 = " + edad2);
       
       //Convertir tipo entero a string
       var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
       //Convertir cadena a tipo Char
       var fraseChar = "Programando".charAt(6);
        System.out.println("fraseChar = " + fraseChar);
        System.out.println("Digite un caracter: ");
        //como la entrada es de tipo string y la variable fraseChar es de tipo char, convertimos el valor de entrada en char
       fraseChar = entrada.nextLine().charAt(0);
        System.out.println("fraseChar = " + fraseChar);*/
        //---------------------------------------------------
        //----------------------------------------------------
        /*
        //CLASE 7 - OPERADORES PARTE 1
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion suma = " + solucion);

        solucion = num1 - num2;
        System.out.println("solucion resta= " + solucion);

        solucion = num1 / num2;
        System.out.println("solucion division= " + solucion);

        solucion = num1 * num2;
        System.out.println("solucion  multiplicacion= " + solucion);

        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 resultado= " + solucion2);

        solucion = num1 % num2; //guardo el residuo entero de la division
        System.out.println("solucion = " + solucion);

        if (num2 % 2 == 0) {
            System.out.println("Es un numero par");
        } else {
            System.out.println("Es un numero impar");
        }

        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);

        varNum1 += 1; //num1 = num1 + 1
        System.out.println("varNum1 = " + varNum1);
        // -= *= /= %=

        varNum1 -= 1;
        System.out.println("varNum1 = " + varNum1);
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        varNum1 /= 4;
        System.out.println("varNum1 = " + varNum1);
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);

        //CLASE 8 - OPERADORES PARTE 2
        //Operadores unarios: cambio de signo
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);

        //Operador de negacion 
        var varC = true;
        var varD = !varC;
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);

        //Operadores unarios de Incremento: Preincremento
        var varE = 9; //se va a modificar su valor 
        var varF = ++varE; //simbolo antes de las variable
        //Primero se incrementa la variable y despues se usa su valor 
        System.out.println("varE = " + varE);//se incrementa en la unidad
        System.out.println("varF = " + varF);//va a sumar uno

        //PostIncremento 
        var varG = 3;
        var varH = varG++;//primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);

        //Operadores Unarios de decremento
        //PreDecremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);
        System.out.println("varJ = " + varJ);

        //PostDecremento
        var varK = 8;
        var varL = varK--;
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);

        //Operadores de Igualdad y Relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);

        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);

        //En este ejemplo solo esta haciendo una comparacion de 'referencia', NO de contenido
        var cadenaA = "Hello";
        var cadenaB = "Hella";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);

        //Para comparar de verdad el contenido de una cadena con otra:
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);

        //OPERADORES RELACIONALES < <= >= > != == 
        var gVar = aNum <= bNum;
        System.out.println("gVar = " + gVar);

        if (aNum % 2 == 0) {
            System.out.println("El numero es par");
        } else {
            System.out.println("El numero es impar");
        }

        var edad = 30;
        var adulto = 18;
        if (edad >= adulto) {
            System.out.println("Es mayor de edad");
        } else {
            System.out.println("Es menor de edad");
        }

        //OPERADORES CONDICIONALES (and / or)
        //AND
        var valorA = 11;
        var valorMinimo = 0;
        var valorMaximo = 10;
        var respuesta = valorA >= valorMinimo && valorA <= valorMaximo;

        if (respuesta) {
            System.out.println("Esta dentro del rango establecido");
        } else {
            System.out.println("NO esta dentro del rango establecido");
        }

        //OR 
        var vacaciones = false;
        var diaLibre = true;
        if (vacaciones || diaLibre) {
            System.out.println("Puede Asistir al Juego");
        }else{
            System.out.println("No puede asistir al juego");
        }
        
        //Operador TERNARIO
       var resultadoT = (5 > 4) ? "VERDADERO" : "FALSO";
        System.out.println("resultadoT = " + resultadoT);
    
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Es Par" : "Es Impar";
        System.out.println("resultadoT = " + resultadoT);
        
        
        //prioridades
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x); //6
        System.out.println("y = " + y); //9
        System.out.println("z = " + z); //16
        
        
        var solucionAritmetica = 4 + 5 * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4+5) * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        */
        
        /////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////
        
        //CLASE 10 - CONDICIONALES
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    }
    
    
    }
