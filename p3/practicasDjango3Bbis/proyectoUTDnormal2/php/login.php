<?php
session_start();
$loggedIn = isset($_SESSION['user_id']);
if ($loggedIn) {
    header("Location: index.php"); 
    exit;
}
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login | PHP Proyecto UTD</title>
    <link rel="stylesheet" href="../css/estilos.css">
</head>
<body>
    <header>
        <div id="logotipo">
            <img src="../img/logophp.png" alt="Imagen PHP" title="PHP">
            <h1>PHP Proyecto Web</h1>
        </div>
    </header>
    <nav>
        <ul>
            <li><a href="../index.php">Inicio</a></li>
            <li><a href="registro.php">Registro</a></li>
            <li><a href="login.php">Login</a></li>
        </ul>
    </nav>
    <section id="content">
        <div class="box">
            <h1>Iniciar Sesión</h1>
            <form id="loginForm">
                <label for="username">Usuario:</label>
                <input type="text" id="username" name="username" placeholder="Ingresa tu usuario" required>

                <label for="password">Contraseña:</label>
                <input type="password" id="password" name="password" placeholder="Ingresa tu contraseña" required>

                <button type="submit">Iniciar Sesión</button>
            </form>
        </div>
    </section>
    <footer>
        <p>PHP Proyecto UTD &copy; 2024</p>
    </footer>
    <script src="../js/funciones.js" defer></script>
</body>
</html>
