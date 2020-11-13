/*

We define S to be a sequence of distinct sequential integers from 1 to n; in other words, S = {1,2,...,n} . 
We want to know the maximum bitwise AND value of any two integers, a and b (where a < b), in sequence S that is also less than a given integer, k.

Complete the function in the editor so that given n & k, it returns the maximum a & b < k.

*/



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


function getMaxLessThanK(n,k){
    
    let arr = [];
    let max = 0;
    let temp = 0;
    let n1, n2 = 0;
    
    for(let i=0 ; i<n ; i++){
        
        arr[i] = i+1;
        
    }
    
    for(let i=0; i<n; i++){
        
        for(let j=i+1; j<n ; j++){
            
            n1 = arr[i];
            n2 = arr[j];
            
            temp = n1 & n2;
            
            if(temp > max){
                
                if(temp < k){
                    max = temp;
                }
                
            }
                        
        }
               
    }
    
    return max;
    
}


function main() {

    const q = +(readLine());
    
    for (let i = 0; i < q; i++) {
        
        const [n, k] = readLine().split(' ').map(Number);
        
        console.log(getMaxLessThanK(n, k));
        
    }
    
}
