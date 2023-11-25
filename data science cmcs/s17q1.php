<?php
    $array=array("Sagar"=>"31","Vicky"=>"41","Leena"=>"39","Ramesh"=>"40");

    echo "a) ascending order sort by Value<br>";
    asort($array);
    foreach($array as $key => $value){
        echo "Age of ".$key."is:".$value."<br>";
    }

    echo "b) ascending order sort by Key<br>";
    ksort($array);
    foreach($array as $key => $value){
        echo "Age of ".$key."is:".$value."<br>";
    }

    echo "c) descending order sorting by Value<br>";
    arsort($array);
    foreach($array as $key => $value){
        echo "Age of ".$key."is:".$value."<br>";
    }

    echo "d) descending order sorting by Key<br>";
    krsort($array);
    foreach($array as $key => $value){
        echo "Age of ".$key."is:".$value."<br>";
    }
?>