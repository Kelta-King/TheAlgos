<?php

/*

This is an easy question of CP.

Students grades are in range of 0 to 100. Any grade less than 40 means failing. Teacher wants to round the grades as such way that...
If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5. 
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

Try to solve it by your self. Then visit the solution here.

*/

function roundGrade($mark){

    if($mark < 38){
        return $mark;
    }

    // 40 to 100
    for($i = 8; $i<=20 ;$i++){

        if($i*5 > $mark){

            if(($i*5 - $mark) < 3){
                return $i*5;
            }
            else{
                return $mark;
            }

        }

    }
    //if mark is 100 then return this.
    return $mark;
    
}

function gradingStudents($grades) {
    
    for($i = 0; $i<count($grades); $i++){

        //calling round grade function for all grades.
        $grades[$i] = roundGrade($grades[$i]);

    }

    return $grades;
    
}


                        //Algo is over

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$grades_count = intval(trim(fgets(STDIN)));

$grades = array();

for ($i = 0; $i < $grades_count; $i++) {
    $grades_item = intval(trim(fgets(STDIN)));
    $grades[] = $grades_item;
}

$result = gradingStudents($grades);

fwrite($fptr, implode("\n", $result) . "\n");

fclose($fptr);
