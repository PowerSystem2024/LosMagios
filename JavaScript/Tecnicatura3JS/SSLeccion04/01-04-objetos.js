let x = 10; //variable de tipo primitiva
console.log(x.length); 

console.log("Tipos primitivos");
//Objeto
let persona = {
    nombre: "Carlos",
    apellido: "Gil",
    email: "cgil@gmail.com",
    edad : 28,
    idioma: "es",
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //Metodo o funcion en JavaSript
        return this.nombre+" "+this.apellido;
    },
    get nombreEdad(){ //Este es el metodo get
        return "El nombre es: "+this.nombre+", Edad: "+this.edad;
    } 
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona);
console.log(persona.nombreCompleto());

console.log("Ejecutando con un objeto");
let persona2 = new Object (); //Debe crear un nuevo objeto en memoria
persona2.nombre = "Juan";
persona2.direccion = "Sarmiento 22";
persona2.telefono = "3456364534";
console.log(persona2.telefono);

console.log("Creamos un nuemo objeto");
console.log(persona["apellido"]); //Accedemos como si fuera un arreglo

console.log("Usamos el ciclo for in");
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
console.log("Cambiamos y eliminamos un error");
persona.apellida = "Bucca"; //Cambiamos dinamicamente un valor del objeto
delete persona.apellida; //Eliminamos el error
console.log(persona);

//Distinta fomras de imprimir un objeto
//Numero 1: es la mas sencilla: concatenar cada valor de cada propiedad
console.log("Distinta fomras de imprimir un objeto: forma 1");
console.log(persona.nombre+", "+persona.apellido);

//Numero 2: A traves del ciclo for in
console.log("Distinta fomras de imprimir un objeto: forma 2");
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
} 

//Numero 3: La funcion Object.values()
console.log("Distinta fomras de imprimir un objeto: forma 3");
let perosonaArray = Object.values(persona);
console.log(perosonaArray);

//Numero 4: Utilizaremos el metodo JSON.stringify
console.log("Distinta fomras de imprimir un objeto: forma 4");
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log("Comenzamos a utilizar el metodo get");
console.log(persona.nombreEdad);

console.log("Comenzamos con el metodo get y set para idiomas");
persona.lang = "en"
console.log(persona.lang);

function Persona3(nombre, apellido, email){ //Constructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+" "+this.apellido;
    }
}
let padre = new Persona3("Leo", "Lopez", "lopezl@gmail.com");
padre.nombre = "Luis"; //Modificamos el nombre
padre.telefono = "34564357561"; //Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); //Utilizamos la funcion
let madre = new Persona3("Laura", "Contrera", "contretal@gmail.com");
console.log(madre);
console.log(madre.telefono); //La propiedad no esta definida
console.log(madre.nombreCompleto());

//Diferentes formas de crear 1 objeto
//Caso objeto 1
let miObjeto = new Object(); //Esta es unas opcion formal
//Caso objeto 2
let miObjeto2 = {}; //Esta opcion es breve y recomendada

//Caso String 1 
let miCadena1 = new String("Hola");
//Caso String 2 
let miCadena2 = "Hola"; //Estas es la sintaxis simplificada y recomendada 

//Caso con numeros 1
let miNumero = new Number(1) //Es formal no recomendable
//Caso con numeros 2
let miNumero2 = 1; //Sintaxis recomendada 

//Caso boolean 1
let miBoolean = new Boolean(false); //Formal
//Caso boolean 2
let miBoolean2 = false; //Sintaxis recomendada

//Caso Arreglos 1
let miArreglo1 = new Array(); //Formal
//Caso Arreglos 2
let miArreglo2 = []; //Sintaxis recomendada

//Caso funcion 1
let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
//Caso funcion 2
let miFuncion2 = function(){}; //Notacion simplificada y recomendada

//Uso de prototype
Persona3.prototype.telefono = "34653456474";
console.log(padre);
console.log(madre.telefono);
madre.telefono = "456745674567456745674567";
console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: "Juan",
    apellido: "Perez",
    nombreCompleto2: function(titulo, telefono){
        return titulo+": "+this.nombre+" "+this.apellido+" "+telefono;
        //return this.nombre+" "+this.apellido;
    }
}

let persona5 = {
    nombre: "Carlos",
    apellido: "Lara",
}

console.log(persona4.nombreCompleto2("Lic.", "34654567475647"));
console.log(persona4.nombreCompleto2.call(persona5, "Ing.", "56475674456745674756"));

//Metodo Apply
let arreglo = ["Ing.", "22222222222"];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
