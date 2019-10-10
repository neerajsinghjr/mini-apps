/* ------------------ Js Code ------------------------*/

var array = [150, 210, 100, 40, 70, 1000, 90, 10];

var car =  ["Corvett", "Paurse", "Mclaren", "GTR 300"];

console.log("Cars: " + car.sort());

console.log("Asc Order: " + array.sort(function(a, b){
	return a-b;
}));

// console.log("Des Order: " + array.sort(function(a, b){
// 	return b-a;
// }));

console.log("Maximum: " + array[array.length-1]);
console.log("Minimum: " + array[0]);