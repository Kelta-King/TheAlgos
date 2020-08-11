/*

This is a military time conversion problem. 
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock. 
Input will be in dtring format.
Output must be in same format.

*/

<?php

function timeConversion($s) {
        
        if($s == "12:00:00AM"){
            return "00:00:00";
        }

        if($s == "12:00:00PM"){
            return "12:00:00";
        }

        //dividing string in variables;
        $times = explode(":", $s);
        $hhm = $times[0];
        $mmm = $times[1];
        $ssm = substr($times[2], 0, 2);
        $ap = substr($times[2], 2, 4);

        //Here we just have to take care of all 12 AM and 12 PM hh time
        
        if($ap == "PM"){

            if($hhm != "12"){
               $hhm = (int)$hhm + 12;
            }
            return $hhm.":".$mmm.":".$ssm;
        }
        else if($ap == "AM"){
            
            if($hhm == "12"){
                $hhm = "00";
            }
            
        }
        
        return $hhm.":".$mmm.":".$ssm;
}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$__fp = fopen("php://stdin", "r");

fscanf($__fp, "%[^\n]", $s);

$result = timeConversion($s);

fwrite($fptr, $result . "\n");

fclose($__fp);
fclose($fptr);
