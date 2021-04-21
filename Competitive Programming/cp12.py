
def howManyGames(p, d, m, s):
    """
    import math
    ln = math.ceil((p-m)/d)
    l = p + (ln-1)*(-d)

    sn = (ln/2)*(p + l)
    
    if sn > s:
        
        while(sn > s):
            sn -= ln*d
            ln -= 1
    
        print('>')
        return ln

    elif sn < s:
        while(sn < s):
            sn += m
            ln += 1
        print('<')
        return ln
    elif sn == s:
        print('=')
        return ln
    """

    items = 0
    cost = p
    sn = 0
    while sn < s:
        if cost < m:
            cost = m
        
        sn += cost
        items += 1
        cost = cost - d
    
    if sn > s:
        items -= 1

    return items
    

#print(howManyGames(16, 2, 1, 9981))
print(howManyGames(20, 3, 6, 50))