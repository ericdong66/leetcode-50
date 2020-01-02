/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var lookup = {};
    var ans = [];
    for (var i = 0; i < nums.length; i++) {
        var num = target - nums[i];
        if (lookup[num.toString()] === undefined) {
            lookup[nums[i].toString()] = i;
        } else {
            ans = [i, lookup[num.toString()]];
            break;
        }
    }
    return ans;
};