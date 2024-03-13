// Declare variables
let a = 10;
let b = 20;
console.log(a + b);

// Reassign variable defined with let
a = 11;
console.log(a + b)

var c = 30; // used before ES2015 old style (legacy) for same thing above and not recommended to use
console.log(c + a);

const pi = 3.14; // Constant variable

// Conditional Statements
if (a < b) {
    console.log('a is lower then 10');
} else if (a < 20) {
    console.log('a is lower than 20');
} else {
    console.log('a is higher than or equal to 20');
}

// expression // трябва да има ;
// statements // не трябва да има ;

// Function declaration
function add(first, second) {
    console.log(first + second);
}

// Function invocation(calling)
add(1, pi);

// Console print with string concatenation
console.log('The number pi is: ' + pi + '!')

// String interpolation
console.log(`The number pi is: ${pi}!!`);

// fix the number output
console.log(pi.toFixed(2));

let num = 5.19923;
console.log(num.toFixed(2));

console.log(10 + '2');

// Single vs double quotes for strings
console.log("mr." + 'Pesho'); // Not recommended to mix both
console.log("Gosho");

// Roundng vs toFixed
console.log(pi.toFixed(5)); // used to fix by number in quotes
console.log(Math.round(pi)); // round to nearest integer

//Switch statement
const firstName = 'pesho';
switch (firstName) {
    case 'gosho':
        console.log('Zdrasti gosho');
        break;
    case 'pesho':
        console.log('Maraba pesho');
        break;
    default:
        console.log('Koi si ti?');
        break;
} 

// Truthy and falsy values
if (firstName) {
    console.log('There is pesho');
} else {
    console.log('There is no pesho');
}

// For loop
// i++ i-- ++i --i

for (let i = 0; i < 10; i++) {
    console.log(i);
}
// While loop

let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}

// Undefined
let futureValue;

console.log(typeof futureValue);