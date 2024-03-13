<html>
    <head></head>
        <body>
        <?php
        $dia = date("Y-m-d");
        $cum = "2024-12-27";
        echo "$dia: dia de hoy";
        echo "<br>";
        echo "$cum: fecha de cumpleaños";
        $res = (strtotime($cum)- strtotime($dia))/86400;
        echo "<br>";
        echo "faltan $res para cumplir años";
        ?>
    </body>
</html>