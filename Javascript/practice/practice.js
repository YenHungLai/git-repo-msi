// // ctrl+shift+s to enable auto save in sublime.

// // Three ways to declare a variable.
// var myName = "Beau"
// let ourName = "freeCodeCamp"
// const pi = 3.14

// console.log(pi)
// console.log("BItch")
// // alert("Bitch")

// // Array.
// var myArray = [["Element_1"], ["Element_2"]]
// console.log(myArray[1])
// console.log(JSON.stringify(myArray));

// // Function.
// function Func(input){
// 	console.log(input)
// }

// Func(11);

// // Object
// var person = {
// 	fName: "Jacob",
// 	lName: "Lai",
// 	age: "21",
// 	fullName: function(){
// 		return this.fName+' '+this.lName;
// 	}
// };

// console.log(person.fName);
// console.log(person.fullName());

// // // if statement.
// // input = prompt("Enter something: ");
// // if(input == 1){	// == converts data type of both values to the same type for you.
// // 	console.log("You entered 1!!!!!");
// // }
// // else if(input === '3'){	// Does not convert data type for you.	e.g 3 == '3' but 3 === '3'
// // 	console.log("You entered char 3!!!!");
// // }

// // // switch statement.
// // input_1 = prompt("Enter Something: ")
// // switch(input_1){
// // 	case '1':
// // 		alert("You entered 1!!!");
// // 		break;
// // 	case '2':
// // 		console.log("You entered 2!!!");
// // 		break;
// // }

// // Objects.
// var myDog = {
// 	"name": "Camper",
// 	"legs": 4,
// 	"tails": 1,
// 	"Breed": "Corki"
// };

// // Create an instance of the object.
// var dog = myDog;
// console.log(dog);
// console.log(dog.Breed);

// // Add and delete fields.
// myDog.number = 1;
// delete myDog.name;
// console.log(dog);

// // Nested Object.
// var myStorage = {
// 	"car": {
// 		"inside": {
// 			"glove box": "maps",
// 			"passenger seat": "crumbs"
// 		},
// 		"outside": {
// 			"trunk": "jack"
// 		}
// 	}
// };

// var storage_1 = myStorage;
// console.log(storage_1);

// // for loop.
// var myArray = [];

// for (var i = 0; i < 5; i++) {
// 	myArray[i] = i;
// }
// console.log(myArray);

// // parseInt function.
// function convertToInteger(str){
// 	return parseInt(str)
// }

// convertToInteger('56');

// // Ternary operator.
// 1 == 1 ? alert('Ture') : alert('False');

// // ES6
// // Enable strict mode that checks for common coding mistakes and check for errors.
// // "use strict"; 

// // Regex

// document.querySelector('input').addEventListener('change', (e) => {
//     console.log(e.target.value);
//     if (e.target.value.endsWith('pdf')) {
//         alert('pdf!!')
//     }
// })
