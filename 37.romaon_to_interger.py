# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the xrange from 1 to 3999.
#
# Time:  O(n)
# Space: O(1)


class Solution:
    @staticmethod
    def roman_to_integer(s):
        r2i = {"I": 1, "V": 5, "X": 10, "L": 50,
               "C": 100, "D": 500, "M": 1000}
        d = 0
        for i in range(len(s)):
            if i >= 1 and r2i[s[i]] > r2i[s[i - 1]]:
                d += r2i[s[i]] - (2 * r2i[s[i - 1]])
            else:
                d += r2i[s[i]]
        return d


if __name__ == "__main__":
    print(Solution().roman_to_integer("IIVX"))
    print(Solution().roman_to_integer("MMMCMXCIX"))
