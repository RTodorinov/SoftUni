

//function solve(first, second, third) {
//    const largestNumber = Math.max(first, second, third);
//
//    console.log('The largest number is ${largestNumber}');
//}
//
//solve(5, -3, 16);
//solve(-3, -5, -22.5);


function findLargestNumber(num1, num2, num3) {
    let largest;

    if (num1 >= num2 && num1 >= num3) {
        largest = num1;
    } else if (num2 >= num1 && num2 >= num3) {
        largest = num2;
    } else {
        largest = num3;
    }

    console.log(`The largest number is ${largest}.`);
}

// Example usage:
findLargestNumber(5, -3, 16);
findLargestNumber(-3, -5, -22.5);

