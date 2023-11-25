<?php
$n1=$_POST['n1'];
$n2=$_POST['n2'];
$selected=$_POST['op'];

function mod($n1,$n2){
    $ans=$n1%$n2;
    echo "$ans";
}
function power($n1,$n2){
    echo pow($n1,$n2);
}
function sum($n1){
    $sum=0;
    for($i= 0;$i<=$n1;$i++){
        $sum+=$i;
    }
    echo $sum;
}
function fact($n2){
    $fact=1;
    for($i= 1;$i<=$n2;$i++){
        $fact=$i*$fact;
    }
    echo $fact;
}

switch($selected){
    case '1':
        mod($n1,$n2);
        break;
    case '2':
        power($n1,$n2);
        break;
    case '3':
        sum($n1);
        break;
    case '4':
        fact($n2);
        break;
}
?>