def nonDivisibleSubset(k, s):
    
    freq = [0 for i in range(k)]
    for i in range(len(s)):
        freq[s[i] % k] += 1
    
    if k%2 == 0:
        freq[k//2] = min(freq[k//2], 1)

    res = min(freq[0], 1)

    for i in range (1, (k//2)+1):
        res += max(freq[i], freq[k-i])
    
    return res

print(nonDivisibleSubset(3, [1, 7, 2, 4]))
print(nonDivisibleSubset(7, [278 ,576 ,496 ,727 ,410 ,124 ,338 ,149 ,209 ,702 ,282 ,718 ,771 ,575 ,436]))