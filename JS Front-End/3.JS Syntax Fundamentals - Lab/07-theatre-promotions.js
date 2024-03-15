function calculateTicketPrice(day, age) {
    if (age >= 0 && age <= 18) {
        switch (day) {
            case "Weekday":
                console.log("12$");
                break;
            case "Weekend":
                console.log("15$");
                break;
            case "Holiday":
                console.log("5$");
                break;
            default:
                console.log("Error!");
        }
    } else if (age > 18 && age <= 64) {
        switch (day) {
            case "Weekday":
                console.log("18$");
                break;
            case "Weekend":
                console.log("20$");
                break;
            case "Holiday":
                console.log("12$");
                break;
            default:
                console.log("Error!");
        }
    } else if (age > 64 && age <= 122) {
        switch (day) {
            case "Weekday":
                console.log("12$");
                break;
            case "Weekend":
                console.log("15$");
                break;
            case "Holiday":
                console.log("10$");
                break;
            default:
                console.log("Error!");
        }
    } else {
        console.log("Error!");
    }
}

calculateTicketPrice('Weekday', 42);
calculateTicketPrice('Holiday', -12);
calculateTicketPrice('Holiday', 15);

function calculateTicketPrice(day, age) {
    let price;
    
    if (age >= 0 && age <= 18) {
        switch (day) {
            case "Weekday":
                price = 12;
                break;
            case "Weekend":
                price = 15;
                break;
            case "Holiday":
                price = 5;
                break;
            default:
                console.log("Error!");
                return;
        }
    } else if (age > 18 && age <= 64) {
        switch (day) {
            case "Weekday":
                price = 18;
                break;
            case "Weekend":
                price = 20;
                break;
            case "Holiday":
                price = 12;
                break;
            default:
                console.log("Error!");
                return;
        }
    } else if (age > 64 && age <= 122) {
        switch (day) {
            case "Weekday":
                price = 12;
                break;
            case "Weekend":
                price = 15;
                break;
            case "Holiday":
                price = 10;
                break;
            default:
                console.log("Error!");
                return;
        }
    } else {
        console.log("Error!");
        return;
    }

    console.log(`${price}$`);
}

calculateTicketPrice('Weekday', 42);
calculateTicketPrice('Holiday', -12);
calculateTicketPrice('Holiday', 15);