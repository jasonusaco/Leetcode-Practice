def canPermutePalindrome(s):
    lookup = {}
    count = 0
    for elem in s:
        lookup[elem] = lookup.get(elem, 0) + 1
    for val in lookup.values():
        count += val%2
    return count <= 1
