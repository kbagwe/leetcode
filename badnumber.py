def pairs(numbers):
    print(":ffsafafsdfv")
    print(numbers[:-1])
    print(numbers[1:])
    return zip(numbers[:-1], numbers[1:])

def goodSegment(bad_numbers, l, u):
    bad_numbers = [l - 1] + sorted(x for x in bad_numbers if l <= x <= u) + [u + 1]
    print(bad_numbers)
    print(list(pairs(bad_numbers)))
    gap_lengths = (b - a for a, b in pairs(bad_numbers))
    print(list(gap_lengths))
    return max(gap_lengths) - 1


badNumbers = [5, 4, 2, 15]
"""
[37,7,22,15,49,60] l=3 u=48
[7,15,22,37,49,60] l=3 u=48

 [2] + [7,15,22,37] + [49]
 = [2, 7, 15, 22, 37, 49]

Time complexity  is O(n^2 logn) 
Another approach is using min heap and heapify

"""
l = 1
r = 10

result = goodSegment([37,7,22,15,49,60], 3, 48)
print(result)