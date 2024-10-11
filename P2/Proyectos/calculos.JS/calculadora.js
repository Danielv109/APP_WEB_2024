function operaciones() {
    let numero1 = parseInt(document.getElementById("numero1").value);
    let numero2 = parseInt(document.getElementById("numero2").value);
    let operacion = document.getElementById("operacion").value;
    let resultado;

    if (isNumber(numero1) && isNumber(numero2)) 
    {
        switch (operacion) 
        {
            case "+":
                resultado = numero1 + numero2;
                break;
            case "-":
                resultado = numero1 - numero2;
                break;
            case "*":
                resultado = numero1 * numero2;
                break;
            case "/":
                resultado = numero1 / numero2;
                break;
        }

        document.getElementById("resultado").innerHTML = `<h3>${numero1} ${operacion} ${numero2} = ${resultado}</h3>`;


    }
    else{
        alert("Debes ingresar un número en los campos");
    }

    function isNumber(n)
    {
        return !isNaN(parseInt(n) && isFinite(n));
    }
}
