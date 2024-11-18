<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $title ?? 'PHP Proyecto Web'; ?></title>
    <link rel="stylesheet" href="css/estilos.css" type="text/css">
</head>
<body>
    <header>
        <div id="logotipo">
            <img src="img/logodjango.jpg" alt="Imagen PHP" title="PHP">
            <h1>PHP Proyecto Web</h1>
        </div>
    </header>
    <nav>
        <ul>
            <li><a href="index.php" onclick="showAlert('Inicio')">Inicio</a></li>
            <li><a href="acercade.php" onclick="showAlert('Acerca de')">Acerca de</a></li>
            <li><a href="mision.php" onclick="showAlert('Misión')">Misión</a></li>
            <li><a href="vision.php" onclick="showAlert('Visión')">Visión</a></li>
        </ul>
    </nav>
    <section id="content">
        <div class="box">
            <?php 
                // Aquí se puede incluir contenido dinámico
                echo $content ?? '<h2>Inicio</h2><p>::¡Bienvenido a la Página Principal!::</p>'; 
            ?>
        </div>
    </section>
    <footer>
        <p>PHP con TuProyecto &copy; <?php echo date('Y'); ?> | Visitado el: <?php echo date('d/m/Y'); ?></p>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
