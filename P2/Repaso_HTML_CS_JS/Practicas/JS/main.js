//Este es un comentario de una sola línea

/* Esto es
 un comentario
de varias líneas
*/

//alerta
// alert("Soy una ventana de alerta");

// variables

var nombre = "Alejandro";
let nombre2 = "Daniel";
let edad = 20
let logica = true;
let estatura = 1.80;


// Mostrar en pantalla con Write
let concatenacion = "La persona: " + nombre + ",  tiene la edad de: " + edad + " años";
// document.write(concatenacion);
// document.write("La persona: " + nombre + ",  tiene la edad de: " + edad + " años");


//Mostrar en pantalla con document.getElementById
let datos = document.getElementById("informacion");
datos.innerHTML =`
    <br>
    <hr>
    <h1>La persona: ${nombre2}, tiene una edad de: ${edad} años</h1>
    <hr>
    <br>
`;

let datos2 = document.getElementById("informacion2");
datos2.innerHTML ="<h1>La persona: " + nombre2 + ", tiene una edad de: " + edad + " años</h1>";

// Condicionales if

if (estatura = 1.90) 
    // document.write("Es una persona alta");
    datos.innerHTML += `
        <h3>Es una persona alta</h3>
        `;
else
    // document.write("Es una persona promedio");
    datos.innerHTML += `
        <h3>Es una persona promedio</h3>
`;

// Ciclos

for (let i =1;i<=5;i++)
{
    datos.innerHTML+=`<hr><h3>For: el numero es: ${i} </h3>`
}

let i = 1;
while(i<=5)
{
    datos.innerHTML+=`<hr><h3>While: el numero es: ${i} </h3>`
    i++;
}

i = 1;
do 
{
    datos.innerHTML+=`<hr><h3>DO-While: el numero es: ${i} </h3>`
    i++;
} 
while (i<=5);

// funciones

// 1.- funcion que no recibe parametros y no regresa valor
function suma()
{
    let n1 = 2;
    let n2 = 4;
    suma=n1 + n2
    console.log("La suma es "+suma);
    datos.innerHTML+=`<hr><h3>La suma es: ${suma}</h3>`
}

suma()

// 2.- funcion que no parametros y regresa valor
function suma2()
{
    let n1 = 2;
    let n2 = 4;
    suma = n1 + n2;
    return suma;
}

let sum = suma2();
datos.innerHTML+=`<hr><h3>La suma2 es: ${sum}</h3>`

// 3.- que recibe parametros y no regresa 
function suma3(numero1, numero2)
{
    let n1 = numero1;
    let n2 = numero2;
    suma = n1 + n2;
    datos.innerHTML+=`<hr><h3>La suma3 es: ${suma}</h3>`
}

suma3(3,4);

// 4.- que recibe parametros y regresa valor
function suma4(numero1,numero2)
{
    let n1 = numero1;
    let n2 = numero2;
    suma = n1 + n2;
    return suma;
}

sum = suma4(8,5);

datos.innerHTML+=`<hr><h3>La suma4 es: ${sum}</h3>`

// arreglos

let animales =[]
animales[0]="perico";
animales[1]="leon";
animales[2]="perro";

datos.innerHTML+=`<hr><h3> El rey de la selva es: ${animales[1]}</h3>`


for(let i=0;i<animales.length;i++)
{
    datos.innerHTML+=`<hr><h3> El animal es: ${animales[i]}</h3>`
}

animales.forEach(element => {
    datos.innerHTML+=`<hr><h3>El animal es: ${element}</h3>`;
});

// funcion de flecha 

// funcion normal 
function sumaR(a,b)
{
    return a + b 
}

datos.innerHTML+=`<hr><h3>La sumaR es: ${sumaR(3,6)} </h3>`;

const sumaFlecha = (a,b) => a+b;

datos.innerHTML+=`<hr><h3>La sumaFlecha es: ${sumaFlecha(3,6)} </h3>`;  