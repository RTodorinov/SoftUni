function solve(age) {
    // if (age >= 0 & age <= 2 ) {
    //     console.log('baby');
    // } else if (age >= 3 & age <= 13) {
    //     console.log('child');
    // } else if (age >= 14 & age <= 19) {
    //     console.log('teenager');
    // } else if (age >= 20 & age <= 65) {
    //     console.log('adult');
    // } else if (age >= 66) {
    //     console.log('elder');
    // } else {
    //     console.log('out of bounds');
    // }

    if (age >= 66) {
        result = 'elder';
    } else if (age >= 20) {
        result = 'adult';
    } else if (age >= 14) {
        result = 'teenager'
    } else if (age >= 3) {
        result = 'child';
    } else if (age >= 0) {
        result = 'baby';
    } else {
        result = 'out of bounds';
    }
    console.log(result)
}

solve(20);
solve(1);
solve(100);
solve(-1);