
function showAlert(section) {
    alert(`Navegando a la sección: ${section}`);
}

document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector("nav");
    nav.style.backgroundColor = "#333"; // Cambia el color de fondo
    nav.style.color = "#fff"; // Cambia el color del texto
});
