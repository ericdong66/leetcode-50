/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    var res = [];
    var arr = s.split(' ')
    for (var each in arr){
        if (!arr[each]) continue;
        res.unshift(arr[each]);
    }
    return res.join(' ');
};