
function printMonth(number) {
    // Array of month names
    const months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ];

    // Check if the number is within bounds
    if (number >= 1 && number <= 12) {
        console.log(months[number - 1]); // Print the corresponding month
    } else {
        console.log("Error!"); // Print "Error!" if out of bounds
    }
}

// Test cases
printMonth(5); // Output: May
printMonth(13); // Output: Error!
printMonth(-3); // Output: Error!
