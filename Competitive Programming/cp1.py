
def appendAndDelete(s, t, k):
    
    lenS = len(s)
    lenT = len(t)
    
    if (lenT + lenS) < k:
        return "Yes"

    cmn = 0
    for i in range(min(lenS, lenT)):

        if s[i] == t[i]:
            cmn += 1
        else:
            break
    x = k - lenS - lenT + 2*(cmn)
    print(x)
    if(x>=0 and x%2 == 0):
        return "Yes"
    
    return "No"

print(appendAndDelete("hackerhappy", "hackerrank", 9))