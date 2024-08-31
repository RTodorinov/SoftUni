function superheroGame(input) {
    const n = parseInt(input[0]);
    const superheroes = {};

    // Initialize superheroes
    for (let i = 1; i <= n; i++) {
        const [name, superpowers, energy] = input[i].split("-");
        superheroes[name] = {
            superpowers: new Set(superpowers.split(",")),
            energy: parseInt(energy)
        };
    }

    // Process commands
    for (let i = n + 1; i < input.length; i++) {
        const [command, name, param1, param2] = input[i].split(" * ");

        if (command === "Evil Defeated!") break;

        switch (command) {
            case "Use Power":
                const superpower = param1;
                const energyRequired = parseInt(param2);
                if (superheroes[name].superpowers.has(superpower) && superheroes[name].energy >= energyRequired) {
                    superheroes[name].energy -= energyRequired;
                    console.log(`${name} has used ${superpower} and now has ${superheroes[name].energy} energy!`);
                } else {
                    console.log(`${name} is unable to use ${superpower} or lacks energy!`);
                }
                break;

            case "Train":
                const trainingEnergy = parseInt(param1);
                const energyBefore = superheroes[name].energy;
                superheroes[name].energy = Math.min(100, superheroes[name].energy + trainingEnergy);
                const energyGained = superheroes[name].energy - energyBefore;
                if (energyBefore === 100) {
                    console.log(`${name} is already at full energy!`);
                } else {
                    console.log(`${name} has trained and gained ${energyGained} energy!`);
                }
                break;

            case "Learn":
                const newSuperpower = param1;
                if (superheroes[name].superpowers.has(newSuperpower)) {
                    console.log(`${name} already knows ${newSuperpower}.`);
                } else {
                    superheroes[name].superpowers.add(newSuperpower);
                    console.log(`${name} has learned ${newSuperpower}!`);
                }
                break;
        }
    }

    // Print the final state of each superhero
    for (const name in superheroes) {
        console.log(`Superhero: ${name}`);
        console.log(`- Superpowers: ${Array.from(superheroes[name].superpowers).join(", ")}`);
        console.log(`- Energy: ${superheroes[name].energy}`);
    }
}

// Example input
const input = [
    "3",
    "Iron Man-Repulsor Beams,Flight-80",
    "Thor-Lightning Strike,Hammer Throw-10",
    "Hulk-Super Strength-60",
    "Use Power * Iron Man * Flight * 30",
    "Train * Thor * 20",
    "Train * Hulk * 50",
    "Learn * Hulk * Thunderclap",
    "Use Power * Hulk * Thunderclap * 70",
    "Evil Defeated!"
];

superheroGame(input);
