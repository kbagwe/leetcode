import LongestCommonPrefix
import ReverseInteger
import RomanToInteger
import TwoSum
import PalindromeNumber
import ValidParentheses
import AddTwoNumber

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

atn = AddTwoNumber.ListNode()
print(atn.addTwoNumber(l1=[2, 4, 3], l2=[5, 6, 4]))

