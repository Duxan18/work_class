<html>
<head>
    <title>Número Aleatorio</title>
</head>
<body>
<?php
    // Generar y mostrar un número aleatorio entre 1 y 10
    $numero_aleatorio = rand(1, 10);
    echo "<p>El número aleatorio es: $numero_aleatorio</p>";

    function numero_nombre ($numero_aleatorio) {
        if ($numero_aleatorio == 1) {
            return "Uno";
        } elseif ($numero_aleatorio == 2) {
            return "Dos";
        } elseif ($numero_aleatorio == 3) {
            return "Tres";
        } elseif ($numero_aleatorio == 4) {
            return "Cuatro";
        } elseif ($numero_aleatorio == 5) {
            return "Cinco";
        } elseif ($numero_aleatorio == 6) {
            return "Seis";
        } elseif ($numero_aleatorio == 7) {
            return "Siete";
        } elseif ($numero_aleatorio == 8) {
            return "Ocho";
        } elseif ($numero_aleatorio == 9) {
            return "Nueve";
        } elseif ($numero_aleatorio == 10) {
            return "Diez";
        } else {
            return "Número no válido";
        }
    };

    $nombre_num = numero_nombre($numero_aleatorio);
    echo "El número se llama: $nombre_num";
?>

</body>
</html>