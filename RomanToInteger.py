class Solution:
    def romanToInt(self, s: str) -> int:
        # Creating a dictionary of roman number
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # finding length of number
        n = len(s)
        # for storing result
        total = d[s[n - 1]]
        print("First value", total)

        for i in range(n - 2, -1, -1):
            print("Value of i", i, "and string value is s[i]", s[i], "dictionary value is d[s[i]]", d[s[i]], "dictionary next value is d[s[i+1]]", d[s[i + 1]])
            if d[s[i]] >= d[s[i + 1]]:
                print("Since d[s[i]] is greater than d[s[i+1]]: ", d[s[i]])
                total += d[s[i]]
                print("After addition total:" ,total)
            else:
                total -= d[s[i]]
                print("After subtraction total:", total)
        return total
