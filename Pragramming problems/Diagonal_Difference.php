/*

Given a square matrix, calculate the absolute difference between the sums of its diagonals. 
Input is a multidimentional array.

Question level: easy

Code is cumputed in PHP but code is explained
*/

                                                                  //Algo started from here
                                                                  
                                                                  
function diagonalDifference($arr) {
    
    $first_dia = 0;
    $second_dia = 0;

    //loop upto n
    for($i = 0;$i<count($arr); $i++){

        //Sum of first diagonal
        $first_dia += $arr[$i][$i];

        //Sum of second diagonal
        $second_dia += $arr[count($arr)-$i -1][$i];

    }
        return abs($first_dia - $second_dia);

}
                                                                    //End of algo



//Input taking. Not more impoertant
$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$n = intval(trim(fgets(STDIN)));

$arr = array();

for ($i = 0; $i < $n; $i++) {
    $arr_temp = rtrim(fgets(STDIN));

    $arr[] = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));
}

$result = diagonalDifference($arr);

fwrite($fptr, $result . "\n");

fclose($fptr);

    © 2020 GitHub, Inc.
    Terms
    Privacy
