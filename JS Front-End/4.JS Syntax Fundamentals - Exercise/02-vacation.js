function solve(count, type, day) {
    let singlePrice = 0;

    if (day === 'Friday') {
        switch (type) {
            case 'Students':
                singlePrice = 8.45;
                break;
            case 'Business':
                singlePrice = 10.90;
                break;
            case 'Regular':
                singlePrice = 15;
                break;
        }
    } if (day === 'Saturday') {
            switch (type) {
                case 'Students':
                    singlePrice = 9.80;
                    break;
                case 'Business':
                    singlePrice = 15.60;
                    break;
                case 'Regular':
                    singlePrice = 20;
                    break;
        }
    } if (day === 'Sunday') {
            switch (type) {
                case 'Students':
                    singlePrice = 10.46;
                        break;
                case 'Business':
                    singlePrice = 16;
                        break;
                case 'Regular':
                    singlePrice = 22.50;
                        break;
            }
    }
}


solve(30, 'Students', 'Sunday')