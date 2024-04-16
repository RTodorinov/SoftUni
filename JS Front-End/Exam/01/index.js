function solve(input) {
    const characterCount = Number(input.shift());
    const posse = {};

    
    for (let i = 0; i < characterCount; i++) {
        const [name, hp, bullets] = input[i].split(' ');

        posse[name] = {
            hp: parseInt(hp),
            bullets: parseInt(bullets),
        }
    }

    const output = [];

    
    let commandLine = input.shift();
    while (commandLine !== 'Ride Off Into Sunset') {
        const [command, ...params] = commandLine.split(' - ');
        const charName = params.shift();
        const character = posse[charName];

        switch (command) {
            case 'FireShot':
                const target = params[0];
                if (character.bullets > 0) {
                    character.bullets--;
                    output.push(`${charName} has successfully hit ${target} and now has ${character.bullets} bullets!`);
                } else {
                    output.push(`${charName} doesn't have enough bullets to shoot at ${target}!`);
                }
                break;
            case 'TakeHit':
                const damage = parseInt(params[0]);
                const attacker = params[1];
                character.hp -= damage;
                if (character.hp > 0) {
                    output.push(`${charName} took a hit for ${damage} HP from ${attacker} and now has ${character.hp} HP!`);
                } else {
                    output.push(`${charName} was gunned down by ${attacker}!`);
                    delete posse[charName];
                }
                break;
            case 'Reload':
                if (character.bullets < 6) {
                    const bulletsReloaded = 6 - character.bullets;
                    character.bullets = 6;
                    output.push(`${charName} reloaded ${bulletsReloaded} bullets!`);
                } else {
                    output.push(`${charName}'s pistol is fully loaded!`);
                }
                break;
            case 'PatchUp':
                const amount = parseInt(params[0]);
                if (character.hp === 100) {
                    output.push(`${charName} is in full health!`);
                } else {
                    character.hp += amount;
                    if (character.hp > 100) character.hp = 100;
                    output.push(`${charName} patched up and recovered ${amount} HP!`);
                }
                break;
        }

        commandLine = input.shift();
    }

    
    const remainingCharacters = Object.entries(posse);
    remainingCharacters.forEach(([charName, char]) => {
        output.push(`${charName}\n HP: ${char.hp}\n Bullets: ${char.bullets}`);
    });

    console.log(output.join('\n'));
}


solve([
    '2',
    'Gus 100 0',
    'Walt 100 6',
    'FireShot - Gus - Bandit',
    'TakeHit - Gus - 100 - Bandit',
    'Reload - Walt',
    'Ride Off Into Sunset'
]);