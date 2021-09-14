from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Longest common prefix string
        lcp = ""
        # Base condition
        if strs is None or len(strs) == 0:
            print("strs is" , strs ,"and lenght of strs is", len(strs))
            return lcp
        # Find the minimum length string from the array
        minimumLength = len(strs[0])
        print("First Minimum length is" , minimumLength ,"character is", strs[0] ," and length of array[strs]" , len(strs))

        for i in range(1, len(strs)):
            minimumLength = min(minimumLength, len(strs[i]))
            print(" After Minimum length is" , minimumLength,"character is", strs[i] , "and length of array[strs]" , len(strs))
            # Loop until the minimum length
            #We found minimum length to be 4 for character flow
        for i in range(0, minimumLength):
            # Get the current character from the first string
            current = strs[0][i]
            print("Current character from 1st string is" , current)
            # Check if this character is found in all other strings or not
            for j in range(0, len(strs)):
                print("strs[j][i]" ,strs[j][i] )
                if strs[j][i] != current:
                    return lcp
            lcp += current
            print("lcp",lcp)
        return lcp
