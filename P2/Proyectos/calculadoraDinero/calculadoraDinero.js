function convertir() {
    let cantidad = parseFloat(document.getElementById("cantidad").value);
    let conversion = document.getElementById("conversion").value;
    let resultado;
    const rates = {
        mxnToUsd: 1 / 20.0287,
        usdToMxn: 20.0287,
        eurToUsd: 1.0813,
        usdToEur: 1 / 1.0813,
        eurToMxn: 21.690,
        mxnToEur: 1 / 21.690
    };

    const images = {
        mxnToUsd: "united-states.png",
        usdToMxn: "flag.png",
        eurToUsd: "united-states.png",
        usdToEur: "european-union.png",
        eurToMxn: "flag.png",
        mxnToEur: "european-union.png"
    };

    if (!isNaN(cantidad)) {
        resultado = cantidad * rates[conversion];
        document.getElementById("resultado").innerHTML = `
            <h2>Resultado: ${resultado.toFixed(2)}</h2>
            <img src="${images[conversion]}" alt="Currency Image" style="width:50px; height:50px; vertical-align: middle;">
        `;
    } else {
        document.getElementById("resultado").innerHTML = `<h2>Por favor ingresa un número válido.</h2>`;
        alert("Debes ingresar una cantidad numérica.");
    }
}
