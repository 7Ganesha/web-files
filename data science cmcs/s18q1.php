<?php
$array = array("Math" => 36, "English" => 40, "Marathi" => 50);

$selected=$_POST['op'];

switch ($selected) {
    case '1':$array=array_flip($array);
    print_r($array);
    break;
    case '2':shuffle($array);
    print_r($array);
    break;
    case '3':
        extract($array);
        echo "Math : $Math , English : $English , Marathi : $Marathi ";
    break;
    case "4":
        foreach($array as $key => $value){
            echo "$key=>$value,";
        }
}
?>
