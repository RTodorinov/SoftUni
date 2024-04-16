function solve(input) {
    const barsitaCount = Number(input.shift());
    const team = {};

    for (let i = 0; i < barsitaCount; i++) {
        const [name, shift, coffeeTypes] = input[i].split(' ');

        team[name] = {
            shift,
            coffeeTypes: coffeeTypes.split(','),
        }
    }
    
    console.log(team); // само с входа за да тествамe какво вкарвамe в масива
    
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