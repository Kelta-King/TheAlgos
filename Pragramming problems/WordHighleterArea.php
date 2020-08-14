/*
When you select a contiguous block of text in a PDF viewer, the selection is highlighted
with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

In this challenge, you will be given a list of letter heights in the alphabet and a string. 
Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

*/
<?php

// Complete the designerPdfViewer function below.
function designerPdfViewer($h, $word) {

    $alpha = array('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z');
    $heights = array();

    for($i=0;$i<count($alpha);$i++){

        $heights[$alpha[$i]] = $h[$i];

    }

    $length = 0;
    $width = strlen($word);
    for($i=0; $i<strlen($word);$i++){

        $length = max($length, $heights[$word[$i]]);
        
    }

    return $length*$width;

}

$fptr = fopen(getenv("OUTPUT_PATH"), "w");

$stdin = fopen("php://stdin", "r");

fscanf($stdin, "%[^\n]", $h_temp);

$h = array_map('intval', preg_split('/ /', $h_temp, -1, PREG_SPLIT_NO_EMPTY));

$word = '';
fscanf($stdin, "%[^\n]", $word);

$result = designerPdfViewer($h, $word);

fwrite($fptr, $result . "\n");

fclose($stdin);
fclose($fptr);
