#!/usr/bin/node

let x = process.argv.slice(2);;
//console.log(x);
if (Number.isNaN(Number(x[0])) === false) {
	console.log("My number: " + Number(x[0]));
}
else {
	console.log("Not a number");
} 
