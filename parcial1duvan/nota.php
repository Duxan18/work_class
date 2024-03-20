<html>
    <head>
        <title>Problema</title>
            </head>
            <body>
                <?php
                    $nota1 = 2;
                    $nota2 = 3;
                    $nota3 = 4;
                    $sum = ($nota1 + $nota2 + $nota3)/3;

                        if ($sum >= 3)
                        {
                            echo "Juan paso la materia con $sum";
                        }
                        else
                        {
                            echo "Juan perdio la materia con $sum";
                        }
                ?>
            </body>
</html>