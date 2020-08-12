/*

Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of 
the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. 
You must determine how many ways she can divide the chocolate.

Output will be the count of possible segments.

*/

<?php

// Complete the birthday function below.
function birthday($s, $d, $m) {

    $count = 0;

    //Selecting segments according to the $d
    
    for($i = 0 ; $i < (count($s)-$m+1) ; $i++){

        $sum = 0;
        for($j=$i; $j<$i+$m; $j++){

            $sum += $s[$j];

        }

        if($sum == $d){
            $count++;
        }

    }

    return $count;

}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$n = intval(trim(fgets(STDIN)));

$s_temp = rtrim(fgets(STDIN));

$s = array_map('intval', preg_split('/ /', $s_temp, -1, PREG_SPLIT_NO_EMPTY));

$dm = explode(' ', rtrim(fgets(STDIN)));

$d = intval($dm[0]);

$m = intval($dm[1]);

$result = birthday($s, $d, $m);

fwrite($fptr, $result . "\n");

fclose($fptr);
