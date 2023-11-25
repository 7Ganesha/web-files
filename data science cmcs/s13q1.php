<!DOCTYPE html>
<html>
    <head>
    <title>chess bord</title>
    <style>
        table{
            border-collapse: collapse;
        }

        td{
            width: 50px;
            height: 50px;
        }
        .black{
            background-color: black;
        }
        .white{
            background-color: white;
        }
    </style>
    </head>
    <body>
        <table>
            <?php
                for($i=1;$i<=8;$i++){
                    echo "<tr>";
                    for($j=1;$j<=8;$j++){
                        $class=($i+$j)%2===0? "black" : "white";
                        echo "<td class=$class></td>";
                    }
                    echo"</tr>";
                }
            ?>
        </table>
    </body>
</html>