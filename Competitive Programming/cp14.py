def chocolateFeast(n, c, m):
    
    chocolates = 0
    wrappers = 0
    
    chocolates = int(n/c)
    wrappers = chocolates

    while (wrappers >= m):

        temp = int(wrappers/m)
        wrappers = wrappers - (temp*m)
        chocolates += temp
        wrappers += temp

    return chocolates


n = 6
c = 2
m = 2

print(chocolateFeast(n, c, m))