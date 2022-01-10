import val as val

import LongestCommonPrefix
import ReverseInteger
import RomanToInteger
import TwoSum
import PalindromeNumber
import ValidParentheses
import AddTwoNumber
import BuildArrayfromPermutation
import ContainsDuplicate
import RunningSumof1Darray
import cipher
import badNumbers

# =============================================#
'''------Two Sum ---------
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8

s = TwoSum.Solution()
s1 = TwoSum.Solutionfast()
s2 = TwoSum.SolutionHash()

print(s.twoSum(num, target))
print(s1.twoSum(num, target))
print(s2.twoSum(num, target))
'''
# =============================================#
'''
#-----Reverse Integer------#
revInt = ReverseInteger.Solution()
print(revInt.reverse(120))
print(revInt.reverse(123))
print(revInt.reverse(-123))
print(revInt.reverse(0))
'''
# =================================================#
'''
#---------PalindromeNumber-----------#
pal = PalindromeNumber.Solution()
print(pal.isPalindrome(121))
'''
# ==================================================
'''
#---------RomanToInetger---------#
rti = RomanToInteger.Solution()
print(rti.romanToInt("XIV"))
print(rti.romanToInt("III"))
print(rti.romanToInt("IX"))
print(rti.romanToInt("LVIII"))
print(rti.romanToInt("MCMXCIV"))
'''
# ==================LongestCommonPrefix=========+#
'''
#------LCP-------
lcp = LongestCommonPrefix.Solution()
print(lcp.longestCommonPrefix(["flower","flow","flight"]))
print(lcp.longestCommonPrefix(["cat","dog","animal"]))

'''

# ===============ValidParentheses===============
'''
vp = ValidParentheses.Solution()
print(vp.isValid("()[]{}"))
print(vp.isValid("([)]"))
'''

# ============TwoSumLinklist=============
'''
atn = AddTwoNumber.ListNode()
print(atn.addTwoNumber(l1=[2, 4, 3], l2=[5, 6, 4]))
'''
#=======================BuildArrayfromPermutation==========
'''
bafp = BuildArrayfromPermutation.Solution()
print(bafp.buildArray([5,0,1,2,3,4]))
'''

#==========ContainsDuplicate=============
'''
cd = ContainsDuplicate.Solution()
print(cd.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
'''
#=============RunningSumof1darray========
'''
rso1d = RunningSumof1Darray.Solution()
print(rso1d.runningSum([[3,1,2,10,1]]))
'''
#======================================
'''
cipher = cipher.Solution()
print(cipher.decrypt(string="CDEF",k="2"))
'''
#=========================================

def pairs(num):
    print(num[:-1])
    print(num[1:])
    print("zip of numbers", zip(num[:-1], num[1:]))
    return zip(num[:-1], num[1:])


def goodSegment(bad_numbers, l, r):
    print("Bad Numbers are ", bad_numbers)
    print("Lower value", l)
    print("Last value", r)
    #bad_numbers = [l - 1] + sorted(x for x in bad_numbers if l <= x <= r) + [r + 1]
    bad_numbers = [l - 1] + g + [r + 1]
    print("The bad numbers are", bad_numbers)
    gap_lengths = (b - a for a, b in pairs(bad_numbers))
    print(c for c in gap_lengths)
    return max(gap_lengths) - 1


badNumbers = [37, 7, 22, 15, 49, 60]
l = 3
r = 48

result = goodSegment(badNumbers, l, r)
print(result)