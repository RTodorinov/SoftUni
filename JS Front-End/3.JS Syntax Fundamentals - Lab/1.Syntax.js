// Declare variables
let a = 10;
let b = 20;
console.log(a + b);

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
