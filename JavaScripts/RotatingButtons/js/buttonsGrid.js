let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");
let btn6 = document.getElementById("btn6");
let btn7 = document.getElementById("btn7");
let btn8 = document.getElementById("btn8");
let btn9 = document.getElementById("btn9");

let arr = [btn1, btn2, btn3, btn6, btn9, btn8, btn7, btn4];

function rotate() {
	
	let temp = btn4.innerHTML;
	
	for(let i = 7; i>0; i--){
		
		arr[i].innerHTML = arr[i-1].innerHTML;
		
	}
	
	arr[0].innerHTML = temp;
	
}
