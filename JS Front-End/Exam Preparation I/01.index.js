function solve(input) {
    const barsitaCount = Number(input.shift()); //Extracting Barista Count 
    const team = {}; // Creating Team Object

    for (let i = 0; i < barsitaCount; i++) { //It extracts the number of baristas from the input array and creates an empty object called team.
        const [name, shift, coffeeTypes] = input[i].split(' '); // It then iterates over the barista details from the input array, splitting each line into name, shift, and coffeeTypes.
        
        team[name] = { // It creates an entry in the team object for each barista with their name as the key and an object containing their shift and an array of coffeeTypes as the value.
            shift,
            coffeeTypes: coffeeTypes.split(','),
        }
    }
    // console.log(team); без кода надолу само с входа за да тествам какво вкарвам в масива
    let commandLine = input.shift();

    while (commandLine != 'Closed') { // Processing Commands: It initializes a variable commandLine with the first command from the input array and enters a loop until the command is 'Closed'.
        const [command, name, firstArg, secondArg] = commandLine.split(' / '); // It splits each command line into its components: command, name, firstArg, and secondArg.
        const barista = team[name]; // It retrieves the corresponding barista object from the team object using the name.

        let shift, coffeeType; // It then uses a switch statement to execute different actions based on the command type ('Prepare', 'Change Shift', 'Learn').
        switch (command) { // Inside the switch statement, each case handles a specific command:
            case 'Prepare': // 'Prepare': Checks if the barista is available to prepare the specified coffee type and provides feedback accordingly.
                shift = firstArg;
                coffeeType = secondArg;

                if (barista.shift === shift && barista.coffeeTypes.includes(coffeeType)) {
                    console.log(`${name} has prepared a ${coffeeType} for you!`);
                } else {
                    console.log(`${name} is not available to prepare a ${coffeeType}.`);
                }
                break;
            case 'Change Shift': // 'Change Shift': Updates the shift of the barista and provides feedback.
                shift = firstArg;
                barista.shift = shift;
                console.log(`${name} has updated his shift to: ${shift}`);
                break;
            case 'Learn': // 'Learn': Adds a new coffee type to the barista's list if they don't already know it and provides feedback.
                coffeeType = firstArg;
                if (barista.coffeeTypes.includes(coffeeType)) {
                    console.log(`${name} knows how to make ${coffeeType}.`);
                } else {
                    barista.coffeeTypes.push(coffeeType);
                    console.log(`${name} has learned a new coffee type: ${coffeeType}.`);
                }
                break;
        }

        commandLine = input.shift();
    }

    for (const baristaName in team) { // After processing all commands, it iterates over the team object to display the details of each barista, including their name, shift, and the types of drinks they can prepare.
        console.log(`Barista: ${baristaName}, Shift: ${team[baristaName].shift}, Drinks: ${team[baristaName].coffeeTypes.join(', ')}`);
    }
}

solve([
    '3',
    'Alice day Espresso,Cappuccino',
    'Bob night Latte,Mocha',
    'Carol day Americano,Mocha',
    'Prepare / Alice / day / Espresso',
    'Change Shift / Bob / night',
    'Learn / Carol / Latte',
    'Learn / Bob / Latte',
    'Prepare / Bob / night / Latte',
    'Closed',
]);