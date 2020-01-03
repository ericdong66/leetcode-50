/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    var i = 0;
    var j = numbers.length - 1;
    while (i < j) {
        sum = numbers[i] + numbers[j]
        if (sum < target) {
            i++
        } else if (sum > target) {
            j--
        } else {
            return [i+1, j+1]
        }
    }
};