class TwoSum {
    constructor() {
        this.lookup = new Map();
    }
    add(num) {
        if (this.lookup[num.toString()] === undefined) {
            this.lookup[num.toString()] = 1;
        }
        else {
            this.lookup[num.toString()]++;
        }
    }
    find(target) {
        for (var num1 in this.lookup) {
            var num2 = target - parseInt(num1);
            if (num2 in this.lookup && (num2 !== parseInt(num1) || this.lookup(num1) > 1)) {
                return true;
            }
        }
        return false;
    }
}
