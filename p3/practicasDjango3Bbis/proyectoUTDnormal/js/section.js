// Mostrar alerta al hacer clic en los enlaces del menú
function showAlert(section) {
    alert(`Navegando a la sección: ${section}`);
}

// Cambiar el color de fondo del menú dinámicamente
document.addEventListener("DOMContentLoaded", () => {
    const nav = document.querySelector("nav");
    nav.style.backgroundColor = "#333"; // Cambia el color de fondo
    nav.style.color = "#fff"; // Cambia el color del texto
});
