'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 * 
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
 */

function sf2(p, a){
    
    let x = (p - Math.sqrt((p*p) - (16*a)))/4;
    
    return x;
    
}

function sf1(p, a){
    
    let x = (p + Math.sqrt((p*p) - (16*a)))/4;
    
    return x;
    
}

function sides(literals, ...expressions) {
    
    let s1 = sf1(expressions[1], expressions[0]);
    let s2 = sf2(expressions[1], expressions[0]);
    
    expressions[0] = s1;
    expressions[1] = s2;
    
    expressions.sort(function( a , b){
        if(a > b) return 1;
        if(a < b) return -1;
        return 0;
    });
    
    return  expressions;
    
}


function main() {
    let s1 = +(readLine());
    let s2 = +(readLine());
    
    [s1, s2] = [s1, s2].sort();
    
    const [x, y] = sides`The area is: ${s1 * s2}.\nThe perimeter is: ${2 * (s1 + s2)}.`;
    
    console.log((s1 === x) ? s1 : -1);
    console.log((s2 === y) ? s2 : -1);
}
