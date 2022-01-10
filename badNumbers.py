def pairs(num):
    print(num[:-1])
    print(num[1:])
    print("zip of numbers", zip(num[:-1], num[1:]))
    return zip(num[:-1], num[1:])


def goodSegment(bad_numbers, l, r):
    print("Bad Numbers are ", bad_numbers)
    print("Lower value", l)
    print("Last value", r)

    bad_numbers = [l - 1] + sorted(x for x in bad_numbers if l <= x <= r) + [r + 1]
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